import os
import re
import json
from typing import List, Dict, Any, Tuple
from pydantic import BaseModel, Field

# Try to import openai, handle failure gracefully
try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False
    OpenAI = None

# Define Pydantic structures for OpenAI Structured Outputs
class SearchResultDecision(BaseModel):
    index: int = Field(description="The index/ID of the search result being evaluated (e.g. 1, 2, 3...)")
    is_trusted: bool = Field(description="True if this search result is for the EXACT product (ignoring size packaging), False otherwise")
    confidence: float = Field(description="Confidence rating of this decision between 0.0 and 1.0")
    explanation: str = Field(description="Concise 1-2 sentence explanation of why this result was trusted or rejected based on the rules (brand, format, flavor, ingredients, single vs combo, etc.)")

class ProductEvaluationResponse(BaseModel):
    results: List[SearchResultDecision] = Field(description="The list of evaluations for each of the provided search results")
    reasoning: str = Field(description="Global step-by-step reasoning explaining key differences observed (e.g., Lite vs Original, Bags vs Bottles, Ale vs Pilsner)")


# --- Heuristic Predictor (Smart Mock Baseline) ---
class HeuristicEvaluator:
    """
    A smart rule-based classifier that acts as a baseline and mock mode.
    Does not require any LLM or API keys.
    """
    def __init__(self):
        pass

    def clean_text(self, text: str) -> str:
        text = text.lower()
        # Remove common size measurements to ignore size differences
        text = re.sub(r'\b\d+(\.\d+)?\s*(oz|oz\b|fl\s*oz|g|ea|ct|pk|pack|ml|zbtl|fl)\b', '', text)
        text = re.sub(r'\b\d+\s*count\b', '', text)
        return text

    def tokenize(self, text: str) -> set:
        cleaned = self.clean_text(text)
        # remove punctuation and split into words
        words = re.findall(r'\b[a-z]{2,}\b', cleaned)
        return set(words)

    def evaluate_product(self, product_title: str, product_description: str, search_results: Dict[str, str]) -> Tuple[List[int], Dict[str, Any]]:
        # Let's clean and tokenize query and description
        full_query = f"{product_title} {product_description}"
        q_tokens = self.tokenize(full_query)
        q_text = full_query.lower()

        # Check if the query is extremely generic (e.g., "Milk, Chocolate", "Large Org Apricot", "Minestrone Soup")
        # Generics usually have very few words and are not branded
        generic_markers = ["soup", "apricot", "lo mein", "milk", "vegetable"]
        is_generic = False
        # If the product name has less than 4 tokens and consists of common food names, mark as generic
        if len(self.tokenize(product_title)) <= 3:
            # Check if any brand-like indicators are missing
            brand_words = ["lipton", "dunkin", "starbucks", "ghirardelli", "theraworx", "monster", "alani", "asepxia", "derma", "v8", "aloha", "birds eye", "rhythm", "cocoa krispies", "chapstick", "capri sun", "equate", "carbon theory", "oaza", "numi"]
            has_brand = any(brand in q_text for brand in brand_words)
            if not has_brand:
                is_generic = True

        predictions = []
        detailed_results = []

        for idx, result_text in search_results.items():
            idx_int = int(idx)
            res_lower = result_text.lower()
            res_tokens = self.tokenize(result_text)

            # Default logic
            is_trusted = True
            rejection_reason = ""
            confidence = 1.0

            # If it's a generic product, never trust specific branded search results
            if is_generic:
                is_trusted = False
                rejection_reason = "Query is a generic product; branded search results are not trusted."
                confidence = 0.9
            else:
                # 1. Brand check: If a major brand is in the query, it MUST be in the search result
                brand_list = ["lipton", "dunkin", "starbucks", "ghirardelli", "theraworx", "monster", "alani", "asepxia", "derma", "v8", "aloha", "birds eye", "rhythm", "cocoa krispies", "chapstick", "capri sun", "equate", "carbon theory", "oaza", "numi", "arizona", "arnold palmer", "life savers", "lifesavers"]
                for brand in brand_list:
                    if brand in q_text and brand not in res_lower:
                        is_trusted = False
                        rejection_reason = f"Brand '{brand.capitalize()}' is in product query but missing from search result."
                        confidence = 0.95
                        break

                # 2. Strong mismatch check: Format (Bags vs Bottles)
                if is_trusted:
                    is_query_liquid = any(w in q_text for w in ["tea", "coffee", "beverage", "water", "juice"]) and not any(w in q_text for w in ["bag", "bags", "powder", "mix", "sachet"])
                    is_result_bag_or_mix = any(w in res_lower for w in ["bag", "bags", "sachet", "mix", "powder", "loose", "canes", "cane"])
                    if is_query_liquid and is_result_bag_or_mix:
                        is_trusted = False
                        rejection_reason = "Product is liquid beverage but search result is tea bags, mix, or candy canes."
                        confidence = 0.9

                # 3. Sweetener / Formula mismatch: Lite/Diet vs Regular
                if is_trusted:
                    query_is_lite = any(w in q_text for w in ["lite", "diet", "zero", "unswet", "unsweet", "unsweetened", "sugar free"])
                    result_is_lite = any(w in res_lower for w in ["lite", "diet", "zero", "unswet", "unsweet", "unsweetened", "sugar free", "sucralose", "aspartame", "stevia"])
                    if query_is_lite != result_is_lite:
                        # Allow "unswet" to match unsweetened, but reject if one is lite and other is regular sugar
                        # If query is unsweetened and result is regular (sweet/sugar), reject.
                        if "unswet" in q_text or "unsweet" in q_text:
                            if "sweetened" in res_lower and "unsweetened" not in res_lower:
                                is_trusted = False
                                rejection_reason = "Product is Unsweetened but search result is sweetened."
                                confidence = 0.85
                        else:
                            is_trusted = False
                            rejection_reason = "Mismatch in Sweetener formula (Lite/Diet/Unsweetened vs Regular)."
                            confidence = 0.85

                # 4. Alcohol / Beer check: Ale vs Pilsener / Lager
                if is_trusted:
                    if "ale" in q_text and not "ale" in res_lower:
                        if "pilsener" in res_lower or "pilsner" in res_lower or "lager" in res_lower:
                            is_trusted = False
                            rejection_reason = "Product is Ale but search result is Pilsener/Lager."
                            confidence = 0.95

                # 5. Format check: Wipes vs Foam combo
                if is_trusted:
                    if "wipes" in q_text and "wipes" in res_lower:
                        # Check if result is a combo pack with foam
                        if "foam" in res_lower and not "foam" in q_text:
                            is_trusted = False
                            rejection_reason = "Product is only Wipes, but search result is a Wipes & Foam combo pack."
                            confidence = 0.9

                # 6. Basic token overlap threshold (at least 20% overlap of query tokens)
                if is_trusted:
                    # Overlap of words (excluding size keywords)
                    overlap = q_tokens.intersection(res_tokens)
                    if not overlap and len(q_tokens) > 0:
                        is_trusted = False
                        rejection_reason = "No overlapping product keywords found between query and search result."
                        confidence = 0.8
                    elif len(overlap) / len(q_tokens) < 0.2:
                        is_trusted = False
                        rejection_reason = f"Keyword overlap is too low ({len(overlap)}/{len(q_tokens)} words overlap)."
                        confidence = 0.7

            if is_trusted:
                predictions.append(idx_int)
                explanation = f"Matched key brand and product attributes. Overlapping terms: {list(q_tokens.intersection(res_tokens))}"
            else:
                explanation = rejection_reason if rejection_reason else "Failed validation check."

            detailed_results.append({
                "index": idx_int,
                "is_trusted": is_trusted,
                "confidence": confidence,
                "explanation": explanation
            })

        global_reasoning = f"Heuristic analysis completed. Identified generic query status: {is_generic}."
        return predictions, {"results": detailed_results, "reasoning": global_reasoning}


