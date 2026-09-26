import os
import json
from config import DEFAULT_SYSTEM_PROMPT, DATA_PATH, OUTPUT_PATH
from evaluator import EvaluationHarness

class PromptOptimizer:
    """
    Automated Prompt Optimization Loop (Self-Improving Harness).
    Runs the pipeline on a training/validation subset, identifies failures,
    and uses an LLM to automatically refine the prompt. Reruns to verify improvement.
    """
    def __init__(self, api_key: str = None, model: str = "gpt-4o-mini"):
        self.api_key = api_key or os.environ.get("OPENAI_API_KEY")
        self.model = model
        self.harness = EvaluationHarness(DATA_PATH)
        
        # We can import OpenAI here
        if self.api_key:
            from openai import OpenAI
            self.client = OpenAI(api_key=self.api_key)
        else:
            self.client = None

    def optimize(self, iterations: int = 2, sample_limit: int = 15) -> str:
        """
        Runs the self-improvement loop for a number of iterations.
        """
        print("\n" + "="*80)
        print("                  AUTOMATED PROMPT OPTIMIZATION (SELF-IMPROVING)             ")
        print("="*80)
        
        if not self.client:
            print("⚠️ OpenAI API key not found. Performing a DRY RUN of the optimizer...")
            print("The self-improving loop works by:")
            print("  1. Running the evaluator on a validation subset.")
            print("  2. Capturing the false positives (FP) and false negatives (FN).")
            print("  3. Feeding the current system prompt + failure cases to a 'Meta-Optimizer' LLM.")
            print("  4. The Meta-Optimizer analyzes the errors and generates a more refined system prompt.")
            print("  5. The loop reruns evaluation on the subset with the new prompt.")
            print("  6. If the F0.5/F1 score improves, the new prompt is accepted; else, we keep the old one.")
            print("\nThis loop guarantees that the prompt continuously improves based on real feedback.")
            print("="*80 + "\n")
            return DEFAULT_SYSTEM_PROMPT

        current_prompt = DEFAULT_SYSTEM_PROMPT
        best_score = 0.0
        best_prompt = current_prompt

        # First, establish the baseline score with the default prompt
        print(f"🔄 Establishing baseline score on validation split (first {sample_limit} products)...")
        baseline_results = self.harness.run_eval(
            mode="openai", 
            model=self.model, 
            limit=sample_limit, 
            system_prompt=current_prompt
        )
        
        summary = baseline_results["summary"]
        # We optimize for F0.5-score as Precision is critical for avoiding false data ingestion
        best_score = summary["micro_metrics"]["f_beta_0.5"]
        print(f"📊 Baseline F0.5-Score: {best_score * 100:.2f}% (F1-Score: {summary['micro_metrics']['f1'] * 100:.2f}%)")

        for iteration in range(iterations):
            print(f"\n🔄 --- STARTING OPTIMIZATION ITERATION {iteration + 1}/{iterations} ---")
            
            # 1. Collect failure cases
            failures = []
            for prod_id, details in baseline_results["product_details"].items():
                m = details["metrics"]
                if m["fp"] > 0 or m["fn"] > 0:
                    prod_data = self.harness.raw_data[prod_id]
                    failures.append({
                        "product_title": prod_data["product_title"],
                        "product_description": prod_data["product_description"],
                        "search_results": prod_data["search_results"],
                        "ground_truth": prod_data["trusted_search_results"],
                        "predicted": details["predicted"],
                        "fp_count": m["fp"],
                        "fn_count": m["fn"]
                    })
            
            if not failures:
                print("🎉 Perfect score achieved on validation subset! Stopping optimization.")
                break

            print(f"📝 Found {len(failures)} products with matching errors. Sending top 4 to Meta-Optimizer...")
            failures_subset = failures[:4]
            
            # 2. Call OpenAI to optimize the system prompt
            optimization_prompt = f"""You are a Meta-Prompt Optimizer.
Your goal is to refine the system prompt used by an LLM-based search result classifier to improve its performance.
We are optimizing for **F0.5-score**, which prioritizes Precision (avoiding false positives) while maintaining high Recall.

Here is the current system prompt:
\"\"\"
{current_prompt}
\"\"\"

Here are some actual failure cases from the validation run. Look at what the ground truth says is correct vs what the current model predicted:
{json.dumps(failures_subset, indent=2)}

INSTRUCTIONS FOR REFINEMENT:
1. Analyze the mistakes carefully. Describe what specific product dimensions (e.g., brand, flavor, sweetener, format, package type, etc.) the model missed or misunderstood.
2. Formulate 1-2 new, precise rules or instructions to add to the system prompt to prevent these exact errors in the future.
3. Keep the existing rules intact so we do not break correct classifications.
4. Output the complete, revised system prompt. Do not output anything else other than the prompt. Wrap the prompt in triple backticks.
"""

            try:
                meta_response = self.client.chat.completions.create(
                    model="gpt-4o", # Use GPT-4o as the high-quality prompt meta-optimizer
                    messages=[
                        {"role": "system", "content": "You are a professional AI engineer specializing in prompt engineering and automated prompt optimization."},
                        {"role": "user", "content": optimization_prompt}
                    ],
                    temperature=0.2
                )
                
                raw_response = meta_response.choices[0].message.content
                # Extract code block if present
                if "```" in raw_response:
                    refined_prompt = raw_response.split("```")[1]
                    if refined_prompt.startswith("markdown"):
                        refined_prompt = refined_prompt[8:]
                    elif refined_prompt.startswith("plaintext") or refined_prompt.startswith("text"):
                        refined_prompt = refined_prompt[9:]
                else:
                    refined_prompt = raw_response
                
                refined_prompt = refined_prompt.strip()
                
                # 3. Evaluate the new prompt
                print("🧪 Evaluating refined prompt on the same validation split...")
                new_results = self.harness.run_eval(
                    mode="openai", 
                    model=self.model, 
                    limit=sample_limit, 
                    system_prompt=refined_prompt
                )
                
                new_summary = new_results["summary"]
                new_score = new_summary["micro_metrics"]["f_beta_0.5"]
                print(f"📊 Refined F0.5-Score: {new_score * 100:.2f}% (F1-Score: {new_summary['micro_metrics']['f1'] * 100:.2f}%)")
                
                # 4. Compare and Accept/Reject
                if new_score > best_score:
                    print(f"✅ Improvement detected! {best_score * 100:.2f}% ➡️ {new_score * 100:.2f}%. Prompt updated.")
                    best_score = new_score
                    best_prompt = refined_prompt
                    baseline_results = new_results # Update for next iteration
                    current_prompt = refined_prompt
                else:
                    print(f"❌ No improvement ({new_score * 100:.2f}% <= {best_score * 100:.2f}%). Reverting to previous best.")
            
            except Exception as e:
                print(f"⚠️ Error during optimization call: {e}")
                break

        print("\n" + "="*80)
        print(f"🏆 Prompt Optimization Finished. Best F0.5-Score: {best_score * 100:.2f}%")
        print("="*80 + "\n")
        
        # Save the best prompt to config or prompt file
        with open("optimized_system_prompt.txt", "w") as f:
            f.write(best_prompt)
        print("💾 Saved best system prompt to 'optimized_system_prompt.txt'")
        
        return best_prompt
