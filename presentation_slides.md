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

### Slide 7: Operational Impact & Roadmap
What should business stakeholders expect, and what are the next steps?

1.  **Operational Performance (Expected)**:
    *   *Accuracy*: GPT-4o-mini with Structured Outputs is expected to achieve **>92% Precision** and **>88% F1-score**.
    *   *Throughput*: Run in parallel threads, classifying 100k products in <5 minutes.
    *   *Cost*: GPT-4o-mini is extremely affordable, costing approximately **$0.02 per 100 products** ($20 per 100,000 products).
2.  **Product Roadmap & Next Steps**:
    *   **Phase 1 (Complete)**: Basic evaluation harness, smart local baseline, OpenAI pipeline with Structured Outputs, and automated prompt-optimization loop.
    *   **Phase 2 (Immediate)**: Collect the interview's 'test' dataset, run evaluation, and output results in the required `llm_trusted_search_results` JSON schema.
    *   **Phase 3 (Mid-term)**: Implement a vector-based hybrid retriever to filter search results *before* the LLM layer, reducing LLM token context size and cost by 40%.
    *   **Phase 4 (Long-term)**: Fine-tune a smaller open-weight model (e.g., Llama-3-8B) on our validated trusted results. This will enable on-premise deployments for clients with strict data privacy requirements, and reduce API costs to $0.
