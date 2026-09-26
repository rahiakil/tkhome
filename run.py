import argparse
import os
import sys

# Simple helper to load .env variables into os.environ
def load_dotenv():
    if os.path.exists(".env"):
        with open(".env", "r") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, val = line.split("=", 1)
                    key = key.strip()
                    val = val.strip().strip("'\"")
                    os.environ[key] = val

# Load environmental variables first
load_dotenv()

from evaluator import EvaluationHarness
from self_improving import PromptOptimizer
from config import DEFAULT_MODEL, DEFAULT_SYSTEM_PROMPT, DATA_PATH, OUTPUT_PATH

def main():
    parser = argparse.ArgumentParser(description="Vertex Smart Categorization - Product Search Result Evaluator Harness")
    parser.add_argument("--mode", type=str, choices=["mock", "openai"], default="mock",
                        help="Run mode. 'mock' runs a smart rule-based heuristic locally (no cost). 'openai' runs OpenAI LLM (requires API key).")
    parser.add_argument("--model", type=str, default=DEFAULT_MODEL,
                        help=f"OpenAI model to use (default: {DEFAULT_MODEL}).")
    parser.add_argument("--input", type=str, default=DATA_PATH,
                        help=f"Path to input JSON file (default: {DATA_PATH}).")
    parser.add_argument("--output", type=str, default=OUTPUT_PATH,
                        help=f"Path to output predictions JSON file (default: {OUTPUT_PATH}).")
    parser.add_argument("--limit", type=int, default=None,
                        help="Limit execution to the first N products (useful for fast development and testing).")
    parser.add_argument("--optimize", action="store_true",
                        help="Run the automated self-improving prompt optimization loop.")
    parser.add_argument("--iterations", type=int, default=2,
                        help="Number of optimization iterations (default: 2).")
    parser.add_argument("--opt-limit", type=int, default=15,
                        help="Number of products to run optimization on (default: 15).")
    args = parser.parse_args()

    print("\n" + "="*80)
    print("                    VERTEX SMART CATEGORIZATION ENGINE HARNESS               ")
    print("="*80)
    print("This harness helps you ingest product search results, predict which results")
    print("are trustworthy, and evaluate against ground truth labels.")
    print("\nAvailable Commands:")
    print("  1. Run Local Smart Heuristic (Default - no OpenAI key needed):")
    print("     python3 run.py --mode mock")
    print("  2. Run OpenAI SOTA LLM Pipeline (Requires OPENAI_API_KEY environment variable):")
    print("     python3 run.py --mode openai")
    print("  3. Run Automated Self-Improving Prompt Loop (Requires OPENAI_API_KEY):")
    print("     python3 run.py --optimize")
    print("="*80 + "\n")

    if args.optimize:
        optimizer = PromptOptimizer(model=args.model, data_path=args.input, output_path=args.output)
        optimizer.optimize(iterations=args.iterations, sample_limit=args.opt_limit)
        sys.exit(0)

    # Initialize and run evaluation harness
    harness = EvaluationHarness(data_path=args.input, output_path=args.output)
    
    # Check for custom optimized system prompt if it exists, otherwise use default
    system_prompt = DEFAULT_SYSTEM_PROMPT
    if os.path.exists("optimized_system_prompt.txt"):
        print("💡 Loaded optimized system prompt from 'optimized_system_prompt.txt'")
        with open("optimized_system_prompt.txt", "r") as f:
            system_prompt = f.read()

    # If running openai mode, double check key
    if args.mode == "openai":
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            print("❌ ERROR: OPENAI_API_KEY environment variable is not set.")
            print("Please run:")
            print("  export OPENAI_API_KEY='your_api_key_here'")
            print("Or run the harness in mock mode using:")
            print("  python3 run.py --mode mock")
            sys.exit(1)

    results = harness.run_eval(
        mode=args.mode,
        model=args.model,
        limit=args.limit,
        system_prompt=system_prompt
    )
    
    harness.print_report(results)

if __name__ == "__main__":
    main()
