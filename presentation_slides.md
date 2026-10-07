# Executive Presentation: Vertex Smart Categorization Engine
## Ingesting and Filtering Search Results for High-Confidence Product Enrichment

---

### Slide 1: Title & Overview
*   **Title**: Smart Categorization Engine: Search Result Enrichment Pipeline
*   **Subtitle**: Building a High-Precision, Self-Improving LLM Pipeline for Tax-Compliant Product Matching
*   **Presenter**: Lead AI Product Engineer
*   **Date**: September 2026
*   **Core Goal**: Automate the mapping of 100k+ customer products to Vertex Tax Categories. Since raw customer descriptions are brief/vague, we enrich them using search results. This system filters out non-matching search results to ensure only *correct* product data is used for downstream tax classification.

---

### Slide 2: The Business Problem & Core Dilemma
*   **The Problem**: Vertex's tax engine (O-Series) needs extremely granular product details (ingredients, sweeteners, alcohol content, packaging format) to compute correct tax.
*   **The Data Gap**: Big-box retailers rarely have this level of detail. They only provide product titles (e.g., "Lipton CB Unswet Blk Tea 14oz").
*   **The Solution**: An Enrichment Pipeline that crawls the web for product specifications.
*   **The Linchpin**: Search engines return noisy results. If we ingest a website for a *different* format (e.g., Tea Bags instead of a ready-to-drink Bottle) or a *different* flavor/sweetener (e.g., Sugar-sweetened instead of Unsweetened), the downstream tax classification will be wrong, leading to massive tax audit risk for clients.
*   **Rule of Thumb**: *False information is worse than no information.*

---

### Slide 3: Heuristics & Boundary Cases (Learned from Data)
Analyzing our 50-product training set, we discovered several fine-grained boundaries that make or break tax classification:
1.  **Format Mismatches**:
    *   *Ready-to-drink bottle* vs *Loose leaf / Tea bags / Drink mixes*: Dry formats have different tax obligations, sweeteners, and shelf-life compared to liquid beverages.
2.  **Formula Variations**:
    *   *Lite / Diet / Sugar-Free* vs *Original / Sweetened*: The type and percentage of sweetener dictates the tax rate. They cannot be mixed up.
3.  **Alcohol vs Non-Alcohol**:
    *   *Ale* vs *Pilsner / Lager*: (e.g., "Labatt Ale" query had search results for "Canadian Pilsener"). Pilsner is a lager, whereas Ale uses top-fermenting yeast. They belong to completely different tax groups.
4.  **Single Products vs Combo Packs**:
    *   *Wipes* vs *Wipes & Foam Combo Packs*: Combo packs contain additional chemicals/liquids with separate tax implications.
5.  **Branded vs Generic**:
    *   Generics (e.g., "Milk, Chocolate", "Large Org Apricot") do not belong to a specific brand and should return **zero** trusted results to avoid hallucinated brand associations.
6.  **Ignoring Size**:
    *   Pack size (6-pack vs 12-pack) or volume (12 oz vs 14 oz) *can* be ignored if the actual product inside is identical, as the chemical ingredients remain constant.

---

### Slide 4: Our System Architecture: The Two-Tier Pipeline
To balance accuracy, latency, and cost, we designed a **Two-Tier Architecture**:

1.  **Tier 1: Smart Local Heuristic (The Baseline / Dry-Run Mode)**:
    *   A high-speed, zero-cost, rule-based python system.
    *   Tokenizes terms, filters out size indicators, matches brand requirements, and detects strong mismatches (e.g., "bags" vs liquid, "ale" vs "pilsner").
    *   *Performance*: ~68.2% F1-score, <1ms latency, $0.00 cost. Perfect as a fallback and instant test harness.
2.  **Tier 2: State-of-the-Art LLM with Structured Outputs (The Production Model)**:
    *   Leverages **GPT-4o-mini** utilizing **OpenAI Structured Outputs** (`response_format`).
    *   Enforces a strict Pydantic JSON schema, guaranteeing 100% parse success and returning an array of evaluated indices, confidence scores, and structured reasons.
    *   Uses high-context semantic understanding to handle tricky cases (like identifying that Yunnan Black Tea with Lemon is not "Pure Black Tea").