# --- OpenAI LLM Predictor (SOTA LLM Pipeline) ---
import threading

class OpenAILLMEvaluator:
    """
    Evaluator that leverages OpenAI API with Structured Outputs to parse search results.
    """
    def __init__(self, api_key: str = None, model: str = "gpt-4o-mini", system_prompt: str = None):
        self.api_key = api_key or os.environ.get("OPENAI_API_KEY")
        self.model = model
        self.system_prompt = system_prompt
        self.client = None
        self.token_usage = {"input": 0, "output": 0}
        self.usage_lock = threading.Lock()
        
        if self.api_key:
            self.client = OpenAI(api_key=self.api_key)

    def evaluate_product(self, product_title: str, product_description: str, search_results: Dict[str, str]) -> Tuple[List[int], Dict[str, Any]]:
        if not self.client:
            raise ValueError("OpenAI client not initialized. Please provide an API key or set OPENAI_API_KEY environment variable.")

        # Structure search results for the prompt
        formatted_results = ""
        for idx, text in search_results.items():
            formatted_results += f"Search Result ID: {idx}\n{text}\n\n"

        user_content = f"""PRODUCT TO EVALUATE:
Title: {product_title}
Description: {product_description}

SEARCH RESULTS TO EVALUATE:
{formatted_results}
"""

        try:
            # Call OpenAI Chat Completion with Structured Outputs
            response = self.client.beta.chat.completions.parse(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": user_content}
                ],
                response_format=ProductEvaluationResponse,
                temperature=0.0 # Force deterministic output
            )

            # Track tokens
            usage = response.usage
            if usage:
                with self.usage_lock:
                    self.token_usage["input"] += usage.prompt_tokens
                    self.token_usage["output"] += usage.completion_tokens

            # Parse structured results
            parsed_data = response.choices[0].message.parsed
            
            predictions = []
            detailed_results = []
            for item in parsed_data.results:
                if item.is_trusted:
                    predictions.append(item.index)
                detailed_results.append({
                    "index": item.index,
                    "is_trusted": item.is_trusted,
                    "confidence": item.confidence,
                    "explanation": item.explanation
                })

            metadata = {
                "results": detailed_results,
                "reasoning": parsed_data.reasoning
            }
            return predictions, metadata

        except Exception as e:
            # Handle API errors or connection errors gracefully
            print(f"Error calling OpenAI API: {e}")
            # Return empty predictions and the error in explanation
            predictions = []
            detailed_results = [{"index": int(idx), "is_trusted": False, "confidence": 0.0, "explanation": f"API Error: {str(e)}"} for idx in search_results.keys()]
            return predictions, {"results": detailed_results, "reasoning": f"Failed with API Error: {str(e)}"}
