import json
from typing import Dict, Any, List
import time
from config import DATA_PATH, OUTPUT_PATH, PRICING, DEFAULT_SYSTEM_PROMPT
from llm_client import HeuristicEvaluator, OpenAILLMEvaluator

class EvaluationHarness:
    """
    Main evaluation harness for Vertex Smart Categorization search results.
    Loads data, runs predictions (LLM or Heuristic), calculates advanced metrics, and formats outputs.
    """
    def __init__(self, data_path: str = DATA_PATH, output_path: str = OUTPUT_PATH):
        import os
        self.data_path = data_path
        
        # If output_path is a directory, append the default filename
        if os.path.isdir(output_path):
            self.output_path = os.path.join(output_path, "search_results_predictions.json")
        else:
            self.output_path = output_path
            
        self.raw_data = self.load_data()

    def load_data(self) -> Dict[str, Any]:
        with open(self.data_path, "r") as f:
            return json.load(f)

    def calculate_metrics(self, ground_truth: List[int], predicted: List[int], all_indices: List[int]) -> Dict[str, Any]:
        """
        Compute binary classification metrics for a single product's search results.
        """
        gt_set = set(ground_truth)
        pred_set = set(predicted)
        all_set = set(all_indices)

        tp = len(gt_set.intersection(pred_set))
        fp = len(pred_set - gt_set)
        fn = len(gt_set - pred_set)
        tn = len(all_set - (gt_set.union(pred_set)))

        precision = tp / (tp + fp) if (tp + fp) > 0 else 1.0 if not gt_set else 0.0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 1.0 if not pred_set else 0.0
        f1 = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0.0
        
        # F2-score puts more emphasis on Recall, F0.5 puts more emphasis on Precision.
        # Given Vertex's business problem: "If the websites are for false information the customers will not trust the system, and our classifications will be wrong because we use incorrect product data."
        # This means Precision is critical to avoid False Positives! So F0.5-score is a highly relevant metric! Let's calculate F0.5 as well.
        beta = 0.5
        f_beta = ((1 + beta**2) * precision * recall) / ((beta**2 * precision) + recall) if (precision + recall) > 0 else 0.0

        return {
            "tp": tp,
            "fp": fp,
            "fn": fn,
            "tn": tn,
            "precision": precision,
            "recall": recall,
            "f1": f1,
            "f_beta_0.5": f_beta,
            "accuracy": (tp + tn) / len(all_indices) if len(all_indices) > 0 else 1.0
        }

    def run_eval(self, mode: str = "mock", model: str = "gpt-4o-mini", limit: int = None, system_prompt: str = DEFAULT_SYSTEM_PROMPT) -> Dict[str, Any]:
        """
        Run the evaluation on the dataset.
        mode can be "mock" (heuristic) or "openai" (LLM).
        """
        print(f"\n🚀 Running evaluation harness in '{mode.upper()}' mode (Model: {model if mode == 'openai' else 'N/A'})...")
        
        if mode == "openai":
            evaluator = OpenAILLMEvaluator(model=model, system_prompt=system_prompt)
        else:
            evaluator = HeuristicEvaluator()

        results = {}
        predictions_json = {}
        
        # Metric aggregators
        total_tp = 0
        total_fp = 0
        total_fn = 0
        total_tn = 0
        
        macro_precision_sum = 0.0
        macro_recall_sum = 0.0
        macro_f1_sum = 0.0
        macro_f_beta_sum = 0.0
        
        # Timing and cost tracking
        start_time = time.time()
        
        items = list(self.raw_data.items())
        if limit:
            items = items[:limit]
            print(f"⚠️ Limiting evaluation to first {limit} products.")

        import concurrent.futures
        
        # We can run parallel requests if in openai mode
        if mode == "openai":
            max_workers = 10  # 10 parallel threads
        else:
            max_workers = 1   # heuristic runs locally, sequentially is fine
            
        def process_item(item_tuple):
            prod_id, prod_info = item_tuple
            product_title = prod_info.get("product_title", "")
            product_description = prod_info.get("product_description", "")
            search_results = prod_info.get("search_results", {})
            ground_truth = prod_info.get("trusted_search_results", [])
            all_indices = [int(k) for k in search_results.keys()]
            
            item_start = time.time()
            predicted_indices, metadata = evaluator.evaluate_product(product_title, product_description, search_results)
            item_latency = time.time() - item_start
            
            return prod_id, product_title, product_description, search_results, ground_truth, all_indices, predicted_indices, metadata, item_latency

        print(f"Executing with ThreadPoolExecutor (max_workers={max_workers})...")
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [executor.submit(process_item, item) for item in items]
            
            for i, future in enumerate(concurrent.futures.as_completed(futures)):
                prod_id, product_title, product_description, search_results, ground_truth, all_indices, predicted_indices, metadata, item_latency = future.result()
                
                # Calculate item metrics
                m = self.calculate_metrics(ground_truth, predicted_indices, all_indices)
                
                # Aggregates for Micro metrics
                total_tp += m["tp"]
                total_fp += m["fp"]
                total_fn += m["fn"]
                total_tn += m["tn"]
                
                # Aggregates for Macro metrics
                macro_precision_sum += m["precision"]
                macro_recall_sum += m["recall"]
                macro_f1_sum += m["f1"]
                macro_f_beta_sum += m["f_beta_0.5"]
                
                # Save predictions
                predictions_json[prod_id] = {
                    "product_title": product_title,
                    "product_description": product_description,
                    "search_results": search_results,
                    "trusted_search_results": ground_truth, # retain original ground truth for reference
                    "llm_trusted_search_results": predicted_indices, # output key as requested in case PDF
                    "metadata": metadata
                }

                # Detailed metrics for this product
                results[prod_id] = {
                    "metrics": m,
                    "latency": item_latency,
                    "predicted": predicted_indices,
                    "ground_truth": ground_truth
                }

                if (i + 1) % 5 == 0 or (i + 1) == len(items):
                    print(f"Processed {i + 1}/{len(items)} products...")

        total_latency = time.time() - start_time
        num_products = len(items)

        # Micro metrics calculation
        micro_precision = total_tp / (total_tp + total_fp) if (total_tp + total_fp) > 0 else 0.0
        micro_recall = total_tp / (total_tp + total_fn) if (total_tp + total_fn) > 0 else 0.0
        micro_f1 = (2 * micro_precision * micro_recall) / (micro_precision + micro_recall) if (micro_precision + micro_recall) > 0 else 0.0
        micro_f05 = ((1 + 0.5**2) * micro_precision * micro_recall) / ((0.5**2 * micro_precision) + micro_recall) if (micro_precision + micro_recall) > 0 else 0.0
        micro_accuracy = (total_tp + total_tn) / (total_tp + total_tn + total_fp + total_fn) if (total_tp + total_tn + total_fp + total_fn) > 0 else 1.0

        # Macro metrics calculation
        macro_precision = macro_precision_sum / num_products
        macro_recall = macro_recall_sum / num_products
        macro_f1 = macro_f1_sum / num_products
        macro_f05 = macro_f_beta_sum / num_products

        # Estimate LLM cost
        cost = 0.0
        if mode == "openai" and model in PRICING:
            input_tokens = evaluator.token_usage["input"]
            output_tokens = evaluator.token_usage["output"]
            cost = (input_tokens * PRICING[model]["input"] + output_tokens * PRICING[model]["output"]) / 1_000_000

        summary = {
            "mode": mode,
            "model": model if mode == "openai" else "heuristic",
            "total_products": num_products,
            "total_search_results_evaluated": total_tp + total_fp + total_fn + total_tn,
            "total_latency_seconds": total_latency,
            "avg_latency_per_product_seconds": total_latency / num_products,
            "estimated_cost_usd": cost,
            "micro_metrics": {
                "precision": micro_precision,
                "recall": micro_recall,
                "f1": micro_f1,
                "f_beta_0.5": micro_f05,
                "accuracy": micro_accuracy,
                "confusion_matrix": {
                    "tp": total_tp,
                    "fp": total_fp,
                    "fn": total_fn,
                    "tn": total_tn
                }
            },
            "macro_metrics": {
                "precision": macro_precision,
                "recall": macro_recall,
                "f1": macro_f1,
                "f_beta_0.5": macro_f05
            }
        }

        # Write predictions file
        with open(self.output_path, "w") as f:
            json.dump(predictions_json, f, indent=2)

        return {"summary": summary, "product_details": results}

    def print_report(self, results: Dict[str, Any]):
        """
        Print a beautiful, well-formatted summary of the run in the terminal,
        and dump it as a persistent text file 'evaluation_report_summary.txt'.
        """
        summary = results["summary"]
        prod_details = results["product_details"]

        report_lines = []
        report_lines.append("="*80)
        report_lines.append("                  VERTEX SMART CATEGORIZATION ENGINE REPORT                  ")
        report_lines.append("="*80)
        report_lines.append(f"Mode:          {summary['mode'].upper()}")
        report_lines.append(f"Model:         {summary['model']}")
        report_lines.append(f"Products:      {summary['total_products']}")
        report_lines.append(f"Total Results: {summary['total_search_results_evaluated']}")
        report_lines.append(f"Total Time:    {summary['total_latency_seconds']:.2f}s (Avg: {summary['avg_latency_per_product_seconds']:.2f}s/product)")
        if summary['mode'] == 'openai':
            report_lines.append(f"Estimated Cost: ${summary['estimated_cost_usd']:.4f}")
        report_lines.append("-"*80)
        report_lines.append("MICRO METRICS (Aggregated across all individual search results):")
        report_lines.append(f"  Precision:   {summary['micro_metrics']['precision'] * 100:.2f}%  (Prevents False Positives - Critical!)")
        report_lines.append(f"  Recall:      {summary['micro_metrics']['recall'] * 100:.2f}%  (Captures relevant sources)")
        report_lines.append(f"  F1-Score:    {summary['micro_metrics']['f1'] * 100:.2f}%")
        report_lines.append(f"  F0.5-Score:  {summary['micro_metrics']['f_beta_0.5'] * 100:.2f}%  (Precision-weighted)")
        report_lines.append(f"  Accuracy:    {summary['micro_metrics']['accuracy'] * 100:.2f}%")
        report_lines.append(f"  Confusion:   TP={summary['micro_metrics']['confusion_matrix']['tp']}, "
                            f"FP={summary['micro_metrics']['confusion_matrix']['fp']}, "
                            f"FN={summary['micro_metrics']['confusion_matrix']['fn']}, "
                            f"TN={summary['micro_metrics']['confusion_matrix']['tn']}")
        report_lines.append("-"*80)
        report_lines.append("MACRO METRICS (Average of metrics computed per product):")
        report_lines.append(f"  Precision:   {summary['macro_metrics']['precision'] * 100:.2f}%")
        report_lines.append(f"  Recall:      {summary['macro_metrics']['recall'] * 100:.2f}%")
        report_lines.append(f"  F1-Score:    {summary['macro_metrics']['f1'] * 100:.2f}%")
        report_lines.append(f"  F0.5-Score:  {summary['macro_metrics']['f_beta_0.5'] * 100:.2f}%")
        report_lines.append("="*80)

        # Show top failures/successes
        report_lines.append("\n🔎 TOP MISMATCHES (Sorted by error count):")
        failures = []
        for prod_id, details in prod_details.items():
            m = details["metrics"]
            total_errors = m["fp"] + m["fn"]
            if total_errors > 0:
                failures.append((prod_id, total_errors, m["fp"], m["fn"], details["ground_truth"], details["predicted"]))

        failures.sort(key=lambda x: x[1], reverse=True)
        for prod_id, errs, fp, fn, gt, pred in failures[:5]:
            report_lines.append(f"  • Product: {prod_id.strip()}")
            report_lines.append(f"    Errors: {errs} (FP={fp}, FN={fn}) | Ground Truth: {gt} | Predicted: {pred}")
        
        if not failures:
            report_lines.append("  🎉 PERFECT RUN! No mismatches found.")
        report_lines.append("="*80 + "\n")

        # Print to terminal
        for line in report_lines:
            print(line)

        # Save to persistent file
        with open("evaluation_report_summary.txt", "w") as f:
            f.write("\n".join(report_lines))
        print("💾 Saved persistent summary report to 'evaluation_report_summary.txt'")