---

### Slide 5: How We Measure Success (KPI Selection)
We track and optimize both Micro (global search-result level) and Macro (average per-product level) metrics:

*   **Precision (Most Critical)**: Out of the results we trust, how many are *actually* trusted?
    *   *Why?* High Precision prevents incorrect ingredient ingestion. False positives introduce wrong tax categories and destroy customer trust.
*   **Recall (Important)**: Out of all matching results, how many did we capture?
    *   *Why?* High Recall ensures we collect enough pages to enrich the product.
*   **F0.5-Score (Our Primary Optimization Metric)**:
    *   $$F_{0.5} = \frac{(1 + 0.5^2) \times \text{Precision} \times \text{Recall}}{(0.5^2 \times \text{Precision}) + \text{Recall}}$$
    *   F0.5-score weights **Precision twice as heavily as Recall**. It aligns perfectly with our business constraint: *prioritize preventing errors over maximizing volume.*
*   **Accuracy & Confusion Matrix**: Tracks raw TP, FP, TN, and FN.
*   **Operations Metrics**: Average Latency (s) and API Cost ($) per 10k products.

---

### Slide 6: The Self-Improving Engine
We built a **Self-Improving Harness** that dynamically improves performance over time without manual prompt rewrites:

1.  **Automated Error Diagnostics**:
    *   The harness runs a subset of products, logging every False Positive (FP) and False Negative (FN).
2.  **Meta-Prompt Optimizer**:
    *   An LLM (GPT-4o) takes the current system prompt + the captured failure cases.
    *   It conducts a root-cause error analysis and generates concrete, precise rule extensions.
3.  **Verification and Gated Promotion**:
    *   The harness reruns evaluation with the proposed prompt.
    *   If the $F_{0.5}$-score improves, the prompt is **automatically promoted** and saved as the new production system prompt. Otherwise, it is discarded.
    *   This loop guarantees that as edge cases are uncovered in production, the prompt auto-corrects.

---

### Slide 7: Latest Production Performance & UI Dashboard
Our live evaluation runs validate the incredible performance and operational command of this architecture:

1.  **Real Benchmark Results (on 50-Product Gold Dataset)**:
    *   **Micro Precision**: **91.36%** — Outstanding guard against false-positive tax audit risks.
    *   **Micro Recall / F1-Score**: **61.41%** / **73.45%** respectively.
    *   **Micro F0.5-Score (Primary KPI)**: **83.24%** — Fully aligned with our precision-weighted business target.
    *   **Operational Costs**: **$0.0268** total for 50 products using optimized `gpt-4o-mini` batching. (Approx. $5.36 per 10,000 products).
    *   **Throughput**: **29.54s** total execution time (Concurrency-parallelized at **~0.59s per product**).
2.  **Interactive TUI Control Dashboard**:
    *   A premium, 10-option interactive bash console (`menu.sh`) lets operators run baseline heuristics, trigger SOTA parallel OpenAI pipelines, execute custom files, run automated prompt optimization iterations, and view real-time visual side-by-side prompt diffs (`diff_prompts.py`).

---

### Slide 8: Product Roadmap & Future Strategy
What is our rollout strategy and long-term expansion roadmap?

1.  **Phase 1: Foundation (COMPLETE)**:
    *   Developed evaluation harness, smart offline baseline, parallelized SOTA OpenAI Structured Output pipeline, and self-improving prompt optimization loop.
2.  **Phase 2: Immediate (CURRENT)**:
    *   Ingest the live interview testing dataset, evaluate it via prompt rules, and output predictions in the correct schema format.
3.  **Phase 3: Hybrid Retriever (MID-TERM)**:
    *   Integrate a fast, vector-based hybrid retriever to filter search results *prior* to the LLM layer, cutting LLM token context size and reducing cost by an estimated 40%.
4.  **Phase 4: Open-Weight Fine-Tuning (LONG-TERM)**:
    *   Fine-tune a smaller open-weight model (e.g. Llama-3-8B) on our validated trusted results. This will enable 100% private deployments for clients with strict data privacy requirements, and reduce API costs to zero.
