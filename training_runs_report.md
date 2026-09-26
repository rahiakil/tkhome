# 📊 Vertex Smart Categorization: Detailed Training Run Report

This report contains the **detailed results and reasoning** for all **50 products** evaluated on the training dataset using our SOTA **GPT-4o-mini with Structured Outputs** pipeline.

## 📈 Pipeline Performance Summary
| Metric | Value | Business Impact |
| :--- | :--- | :--- |
| **Precision** | **89.25%** | Prevents ingestion of false product data (avoiding audit risk) |
| **Recall** | **69.17%** | Captures useful sources for robust product enrichment |
| **F0.5-Score** | **84.35%** | Core KPI: Weights Precision twice as heavily as Recall |
| **Total Products** | **50** | Full validation subset |
| **Total Search Results** | **455** | Evaluated search items |
| **API Cost** | **$0.0286** | Incredibly cost-efficient (~$0.00057 per product) |

---

## 🔍 Individual Product Run Analyses

Click on any product below to expand its search result evaluations, predictions, and detailed LLM reasoning.

### 1. ✅ Dunkin Donuts Mocha 13.7zBtl
<details>
<summary><b>View Evaluation (TP: 5 | FP: 0 | FN: 0)</b></summary>

**Description:** *(None provided)*

**Ground Truth Trusted IDs:** `[1, 2, 3, 4, 5]`  
**LLM Predicted Trusted IDs:** `[1, 2, 3, 4, 5]`  

💡 **Global Pipeline Reasoning:** All search results are for Dunkin' Mocha Iced Coffee in a 13.7 oz bottle format, which matches the product being evaluated. They all represent the same brand and product type, ensuring consistency in ingredients and tax obligations.

| ID | Ground Truth | Prediction | Confidence | Decision Reasoning |
| :--- | :---: | :---: | :---: | :--- |
| 1 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result is for Dunkin' Mocha Iced Coffee in a 13.7 oz bottle, matching the brand and product format exactly, despite being a 12-pack. |
| 2 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result is for Dunkin Mocha Iced Coffee in a 13.7 oz bottle, matching the brand and product format exactly. |
| 3 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result is for Dunkin Donuts Iced Coffee Beverage Mocha in a 13.7 oz bottle, matching the brand and product format exactly. |
| 4 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result is for Dunkin' Mocha Iced Coffee & Milk Beverage in a 13.7 fl oz bottle, matching the brand and product format exactly. |
| 5 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result is for Dunkin' Mocha Iced Coffee Bottle, matching the brand and product format exactly. |

</details>

### 2. ✅ 
<details>
<summary><b>View Evaluation (TP: 0 | FP: 0 | FN: 0)</b></summary>

**Description:** *Milk, Chocolate*

**Ground Truth Trusted IDs:** `[]`  
**LLM Predicted Trusted IDs:** `[]`  

💡 **Global Pipeline Reasoning:** All search results are either generic descriptions of milk chocolate or refer to cake recipes, none of which match the specific product of ready-to-drink chocolate milk. There are no trusted results as they do not represent a specific brand or product format.

| ID | Ground Truth | Prediction | Confidence | Decision Reasoning |
| :--- | :---: | :---: | :---: | :--- |
| 1 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result discusses the ingredients of milk chocolate but does not represent a specific product; it is generic and does not match the brand or format of a ready-to-drink milk product. |
| 2 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is a general description of milk chocolate and does not refer to a specific product; it is not a branded item and does not match the format of a ready-to-drink milk. |
| 3 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is about a milk chocolate layer cake, which is a different product format (cake) and does not match the queried product of chocolate milk. |
| 4 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is about a milk chocolate cake, which is also a different product format (cake) and does not match the queried product of chocolate milk. |
| 5 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is a recipe for chocolate cake, which is unrelated to the queried product of chocolate milk and represents a different product format. |

</details>

### 3. ⚠️ Arnold Palmer Half & Half Iced Tea Lemonade 6 ea
<details>
<summary><b>View Evaluation (TP: 0 | FP: 0 | FN: 3)</b></summary>

**Description:** *Iced Tea Lemonade, Half & Half*

**Ground Truth Trusted IDs:** `[9, 6, 7]`  
**LLM Predicted Trusted IDs:** `[]`  

💡 **Global Pipeline Reasoning:** All search results either refer to a 'Lite' version, a spiked version, or a different format (like a mix or instant tea), which do not match the original product of Arnold Palmer Half & Half Iced Tea Lemonade.

| ID | Ground Truth | Prediction | Confidence | Decision Reasoning |
| :--- | :---: | :---: | :---: | :--- |
| 1 | 🔴 Rejected | 🔴 Rejected | 0.80 | This result is for 'Lite' version of Arnold Palmer, which is not the same as the original product queried. |
| 2 | 🔴 Rejected | 🔴 Rejected | 0.80 | This result is also for the 'Lite' version of Arnold Palmer, which does not match the original product. |
| 3 | 🔴 Rejected | 🔴 Rejected | 0.80 | This result is for the 'Lite' version of Arnold Palmer, which is not the same as the original product queried. |
| 4 | 🔴 Rejected | 🔴 Rejected | 0.80 | This result does not specify 'Lite', but it is still a different product format (not the original queried product). |
| 5 | 🔴 Rejected | 🔴 Rejected | 0.80 | This result is for a powdered mix version of Arnold Palmer, which is not the same as the ready-to-drink product queried. |
| 6 | 🟢 Trusted | ❌ 🔴 Rejected | 0.80 | This result is for the 'Original' version, but it is a spiked version, which is not the same as the non-alcoholic product queried. |
| 7 | 🟢 Trusted | ❌ 🔴 Rejected | 0.80 | This result is for the 'Original' version, but it is a spiked version, which is not the same as the non-alcoholic product queried. |
| 8 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is a recipe and not a product for sale, thus it cannot be trusted. |
| 9 | 🟢 Trusted | ❌ 🔴 Rejected | 0.80 | This result is for a different product format (instant tea) and does not match the original product. |

</details>

### 4. ⚠️ capri sun paw patrol mango pineapple juice blend 10 ea
<details>
<summary><b>View Evaluation (TP: 8 | FP: 0 | FN: 2)</b></summary>

**Description:** *(None provided)*

**Ground Truth Trusted IDs:** `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`  
**LLM Predicted Trusted IDs:** `[1, 2, 4, 5, 7, 8, 9, 10]`  

💡 **Global Pipeline Reasoning:** All trusted results match the exact product title and description, including the brand 'Capri Sun', the flavor 'Mango Pineapple', and the Paw Patrol branding. Non-trusted results either indicate a flavored variant or a different packaging format.

| ID | Ground Truth | Prediction | Confidence | Decision Reasoning |
| :--- | :---: | :---: | :---: | :--- |
| 1 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the exact product title and description, including the brand 'Capri Sun', the flavor 'Mango Pineapple', and the Paw Patrol branding. |
| 2 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result is identical to the product being queried, matching the brand, flavor, and Paw Patrol branding. |
| 3 | 🟢 Trusted | ❌ 🔴 Rejected | 0.00 | This result mentions 'Flavored' which indicates it is not the same as the '100% Juice' product being queried. |
| 4 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result is a direct match to the product title and description, confirming the brand and flavor. |
| 5 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the product title and description exactly, including the brand and flavor. |
| 6 | 🟢 Trusted | ❌ 🔴 Rejected | 0.00 | This result specifies '6 fl oz' which indicates a different packaging format, even though the product is similar. |
| 7 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the product title and description, confirming the brand and flavor. |
| 8 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result is identical to the product being queried, matching the brand, flavor, and Paw Patrol branding. |
| 9 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the product title and description, confirming the brand and flavor. |
| 10 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the product title and description, confirming the brand and flavor. |

</details>

### 5. ⚠️ Theraworx Protect For Daily Urinary Health Wipes 60 ea
<details>
<summary><b>View Evaluation (TP: 3 | FP: 0 | FN: 1)</b></summary>

**Description:** *Wipes, Protect, For Daily Urinary Health*

**Ground Truth Trusted IDs:** `[1, 10, 3, 7]`  
**LLM Predicted Trusted IDs:** `[1, 10, 7]`  

💡 **Global Pipeline Reasoning:** The trusted results (1, 7, and 10) are all for the exact product 'Theraworx Protect For Daily Urinary Health Wipes 60 ea', while the other results are for combo packs that include foam or other products, which do not match the single wipes format required.

| ID | Ground Truth | Prediction | Confidence | Decision Reasoning |
| :--- | :---: | :---: | :---: | :--- |
| 1 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the exact product title and description, confirming it is the same brand and format (wipes) as the queried product. |
| 2 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is for a combo pack that includes both wipes and foam, which does not match the single product format of the queried item. |
| 3 | 🟢 Trusted | ❌ 🔴 Rejected | 0.00 | This result is also for a combo pack (U-Pak) and does not represent the single wipes product being queried. |
| 4 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result does not specify the product format as wipes only and may include other products, thus it cannot be trusted. |
| 5 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is for a U-Pak that includes both wipes and foam, which does not match the single product format of the queried item. |
| 6 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is for a U-Pak that includes both wipes and foam, which does not match the single product format of the queried item. |
| 7 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the exact product title and description, confirming it is the same brand and format (wipes) as the queried product. |
| 8 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is for a U-Pak that includes both wipes and foam, which does not match the single product format of the queried item. |
| 9 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is for a U-Pak that includes both wipes and foam, which does not match the single product format of the queried item. |
| 10 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the exact product title and description, confirming it is the same brand and format (wipes) as the queried product. |

</details>

### 6. ⚠️ Ghirardeli Squares White Chocolate Caramel 5 oz
<details>
<summary><b>View Evaluation (TP: 2 | FP: 1 | FN: 2)</b></summary>

**Description:** *White Chocolate, Squares, Caramel*

**Ground Truth Trusted IDs:** `[1, 2, 3, 5]`  
**LLM Predicted Trusted IDs:** `[2, 4, 5]`  

💡 **Global Pipeline Reasoning:** The trusted results must match the brand, product format, and flavor exactly. Results for different flavors (like sugar cookie) or different packaging formats (like case packs) are not trusted. The results that matched the exact product description were those that specified 'Ghirardelli White Chocolate Squares with Caramel Filling' and the 5 oz size.

| ID | Ground Truth | Prediction | Confidence | Decision Reasoning |
| :--- | :---: | :---: | :---: | :--- |
| 1 | 🟢 Trusted | ❌ 🔴 Rejected | 0.00 | This result refers to 'Medium Bags' which indicates a different packaging format and is not the exact product being queried. |
| 2 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the brand, product format, and flavor exactly as it is Ghirardelli White Chocolate Squares with Caramel Filling, 5 oz. |
| 3 | 🟢 Trusted | ❌ 🔴 Rejected | 0.00 | This result is for a 'Case Pack' which indicates a different packaging format and is not the exact product being queried. |
| 4 | 🔴 Rejected | ❌ 🟢 Trusted | 1.00 | This result matches the brand and product description exactly as it is Ghirardelli White Chocolate Caramel Chocolate Candy, 5 oz. |
| 5 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the brand and product description exactly as it is Ghirardelli White Chocolate Squares with Caramel Filling, 5 oz. |
| 6 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is for 'White Chocolate Sugar Cookie SQUARES' which is a different flavor and not the exact product being queried. |
| 7 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is for 'White Chocolate Sugar Cookie Squares' which is a different flavor and not the exact product being queried. |
| 8 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is for 'White Chocolate Sugar Cookie Squares' which is a different flavor and not the exact product being queried. |
| 9 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is for 'Milk Chocolate Caramel Waffle Cone' which is a different product and not the exact product being queried. |
| 10 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is for 'White Chocolate Sugar Cookie Candy Squares' which is a different flavor and not the exact product being queried. |

</details>

### 7. ⚠️ BRK STRAWBERRY DRINKING WATER   15/10 OZ
<details>
<summary><b>View Evaluation (TP: 3 | FP: 0 | FN: 2)</b></summary>

**Description:** *(None provided)*

**Ground Truth Trusted IDs:** `[1, 3, 6, 7, 8]`  
**LLM Predicted Trusted IDs:** `[8, 3, 7]`  

💡 **Global Pipeline Reasoning:** The trusted results must match the brand 'Brookshire's' and the product type 'Water Beverage, Strawberry'. Results that are from different brands or are combo packs were rejected. The size differences were ignored as the product inside is identical.

| ID | Ground Truth | Prediction | Confidence | Decision Reasoning |
| :--- | :---: | :---: | :---: | :--- |
| 1 | 🟢 Trusted | ❌ 🔴 Rejected | 0.80 | This result is for a 'Brookshire's Water Beverage, Strawberry, 15 Pack', which is a combo pack and not the single product queried. |
| 2 | 🔴 Rejected | 🔴 Rejected | 0.90 | This result is for 'Kroger® Strawberry Flavored Bottled Water', which is a different brand and therefore not trusted. |
| 3 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result is for 'Brookshire's Water Beverage, Strawberry', which matches the brand and product format exactly. |
| 4 | 🔴 Rejected | 🔴 Rejected | 0.70 | This result is for 'Fruit Splash Juniors Water Beverage, Strawberry', which is a different brand and product. |
| 5 | 🔴 Rejected | 🔴 Rejected | 0.60 | This result is for a 'Strawberry Rhubarb' flavored beverage, which is a different flavor and product type. |
| 6 | 🟢 Trusted | ❌ 🔴 Rejected | 0.80 | This result is a repeat of the first search result for a 'Brookshire's Water Beverage, Strawberry, 15 Pack', which is a combo pack. |
| 7 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result is for 'Brookshire's Water Beverage, Strawberry', which matches the brand and product format exactly. |
| 8 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result is for 'Brookshire's Strawberry Water Beverage (10 oz x 15 ct)', which matches the brand and product format, despite the packaging size. |
| 9 | 🔴 Rejected | 🔴 Rejected | 0.70 | This result is for 'Fruit Splash Juniors Water Beverage, Strawberry', which is a different brand and product. |
| 10 | 🔴 Rejected | 🔴 Rejected | 0.50 | This result is for 'Best Choice Drinking Water 10 Oz 15 Pack', which is a different brand and product. |

</details>

### 8. ✅ Lipton CB Unswet Blk Tea 14oz
<details>
<summary><b>View Evaluation (TP: 0 | FP: 0 | FN: 0)</b></summary>

**Description:** *(None provided)*

**Ground Truth Trusted IDs:** `[]`  
**LLM Predicted Trusted IDs:** `[]`  

💡 **Global Pipeline Reasoning:** All search results are for tea bags, mixes, or different product lines that do not match the liquid ready-to-drink format of the queried Lipton CB Unswet Blk Tea. None of the results match the exact product in terms of format, flavor, or brand identity.

| ID | Ground Truth | Prediction | Confidence | Decision Reasoning |
| :--- | :---: | :---: | :---: | :--- |
| 1 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is for Lipton Iced Tea Bags, which is a different format (tea bags) compared to the queried product (liquid ready-to-drink). |
| 2 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is for Lipton Unsweetened Black Iced Tea in a case of tea bags, which is not the same as the liquid ready-to-drink format of the queried product. |
| 3 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is for Cold Brew Iced Black Tea in tea bags, which is a different format than the liquid ready-to-drink product being queried. |
| 4 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is for Lipton Black Tea Cold Brew Iced Tea Bags, which is not the same as the liquid ready-to-drink format of the queried product. |
| 5 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is for Lipton Sweet Tea, which contains sugar and is not the same as the unsweetened version queried. |
| 6 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is for Lipton Black Unsweetened Iced Tea Bags, which is a different format (tea bags) compared to the liquid ready-to-drink product. |
| 7 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is for Lipton Unsweetened Iced Tea Mix, which is a powdered mix and not the same as the liquid ready-to-drink product. |
| 8 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is a general page about various Lipton teas and does not specify the exact product being queried. |
| 9 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is a duplicate of search result ID 2, which is for tea bags and not the liquid product. |
| 10 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is for Lipton Pure Leaf Unsweetened Iced Black Tea, which is a different product line and not the same as the queried Lipton CB Unswet Blk Tea. |

</details>

### 9. ⚠️ FC
<details>
<summary><b>View Evaluation (TP: 0 | FP: 2 | FN: 0)</b></summary>

**Description:** *(None provided)*

**Ground Truth Trusted IDs:** `[]`  
**LLM Predicted Trusted IDs:** `[2, 3]`  

💡 **Global Pipeline Reasoning:** The first search result is unrelated to a game or sports product, focusing instead on the FC Barcelona team. The second and third results are both video games under the EA SPORTS FC brand, which aligns with the product context of 'FC'.

| ID | Ground Truth | Prediction | Confidence | Decision Reasoning |
| :--- | :---: | :---: | :---: | :--- |
| 1 | 🔴 Rejected | 🔴 Rejected | 0.00 | The search result is for the official website of FC Barcelona, which is not the same product as 'FC' and does not match the context of a game or sports product. |
| 2 | 🔴 Rejected | ❌ 🟢 Trusted | 1.00 | This result is for EA SPORTS FC™ 25, which matches the product context of 'FC' as a video game related to football. |
| 3 | 🔴 Rejected | ❌ 🟢 Trusted | 1.00 | This result is for EA SPORTS FC™ 24, which also matches the product context of 'FC' as a video game related to football. |

</details>

### 10. ⚠️ Muscle Milk Banana Creme 14oz
<details>
<summary><b>View Evaluation (TP: 3 | FP: 1 | FN: 1)</b></summary>

**Description:** *(None provided)*

**Ground Truth Trusted IDs:** `[8, 1, 2, 4]`  
**LLM Predicted Trusted IDs:** `[8, 1, 2, 6]`  

💡 **Global Pipeline Reasoning:** The trusted results must match the brand 'Muscle Milk', the flavor 'Banana Creme', and the format of 14 oz liquid. Variations such as 'Zero Sugar' or 'Non-Dairy' are not trusted as they represent different formulations. Additionally, protein powders are not the same as ready-to-drink shakes.

| ID | Ground Truth | Prediction | Confidence | Decision Reasoning |
| :--- | :---: | :---: | :---: | :--- |
| 1 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result matches the brand 'Muscle Milk' and the flavor 'Banana Creme' in a 14 oz format, making it a trusted match. |
| 2 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result is from the same brand 'Muscle Milk', has the same flavor 'Banana Creme', and is in the same 14 fl oz format, thus it is trusted. |
| 3 | 🔴 Rejected | 🔴 Rejected | 0.40 | This result is for a 'Zero Sugar' version, which is a different formula than the original 'Muscle Milk Banana Creme', making it untrusted. |
| 4 | 🟢 Trusted | ❌ 🔴 Rejected | 0.30 | This result does not specify a format (liquid vs powder) and lacks brand context, making it untrusted. |
| 5 | 🔴 Rejected | 🔴 Rejected | 0.20 | This result is for a protein powder, which is a different format than the liquid shake being queried, thus it is untrusted. |
| 6 | 🔴 Rejected | ❌ 🟢 Trusted | 0.90 | This result matches the brand 'Muscle Milk', the flavor 'Banana Crème', and the 14 fl oz format, making it a trusted match. |
| 7 | 🔴 Rejected | 🔴 Rejected | 0.30 | This result is for a 'Non-Dairy' version, which is a different formulation than the original 'Muscle Milk Banana Creme', making it untrusted. |
| 8 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result matches the brand 'Muscle Milk', the flavor 'Banana Creme', and the 14 fl oz format, thus it is trusted. |
| 9 | 🔴 Rejected | 🔴 Rejected | 0.40 | This result is for a 'Zero Sugar' version, which is a different formula than the original 'Muscle Milk Banana Creme', making it untrusted. |
| 10 | 🔴 Rejected | 🔴 Rejected | 0.30 | This result is for a 'Non-Dairy' version, which is a different formulation than the original 'Muscle Milk Banana Creme', making it untrusted. |

</details>

### 11. ⚠️ LIFESAVERS MINTS WINTOGREEN SUP
<details>
<summary><b>View Evaluation (TP: 4 | FP: 0 | FN: 5)</b></summary>

**Description:** *(None provided)*

**Ground Truth Trusted IDs:** `[1, 2, 3, 4, 5, 6, 7, 8, 10]`  
**LLM Predicted Trusted IDs:** `[1, 2, 10, 5]`  

💡 **Global Pipeline Reasoning:** The evaluations focused on matching the brand 'Lifesavers' and the specific flavor 'Wint-O-Green'. Results that presented different formats (like rolls or candy canes) were rejected. Size differences were ignored as long as the product type and flavor matched.

| ID | Ground Truth | Prediction | Confidence | Decision Reasoning |
| :--- | :---: | :---: | :---: | :--- |
| 1 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result matches the brand 'Lifesavers' and the exact product 'Wint-O-Green Mints' in a similar format (bag). The size difference is ignored as the product inside is identical. |
| 2 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result is from the same brand 'Lifesavers' and refers to 'Wint-O-Green' mints, matching the flavor exactly. The format is consistent with mints. |
| 3 | 🟢 Trusted | ❌ 🔴 Rejected | 0.70 | While this result is from the same brand and flavor, it is a single roll format, which is a different product format compared to the queried product. |
| 4 | 🟢 Trusted | ❌ 🔴 Rejected | 0.50 | This result provides ingredient information but does not specify a product format or size, making it unclear if it matches the exact product. |
| 5 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result matches the brand 'Lifesavers' and the flavor 'Wint-O-Green', and is in a similar format (sharing size), which is acceptable. |
| 6 | 🟢 Trusted | ❌ 🔴 Rejected | 0.40 | This result is a repeat of a previous entry and does not provide a unique product that matches the queried item. |
| 7 | 🟢 Trusted | ❌ 🔴 Rejected | 0.40 | This result is a repeat of a previous entry and does not provide a unique product that matches the queried item. |
| 8 | 🟢 Trusted | ❌ 🔴 Rejected | 0.30 | This result refers to a bulk size of 'Wint-O-Green' mints, which is a different product format compared to the queried item. |
| 9 | 🔴 Rejected | 🔴 Rejected | 0.20 | This result refers to 'Candy Canes' which is a different product format and flavor, thus not matching the queried item. |
| 10 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result matches the brand 'Lifesavers' and the flavor 'Wint-O-Green', and is in a similar format (bag), making it a trusted result. |

</details>

### 12. ⚠️ Equate Bandages 10 ea
<details>
<summary><b>View Evaluation (TP: 3 | FP: 0 | FN: 6)</b></summary>

**Description:** *Bandages, Flexible Fabric, Antibacterial, Jumbo*

**Ground Truth Trusted IDs:** `[1, 2, 3, 5, 6, 7, 8, 9, 10]`  
**LLM Predicted Trusted IDs:** `[8, 1, 2]`  

💡 **Global Pipeline Reasoning:** The trusted results must match the brand 'Equate', the antibacterial feature, the flexible fabric format, and the count of 10. Results that deviate in size, count, or lack specific brand identification are not trusted.

| ID | Ground Truth | Prediction | Confidence | Decision Reasoning |
| :--- | :---: | :---: | :---: | :--- |
| 1 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the product title and description exactly, including the brand 'Equate', the antibacterial feature, and the flexible fabric format. |
| 2 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result is identical to the product being evaluated, matching the brand, antibacterial feature, flexible fabric, and count of 10. |
| 3 | 🟢 Trusted | ❌ 🔴 Rejected | 0.00 | This result specifies 'X-Large' bandages, which indicates a different size and potentially different product characteristics compared to the queried product. |
| 4 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is for a 100 count package, which is a different quantity than the 10 count specified in the query. |
| 5 | 🟢 Trusted | ❌ 🔴 Rejected | 0.00 | This result is too generic and does not specify the count or the exact features of the bandages, making it unreliable. |
| 6 | 🟢 Trusted | ❌ 🔴 Rejected | 0.00 | This result also specifies 'X-Large' bandages, which indicates a different size and potentially different product characteristics. |
| 7 | 🟢 Trusted | ❌ 🔴 Rejected | 0.00 | This result is for a 100 count package, which is a different quantity than the 10 count specified in the query. |
| 8 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the product title and description exactly, including the brand 'Equate', the antibacterial feature, and the flexible fabric format. |
| 9 | 🟢 Trusted | ❌ 🔴 Rejected | 0.00 | This result is too generic and does not specify the count or the exact features of the bandages, making it unreliable. |
| 10 | 🟢 Trusted | ❌ 🔴 Rejected | 0.00 | This result does not specify the brand 'Equate' and is too generic, making it unreliable. |

</details>

### 13. ✅ FM PEANUT BTR BUCKEYES
<details>
<summary><b>View Evaluation (TP: 0 | FP: 0 | FN: 0)</b></summary>

**Description:** *(None provided)*

**Ground Truth Trusted IDs:** `[]`  
**LLM Predicted Trusted IDs:** `[]`  

💡 **Global Pipeline Reasoning:** All search results are generic recipes for Buckeyes or variations thereof, lacking the specific brand identity of 'FM'. None of the results represent the exact product being queried.

| ID | Ground Truth | Prediction | Confidence | Decision Reasoning |
| :--- | :---: | :---: | :---: | :--- |
| 1 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is a generic recipe for Peanut Butter Buckeyes and does not match the specific brand identity of 'FM'. |
| 2 | 🔴 Rejected | 🔴 Rejected | 0.00 | This is another generic recipe for Buckeyes and does not represent the specific brand 'FM'. |
| 3 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is a generic recipe for Peanut Butter Buckeyes and lacks the brand identity of 'FM'. |
| 4 | 🔴 Rejected | 🔴 Rejected | 0.00 | This is a generic recipe for Peanut Butter Balls (Buckeyes) and does not match the brand 'FM'. |
| 5 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is for a Peanut Butter Buckeye Roulade, which is a different product format and does not match the original query. |
| 6 | 🔴 Rejected | 🔴 Rejected | 0.00 | This recipe features a variation of Buckeyes using natural peanut butter and maple syrup, differing from the original product. |
| 7 | 🔴 Rejected | 🔴 Rejected | 0.00 | This is a generic recipe for Peanut Butter Balls (Buckeyes) and does not represent the specific brand 'FM'. |
| 8 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is a generic recipe for Chocolate Covered Peanut Butter Balls and does not match the brand 'FM'. |

</details>

### 14. ⚠️ Monster Ultra PeachyKeen 12zCn
<details>
<summary><b>View Evaluation (TP: 3 | FP: 0 | FN: 1)</b></summary>

**Description:** *(None provided)*

**Ground Truth Trusted IDs:** `[1, 10, 5, 7]`  
**LLM Predicted Trusted IDs:** `[1, 10, 7]`  

💡 **Global Pipeline Reasoning:** The key differences observed are primarily due to the 'Zero Sugar' variants, which are not the same as the original product. Trusted results must match the exact product name and format, which is why only results 1, 7, and 10 are trusted.

| ID | Ground Truth | Prediction | Confidence | Decision Reasoning |
| :--- | :---: | :---: | :---: | :--- |
| 1 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result matches the brand and product name exactly, and it is a liquid ready-to-drink format, which aligns with the queried product. |
| 2 | 🔴 Rejected | 🔴 Rejected | 0.80 | This result is for a 'Zero Sugar' version, which is a different formula from the original product, thus it does not match the queried product. |
| 3 | 🔴 Rejected | 🔴 Rejected | 0.80 | This result is also for a 'Zero Sugar' version, which is not the same as the original product being queried. |
| 4 | 🔴 Rejected | 🔴 Rejected | 0.80 | Similar to previous results, this is a 'Zero Sugar' variant, which does not match the original product. |
| 5 | 🟢 Trusted | ❌ 🔴 Rejected | 0.70 | While it has the same name, this result emphasizes 'zero sugar', indicating it is not the original product. |
| 6 | 🔴 Rejected | 🔴 Rejected | 0.50 | This result is for a different product (Energy Juice Rio Punch), which is not related to the queried product. |
| 7 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result matches the brand and product name exactly, and it is a liquid ready-to-drink format, which aligns with the queried product. |
| 8 | 🔴 Rejected | 🔴 Rejected | 0.60 | This result is for a 'Zero Sugar' version, which is not the same as the original product being queried. |
| 9 | 🔴 Rejected | 🔴 Rejected | 0.80 | This result is for a 'Zero Sugar' variant, which does not match the original product. |
| 10 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result matches the brand and product name exactly, and it is a liquid ready-to-drink format, which aligns with the queried product. |

</details>

### 15. ⚠️ Q KOLA
<details>
<summary><b>View Evaluation (TP: 5 | FP: 0 | FN: 4)</b></summary>

**Description:** *(None provided)*

**Ground Truth Trusted IDs:** `[1, 2, 3, 4, 5, 6, 7, 9, 10]`  
**LLM Predicted Trusted IDs:** `[2, 3, 5, 9, 10]`  

💡 **Global Pipeline Reasoning:** The evaluations focused on ensuring the brand 'Q' was present in the results, as well as confirming that the product format and ingredients matched the original query for 'Q Kola'. Generic terms or variations in branding led to rejections, while exact matches were trusted.

| ID | Ground Truth | Prediction | Confidence | Decision Reasoning |
| :--- | :---: | :---: | :---: | :--- |
| 1 | 🟢 Trusted | ❌ 🔴 Rejected | 0.80 | This result is a generic 'Kola' and does not specify the brand 'Q', which is critical for trust. |
| 2 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result specifies 'Q Kola Drink' and matches the brand and product format exactly. |
| 3 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result is for 'Q Kola' and matches the brand and product description accurately. |
| 4 | 🟢 Trusted | ❌ 🔴 Rejected | 0.70 | This result is for 'Q Mixers Kola', which indicates a different branding focus and may not be the exact product queried. |
| 5 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result is for 'Q Kola by Joel McHale' and matches the brand and product description accurately. |
| 6 | 🟢 Trusted | ❌ 🔴 Rejected | 0.80 | This result is a repeat of the first search result and does not specify the brand 'Q', which is critical for trust. |
| 7 | 🟢 Trusted | ❌ 🔴 Rejected | 0.50 | This result does not specify a product but rather a general brand page, lacking specific product details. |
| 8 | 🔴 Rejected | 🔴 Rejected | 0.60 | This result refers to 'Spectacular Kola', which is a different product and not the exact 'Q Kola' queried. |
| 9 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result is for 'Q Drinks Q Kola 4 pack', matching the brand and product description accurately. |
| 10 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result is a repeat of the fifth search result and matches the brand and product description accurately. |

</details>

### 16. ⚠️ starbucks doubleshot mexican mocha energy coffee beverage 15 oz
<details>
<summary><b>View Evaluation (TP: 5 | FP: 3 | FN: 0)</b></summary>

**Description:** *energy coffee beverage, mexican mocha*

**Ground Truth Trusted IDs:** `[2, 3, 6, 7, 10]`  
**LLM Predicted Trusted IDs:** `[2, 3, 4, 5, 6, 7, 9, 10]`  

💡 **Global Pipeline Reasoning:** The search results were evaluated based on the exact match of the product title, flavor, and format. Results that did not match the 'Mexican Mocha' flavor or were for different product formats (like 'Mocha' without 'Mexican Mocha') were rejected. All trusted results confirmed the product as an energy coffee beverage with the specified flavor.

| ID | Ground Truth | Prediction | Confidence | Decision Reasoning |
| :--- | :---: | :---: | :---: | :--- |
| 1 | 🔴 Rejected | 🔴 Rejected | 0.80 | This result is for 'Starbucks Double Shot Mocha', which does not match the 'Mexican Mocha' flavor specified in the query. |
| 2 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the exact product title and description, including the 'Mexican Mocha' flavor and 'Energy Coffee Beverage' format. |
| 3 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result is for 'Starbucks Doubleshot Energy Mexican Mocha', which matches the product title and flavor exactly. |
| 4 | 🔴 Rejected | ❌ 🟢 Trusted | 1.00 | This result matches the product title and flavor, confirming it is the same 'Mexican Mocha' energy coffee beverage. |
| 5 | 🔴 Rejected | ❌ 🟢 Trusted | 1.00 | This result is for 'Starbucks Doubleshot Energy Beverage, Mexican Mocha', matching the product title and flavor exactly. |
| 6 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the product title and flavor, confirming it is the same 'Mexican Mocha' energy coffee beverage. |
| 7 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the product title and flavor, confirming it is the same 'Mexican Mocha' energy coffee beverage. |
| 8 | 🔴 Rejected | 🔴 Rejected | 0.70 | This result is for 'Starbucks Doubleshot Energy Drink Coffee Beverage, Mocha', which does not specify 'Mexican Mocha' and may refer to a different flavor. |
| 9 | 🔴 Rejected | ❌ 🟢 Trusted | 1.00 | This result matches the product title and flavor, confirming it is the same 'Mexican Mocha' energy coffee beverage. |
| 10 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the product title and flavor, confirming it is the same 'Mexican Mocha' energy coffee beverage. |

</details>

### 17. ⚠️ S SEL TEA GREEN DECAF
<details>
<summary><b>View Evaluation (TP: 0 | FP: 4 | FN: 0)</b></summary>

**Description:** *(None provided)*

**Ground Truth Trusted IDs:** `[]`  
**LLM Predicted Trusted IDs:** `[2, 3, 4, 7]`  

💡 **Global Pipeline Reasoning:** The trusted results must match the brand 'Celestial Seasonings' and the product type 'Decaf Green Tea'. Generic results or those from different brands are not trusted. The flavor and decaffeination status must also align with the original product.

| ID | Ground Truth | Prediction | Confidence | Decision Reasoning |
| :--- | :---: | :---: | :---: | :--- |
| 1 | 🔴 Rejected | 🔴 Rejected | 0.80 | The product is a generic 'Decaf Green Tea' and does not specify the brand, while the original product is specifically 'S SEL TEA GREEN DECAF'. |
| 2 | 🔴 Rejected | ❌ 🟢 Trusted | 0.90 | This result is from Celestial Seasonings, matching the brand, and is a decaffeinated green tea, which aligns with the product description. |
| 3 | 🔴 Rejected | ❌ 🟢 Trusted | 0.90 | This result is also from Celestial Seasonings and specifies 'Decaf Authentic Green Tea', matching the brand and decaffeinated format. |
| 4 | 🔴 Rejected | ❌ 🟢 Trusted | 0.90 | This result is from Celestial Seasonings and describes 'Decaf Green Tea', matching the brand and product type. |
| 5 | 🔴 Rejected | 🔴 Rejected | 0.70 | This result is for 'Decaf The People's Green Tea Bags', which is a different brand and product, thus not trusted. |
| 6 | 🔴 Rejected | 🔴 Rejected | 0.80 | This is a generic 'Decaf Green Tea' without a specific brand, which does not match the original product. |
| 7 | 🔴 Rejected | ❌ 🟢 Trusted | 0.90 | This result is a repeat of ID 2, confirming it is from Celestial Seasonings and matches the product type. |
| 8 | 🔴 Rejected | 🔴 Rejected | 0.70 | This result is for 'Decaf The People's Green Tea Bags', which is a different brand and product, thus not trusted. |
| 9 | 🔴 Rejected | 🔴 Rejected | 0.60 | This result is a generic listing for 'Decaf Green Tea' and does not specify a brand, making it untrusted. |
| 10 | 🔴 Rejected | 🔴 Rejected | 0.50 | This result discusses various decaf teas but does not pertain to the specific product being queried. |

</details>

### 18. ⚠️ SPARKLING ICE PEACH NECTARINE
<details>
<summary><b>View Evaluation (TP: 4 | FP: 1 | FN: 2)</b></summary>

**Description:** *(None provided)*

**Ground Truth Trusted IDs:** `[1, 2, 5, 6, 7, 9]`  
**LLM Predicted Trusted IDs:** `[2, 3, 6, 7, 9]`  

💡 **Global Pipeline Reasoning:** The trusted results must match the brand 'Sparkling Ice' and the flavor 'Peach Nectarine' exactly. Generic results without the brand are not trusted. Variations like 'Zero Sugar' are not trusted if not specified in the query.

| ID | Ground Truth | Prediction | Confidence | Decision Reasoning |
| :--- | :---: | :---: | :---: | :--- |
| 1 | 🟢 Trusted | ❌ 🔴 Rejected | 0.00 | This result is for a generic 'Peach Nectarine' without the 'Sparkling Ice' brand, thus it does not match the queried product. |
| 2 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result is for 'Sparkling Ice® Peach Nectarine Flavored', matching both the brand and the flavor exactly. |
| 3 | 🔴 Rejected | ❌ 🟢 Trusted | 1.00 | This result is for 'Sparkling Ice, Peach Nectarine Sparkling Water', matching the brand and flavor exactly. |
| 4 | 🔴 Rejected | 🔴 Rejected | 0.50 | This result is for 'Sparkling Ice® Peach Nectarine Sparkling Water, Zero Sugar', which introduces a 'Zero Sugar' variation not present in the query. |
| 5 | 🟢 Trusted | ❌ 🔴 Rejected | 0.00 | This result is for a generic 'Peach Nectarine' without the 'Sparkling Ice' brand, thus it does not match the queried product. |
| 6 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result is for 'Sparkling Ice, Peach Nectarine', matching the brand and flavor exactly. |
| 7 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result is for 'Sparkling Ice Peach Nectarine Flavored Water', matching the brand and flavor exactly. |
| 8 | 🔴 Rejected | 🔴 Rejected | 0.50 | This result is for 'Sparkling Ice® Peach Nectarine Sparkling Water, Zero Sugar', which introduces a 'Zero Sugar' variation not present in the query. |
| 9 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result is for 'Sparkling Ice® Peach Nectarine Flavored', matching both the brand and the flavor exactly. |

</details>

### 19. ✅ Labatt Ale 12 ea
<details>
<summary><b>View Evaluation (TP: 0 | FP: 0 | FN: 0)</b></summary>

**Description:** *(None provided)*

**Ground Truth Trusted IDs:** `[]`  
**LLM Predicted Trusted IDs:** `[]`  

💡 **Global Pipeline Reasoning:** All search results are for Labatt Canadian Pilsener, which is a different beer classification than Labatt Ale. Therefore, none of the results can be trusted as they do not match the queried product.

| ID | Ground Truth | Prediction | Confidence | Decision Reasoning |
| :--- | :---: | :---: | :---: | :--- |
| 1 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is for Labatt Canadian Pilsener, which is a different beer classification than Labatt Ale, thus it does not match the product being queried. |
| 2 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is for Labatt Canadian Pilsener, which is a different beer classification than Labatt Ale, thus it does not match the product being queried. |
| 3 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is for Labatt Canadian Pilsener, which is a different beer classification than Labatt Ale, thus it does not match the product being queried. |
| 4 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is for Labatt Canadian Pilsener, which is a different beer classification than Labatt Ale, thus it does not match the product being queried. |
| 5 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is for Labatt Canadian Pilsener, which is a different beer classification than Labatt Ale, thus it does not match the product being queried. |
| 6 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is a general company page and does not represent a specific product, thus it cannot be trusted. |
| 7 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is for Labatt Canadian Pilsener, which is a different beer classification than Labatt Ale, thus it does not match the product being queried. |
| 8 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is for Labatt Canadian Pilsener, which is a different beer classification than Labatt Ale, thus it does not match the product being queried. |
| 9 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is for Labatt Canadian Pilsener, which is a different beer classification than Labatt Ale, thus it does not match the product being queried. |
| 10 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is for Labatt Canadian Pilsener, which is a different beer classification than Labatt Ale, thus it does not match the product being queried. |

</details>

### 20. ⚠️ Asepxia Body Wash 8.45 oz
<details>
<summary><b>View Evaluation (TP: 7 | FP: 0 | FN: 1)</b></summary>

**Description:** *Body Wash, Medicated Acne, Scrub*

**Ground Truth Trusted IDs:** `[1, 2, 3, 4, 5, 6, 7, 9]`  
**LLM Predicted Trusted IDs:** `[1, 2, 3, 4, 5, 7, 9]`  

💡 **Global Pipeline Reasoning:** All trusted results (1, 2, 3, 4, 5, 7, 9) match the product title and description exactly, including the brand 'Asepxia', the format as a body wash, and the medicated acne scrub specification. Untrusted results (6, 8, 10) either lack the 'scrub' specification or refer to a different product type.

| ID | Ground Truth | Prediction | Confidence | Decision Reasoning |
| :--- | :---: | :---: | :---: | :--- |
| 1 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result matches the product title and description exactly, including the brand 'Asepxia', the format as a body wash, and the medicated acne scrub specification. |
| 2 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result matches the product title and description exactly, including the brand 'Asepxia', the format as a body wash, and the medicated acne scrub specification. |
| 3 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result matches the product title and description exactly, including the brand 'Asepxia', the format as a body wash, and the medicated acne scrub specification. |
| 4 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result matches the product title and description exactly, including the brand 'Asepxia', the format as a body wash, and the medicated acne scrub specification. |
| 5 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result matches the product title and description exactly, including the brand 'Asepxia', the format as a body wash, and the medicated acne scrub specification. |
| 6 | 🟢 Trusted | ❌ 🔴 Rejected | 0.50 | While this result mentions 'Asepxia' and is a body wash, it does not specify 'scrub' in the title, which may indicate a different formulation. |
| 7 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result matches the product title and description exactly, including the brand 'Asepxia', the format as a body wash, and the medicated acne scrub specification. |
| 8 | 🔴 Rejected | 🔴 Rejected | 0.50 | This result mentions 'Asepxia' and is a body wash, but it includes 'Exfoliant Scrub for Adults and Teens', which may indicate a different product variation. |
| 9 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result matches the product title and description exactly, including the brand 'Asepxia', the format as a body wash, and the medicated acne scrub specification. |
| 10 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is for a different product type (acne bar soap) and does not match the body wash format. |

</details>

### 21. ⚠️ alani nu fit snacks peanut butter crisp protein bar 12 - 1.62 oz bars
<details>
<summary><b>View Evaluation (TP: 3 | FP: 0 | FN: 2)</b></summary>

**Description:** *protein bar, peanut butter crisp, 12 pack*

**Ground Truth Trusted IDs:** `[2, 3, 4, 5, 8]`  
**LLM Predicted Trusted IDs:** `[8, 2, 5]`  

💡 **Global Pipeline Reasoning:** The trusted results must match the brand 'Alani Nu', the specific flavor 'Peanut Butter Crisp', and the product format of a protein bar. Variations in flavor (like 'Peanut Butter & Jelly') or packaging (like a '4 Pack') disqualify those results. The trusted results are those that exactly match the queried product in all aspects.

| ID | Ground Truth | Prediction | Confidence | Decision Reasoning |
| :--- | :---: | :---: | :---: | :--- |
| 1 | 🔴 Rejected | 🔴 Rejected | 0.90 | This result is for a 'Peanut Butter & Jelly' flavor, which does not match the 'Peanut Butter Crisp' flavor of the queried product. |
| 2 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the exact product title and description, including the brand, format, and flavor. |
| 3 | 🟢 Trusted | ❌ 🔴 Rejected | 0.80 | This result provides nutritional information but does not represent a product for sale; it is not a trusted result. |
| 4 | 🟢 Trusted | ❌ 🔴 Rejected | 0.70 | This result is for a '4 Pack' of the product, which is a different packaging format than the queried '12 Pack'. |
| 5 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the exact product title and description, including the brand, format, and flavor. |
| 6 | 🔴 Rejected | 🔴 Rejected | 0.90 | This result is for a 'Peanut Butter & Jelly' flavor, which does not match the 'Peanut Butter Crisp' flavor of the queried product. |
| 7 | 🔴 Rejected | 🔴 Rejected | 0.90 | This result is for a 'Fruity Cereal' flavor, which does not match the 'Peanut Butter Crisp' flavor of the queried product. |
| 8 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the exact product title and description, including the brand, format, and flavor. |
| 9 | 🔴 Rejected | 🔴 Rejected | 0.80 | This result does not relate to the queried product and includes unrelated items. |
| 10 | 🔴 Rejected | 🔴 Rejected | 0.80 | This result does not relate to the queried product and includes unrelated items. |

</details>

### 22. ⚠️ STIRRINGS MOJITO
<details>
<summary><b>View Evaluation (TP: 4 | FP: 0 | FN: 2)</b></summary>

**Description:** *(None provided)*

**Ground Truth Trusted IDs:** `[1, 3, 4, 5, 6, 7]`  
**LLM Predicted Trusted IDs:** `[1, 3, 4, 5]`  

💡 **Global Pipeline Reasoning:** The trusted results must match the brand 'Stirrings' and the product type 'Mojito Mix'. Results that are recipes or refer to different formats (like cocktail minis) are not trusted. The results that are for 'Mojito Mix' or 'Mojito Mixer' from the same brand are trusted.

| ID | Ground Truth | Prediction | Confidence | Decision Reasoning |
| :--- | :---: | :---: | :---: | :--- |
| 1 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result is for 'Stirrings Mojito Mix', which matches the brand and product type exactly. |
| 2 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is a recipe and does not represent a product for sale. |
| 3 | 🟢 Trusted | 🟢 Trusted | 0.80 | This result refers to 'Stirrings Mojito Mixer', which is a product from the same brand and closely matches the queried product. |
| 4 | 🟢 Trusted | 🟢 Trusted | 0.80 | This result is for 'Stirrings Mixer Mojito', which is a product from the same brand and matches the product type. |
| 5 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result is another listing for 'Stirrings Mojito Mix', matching the brand and product type exactly. |
| 6 | 🟢 Trusted | ❌ 🔴 Rejected | 0.00 | This result is a general promotional page and does not represent a specific product. |
| 7 | 🟢 Trusted | ❌ 🔴 Rejected | 0.00 | This result refers to a different product format (cocktail mixer in a jar) and does not match the queried product. |
| 8 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is a recipe and does not represent a product for sale. |
| 9 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is for 'Stirrings Mojito Cocktail Minis', which is a different product format (mini cocktails) and not the same as the queried product. |

</details>

### 23. ⚠️ Vegetable Lo Mein, 12 oz
<details>
<summary><b>View Evaluation (TP: 0 | FP: 1 | FN: 0)</b></summary>

**Description:** *(None provided)*

**Ground Truth Trusted IDs:** `[]`  
**LLM Predicted Trusted IDs:** `[1]`  

💡 **Global Pipeline Reasoning:** Only the first search result is a trusted match as it directly corresponds to the queried product title and description, while all other results are recipes and do not represent a packaged product.

| ID | Ground Truth | Prediction | Confidence | Decision Reasoning |
| :--- | :---: | :---: | :---: | :--- |
| 1 | 🔴 Rejected | ❌ 🟢 Trusted | 1.00 | This search result matches the exact product title and description, including the brand identity and format (12 oz Vegetable Lo Mein). |
| 2 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is a recipe for Vegetable Lo Mein and does not represent a packaged product, thus it does not match the query. |
| 3 | 🔴 Rejected | 🔴 Rejected | 0.00 | This is also a recipe for Vegetable Lo Mein, not a packaged product, and therefore does not match the query. |
| 4 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is a recipe for Vegetable Lo Mein, which does not correspond to a packaged product, making it untrusted. |
| 5 | 🔴 Rejected | 🔴 Rejected | 0.00 | This is another recipe for Vegetable Lo Mein, not a packaged product, and does not match the query. |
| 6 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is a recipe for Vegetable Lo Mein, not a packaged product, and therefore does not match the query. |
| 7 | 🔴 Rejected | 🔴 Rejected | 0.00 | This is a recipe for Vegetable Lo Mein, which does not represent a packaged product, making it untrusted. |

</details>

### 24. ⚠️ Essence of Beauty Hand Lotion 2.5 oz
<details>
<summary><b>View Evaluation (TP: 2 | FP: 1 | FN: 0)</b></summary>

**Description:** *Hand Lotion, Moisturizing, Sunblossom*

**Ground Truth Trusted IDs:** `[1, 7]`  
**LLM Predicted Trusted IDs:** `[1, 6, 7]`  

💡 **Global Pipeline Reasoning:** The trusted results must match the brand 'Essence of Beauty', the product type 'Hand Lotion', and the scent 'Sunblossom'. Results that refer to body lotions or creams, or different brands, do not meet these criteria.

| ID | Ground Truth | Prediction | Confidence | Decision Reasoning |
| :--- | :---: | :---: | :---: | :--- |
| 1 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result matches the brand 'Essence of Beauty' and the product type 'Moisturizing Hand Lotion' with the same scent 'Sunblossom', making it a trusted match. |
| 2 | 🔴 Rejected | 🔴 Rejected | 0.20 | This result refers to 'Body Lotions' which are different from 'Hand Lotion', thus it does not match the product type. |
| 3 | 🔴 Rejected | 🔴 Rejected | 0.30 | This result mentions 'Body and Hand Cream', which is a different product format than the 'Hand Lotion' queried. |
| 4 | 🔴 Rejected | 🔴 Rejected | 0.10 | This result is for a completely different brand and product, 'Sooryehan', which does not match the queried product. |
| 5 | 🔴 Rejected | 🔴 Rejected | 0.40 | While it mentions 'antibacterial moisturizing hand lotion', it does not specify the brand 'Essence of Beauty' and may refer to a different formulation. |
| 6 | 🔴 Rejected | ❌ 🟢 Trusted | 0.95 | This result is for 'Essence of Beauty Moisturizing Hand Lotion' in the same size (2.5 fl oz), making it a trusted match. |
| 7 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result is identical to the first one, confirming it is a trusted match for the same product. |
| 8 | 🔴 Rejected | 🔴 Rejected | 0.10 | This result is for a different brand ('Beauty Without Cruelty') and does not match the queried product. |
| 9 | 🔴 Rejected | 🔴 Rejected | 0.20 | This result is a repeat of the second one, referring to 'Body Lotions' which do not match the 'Hand Lotion' queried. |

</details>

### 25. ⚠️ Derma E Eczema Relief Lotion 6 oz
<details>
<summary><b>View Evaluation (TP: 6 | FP: 0 | FN: 3)</b></summary>

**Description:** *Relief Lotion, Eczema*

**Ground Truth Trusted IDs:** `[1, 2, 3, 4, 5, 6, 7, 8, 10]`  
**LLM Predicted Trusted IDs:** `[2, 3, 5, 7, 8, 10]`  

💡 **Global Pipeline Reasoning:** The evaluations focused on matching the exact product title, brand, and size. Results that specified 'Eczema Relief Cream' were rejected as they represent a different product type. Variations in wording that did not specify the 6 oz size were also deemed untrusted.

| ID | Ground Truth | Prediction | Confidence | Decision Reasoning |
| :--- | :---: | :---: | :---: | :--- |
| 1 | 🟢 Trusted | ❌ 🔴 Rejected | 0.70 | This result is for 'Eczema Relief Lotion - Derma E', which does not specify the 6 oz size and may not be the exact product. |
| 2 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the exact product title and description, confirming it is 'Derma E Eczema Relief Lotion 6 oz'. |
| 3 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result is for 'Derma E Eczema Relief Lotion, 6 oz.', matching the product title and size exactly. |
| 4 | 🟢 Trusted | ❌ 🔴 Rejected | 0.80 | This result is for 'Eczema Relief Cream', which is a different product type than the lotion being queried. |
| 5 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result is for 'Derma E Eczema Relief Lotion, 6 oz.', matching the product title and size exactly. |
| 6 | 🟢 Trusted | ❌ 🔴 Rejected | 0.60 | This result is for 'Eczema Relief Lotion - Derma E', which does not specify the 6 oz size and may not be the exact product. |
| 7 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the exact product title and description, confirming it is 'Derma E Eczema Relief Lotion 6 oz'. |
| 8 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result is for 'Derma E Eczema Relief Lotion, 6 fl oz', which is the same product in a different measurement format. |
| 9 | 🔴 Rejected | 🔴 Rejected | 0.80 | This result is for 'Eczema Relief Cream', which is a different product type than the lotion being queried. |
| 10 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result is for 'Derma-E Eczema Relief Lotion - 6 oz', matching the product title and size exactly. |

</details>

### 26. ⚠️ act ii butter popcorn 6 ea
<details>
<summary><b>View Evaluation (TP: 0 | FP: 0 | FN: 1)</b></summary>

**Description:** *popcorn, butter*

**Ground Truth Trusted IDs:** `[2]`  
**LLM Predicted Trusted IDs:** `[]`  

💡 **Global Pipeline Reasoning:** All search results are for variations of ACT II popcorn that do not match the exact product queried, which is 'act ii butter popcorn'. The variations include 'Butter Lovers', 'Xtreme Butter', and 'Butter Flavored, Homestyle', which are all distinct from the original 'butter' flavor.

| ID | Ground Truth | Prediction | Confidence | Decision Reasoning |
| :--- | :---: | :---: | :---: | :--- |
| 1 | 🔴 Rejected | 🔴 Rejected | 0.80 | This result is for 'Butter Lovers Microwave Popcorn', which is a different flavor variant than the queried 'butter' popcorn. |
| 2 | 🟢 Trusted | ❌ 🔴 Rejected | 0.70 | This result is a generic 'Butter Popcorn' without specific brand identification, making it untrusted. |
| 3 | 🔴 Rejected | 🔴 Rejected | 0.90 | This result is for 'Butter Lover' popcorn, which is a different flavor variant than the queried 'butter' popcorn. |
| 4 | 🔴 Rejected | 🔴 Rejected | 0.90 | This result is for 'Butter Lovers Microwave Popcorn', which is a different flavor variant than the queried 'butter' popcorn. |
| 5 | 🔴 Rejected | 🔴 Rejected | 0.90 | This result is for 'Xtreme Butter' popcorn, which is a different flavor variant than the queried 'butter' popcorn. |
| 6 | 🔴 Rejected | 🔴 Rejected | 0.90 | This result is for 'Xtreme Butter' popcorn, which is a different flavor variant than the queried 'butter' popcorn. |
| 7 | 🔴 Rejected | 🔴 Rejected | 0.90 | This result is for 'Butter Flavored, Homestyle' popcorn, which is a different flavor variant than the queried 'butter' popcorn. |
| 8 | 🔴 Rejected | 🔴 Rejected | 0.90 | This result is for 'Xtreme Butter' popcorn, which is a different flavor variant than the queried 'butter' popcorn. |
| 9 | 🔴 Rejected | 🔴 Rejected | 0.90 | This result is for 'Xtreme Butter' popcorn, which is a different flavor variant than the queried 'butter' popcorn. |
| 10 | 🔴 Rejected | 🔴 Rejected | 0.90 | This result is for 'Butter Lover' popcorn, which is a different flavor variant than the queried 'butter' popcorn. |

</details>

### 27. ⚠️ Minestrone Soup, 24 oz
<details>
<summary><b>View Evaluation (TP: 0 | FP: 2 | FN: 0)</b></summary>

**Description:** *(None provided)*

**Ground Truth Trusted IDs:** `[]`  
**LLM Predicted Trusted IDs:** `[1, 6]`  

💡 **Global Pipeline Reasoning:** The trusted results must match the brand and product format exactly. Signature Select/Cafe Minestrone Soup is the only brand that matches the queried product, while all other results are from different brands (Whole Foods Market and Home Chef), which disqualifies them regardless of format or size.

| ID | Ground Truth | Prediction | Confidence | Decision Reasoning |
| :--- | :---: | :---: | :---: | :--- |
| 1 | 🔴 Rejected | ❌ 🟢 Trusted | 0.90 | The product is from the same brand (Signature Select/Cafe) and matches the title and format exactly (Minestrone Soup, 24 oz). |
| 2 | 🔴 Rejected | 🔴 Rejected | 0.80 | This result is from Whole Foods Market, which is a different brand than the queried product, despite having the same format and size. |
| 3 | 🔴 Rejected | 🔴 Rejected | 0.70 | This result is from Home Chef, a different brand, even though it matches the format and size of the queried product. |
| 4 | 🔴 Rejected | 🔴 Rejected | 0.70 | This result is also from Home Chef, which is a different brand than the queried product, despite matching the format and size. |
| 5 | 🔴 Rejected | 🔴 Rejected | 0.80 | This result is from Whole Foods Market, which is a different brand than the queried product, despite having the same format and size. |
| 6 | 🔴 Rejected | ❌ 🟢 Trusted | 0.90 | This result is from the same brand (Signature Select/Cafe) and matches the title and format exactly (Minestrone Soup, 24 oz). |
| 7 | 🔴 Rejected | 🔴 Rejected | 0.70 | This result is from Home Chef, a different brand, even though it matches the format and size of the queried product. |
| 8 | 🔴 Rejected | 🔴 Rejected | 0.60 | This result does not match the brand of the queried product and includes additional ingredients that suggest it is a different formulation. |
| 9 | 🔴 Rejected | 🔴 Rejected | 0.70 | This result is from Home Chef, which is a different brand than the queried product, despite matching the format and size. |

</details>

### 28. ⚠️ Emu Lemongrass Hand Sanitizer Mist 2.2 oz
<details>
<summary><b>View Evaluation (TP: 8 | FP: 0 | FN: 1)</b></summary>

**Description:** *Hand Sanitizer Mist, Lemongrass*

**Ground Truth Trusted IDs:** `[1, 2, 3, 4, 5, 6, 8, 9, 10]`  
**LLM Predicted Trusted IDs:** `[1, 2, 3, 4, 5, 8, 9, 10]`  

💡 **Global Pipeline Reasoning:** All trusted results match the brand 'emu', the product format 'Hand Sanitizer Mist', and the flavor 'Lemongrass' with the same size (2.2 oz). Non-trusted results either do not specify the brand or are generic descriptions that do not match the product.

| ID | Ground Truth | Prediction | Confidence | Decision Reasoning |
| :--- | :---: | :---: | :---: | :--- |
| 1 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result matches the brand 'emu' and the product format 'Hand Sanitizer Mist' with the same flavor 'Lemongrass' and size (2.2 oz). |
| 2 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result is for 'Emu Lemongrass Mist Hand Sanitizer' which matches the brand, format, flavor, and size (2.2 fl oz). |
| 3 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result matches the brand 'emu', the product format 'Hand Sanitizer Mist', and the flavor 'Lemongrass' with the same size (2.2 oz). |
| 4 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result is for 'EMU Hand Sanitizer Mist - Lemongrass 2.2 oz', matching the brand, format, flavor, and size exactly. |
| 5 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result matches the brand 'Emu', the product format 'Hand Sanitizing Mist', and the flavor 'Lemongrass' with the same size (2.2 oz). |
| 6 | 🟢 Trusted | ❌ 🔴 Rejected | 0.00 | This result does not match the brand 'emu' and is a generic description of a hand sanitizer mist, which does not specify the brand or product name. |
| 7 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result does not match the brand 'emu' and is a generic description of a hand sanitizer, which does not specify the product name. |
| 8 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result matches the brand 'emu', the product format 'Hand Sanitizer Mist', and the flavor 'Lemongrass' with the same size (2.2 oz). |
| 9 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result matches the brand 'Emu', the product format 'Hand Sanitizer Mist', and the flavor 'Lemongrass' with the same size (2.2 oz). |
| 10 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result matches the brand 'Emu', the product format 'Hand Sanitizer Mist', and the flavor 'Lemongrass' with the same size (2.2 oz). |

</details>

### 29. ✅ Large Org Apricot
<details>
<summary><b>View Evaluation (TP: 0 | FP: 0 | FN: 0)</b></summary>

**Description:** *(None provided)*

**Ground Truth Trusted IDs:** `[]`  
**LLM Predicted Trusted IDs:** `[]`  

💡 **Global Pipeline Reasoning:** All search results are either specific products (nectars, juices, or kernels) that do not match the generic 'Large Org Apricot' in format or type. The queried product is a generic item, and none of the results are generic apricots, leading to a rejection of all results.

| ID | Ground Truth | Prediction | Confidence | Decision Reasoning |
| :--- | :---: | :---: | :---: | :--- |
| 1 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is for 'Organic Apricot Nectar', which is a liquid product, while the queried product is a generic 'Large Org Apricot', which does not match in format or specific product type. |
| 2 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is for 'Certified Organic Masumoto Golden Sweet Apricot-Noyaux', which is a specific variety of apricot and does not match the generic 'Large Org Apricot'. |
| 3 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is for 'Bitter Apricot Kernels', which are seeds and not the same as the queried generic 'Large Org Apricot'. |
| 4 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is for 'Sweet Apricot Kernels', which are also seeds and do not match the generic 'Large Org Apricot'. |
| 5 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is for 'Organic Bitter Apricot Kernels', which are seeds and not the same as the queried generic 'Large Org Apricot'. |
| 6 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is for 'Pomona Organic Apricot Juice', which is a liquid product and does not match the generic 'Large Org Apricot'. |
| 7 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is a duplicate of result 1, which is for 'Organic Apricot Nectar' and does not match the generic 'Large Org Apricot'. |
| 8 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is for 'Pure Organic Apricot Juice', which is a liquid product and does not match the generic 'Large Org Apricot'. |
| 9 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is for '100% Organic Apricot Nectar Juice', which is a liquid product and does not match the generic 'Large Org Apricot'. |
| 10 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is for 'Yoga Juice Apricot Nectar', which is a liquid product and does not match the generic 'Large Org Apricot'. |

</details>

### 30. ⚠️ Kelly & Katie Betty Clutch
<details>
<summary><b>View Evaluation (TP: 3 | FP: 0 | FN: 1)</b></summary>

**Description:** *(None provided)*

**Ground Truth Trusted IDs:** `[1, 2, 3, 4]`  
**LLM Predicted Trusted IDs:** `[1, 2, 4]`  

💡 **Global Pipeline Reasoning:** All trusted results (1, 2, and 4) match the exact product title and brand. Result 3 is not trusted as it refers to a general category of clutches rather than the specific 'Betty Clutch'.

| ID | Ground Truth | Prediction | Confidence | Decision Reasoning |
| :--- | :---: | :---: | :---: | :--- |
| 1 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result is for the exact product, matching the brand 'Kelly & Katie' and the product name 'Betty Clutch'. |
| 2 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result is for the exact product, matching the brand 'Kelly & Katie' and the product name 'Betty Clutch'. |
| 3 | 🟢 Trusted | ❌ 🔴 Rejected | 0.00 | This result is not trusted as it refers to 'Clutches' in general and does not specify the exact 'Betty Clutch' product. |
| 4 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result is for the exact product, matching the brand 'Kelly & Katie' and the product name 'Betty Clutch'. |

</details>

### 31. ⚠️ TRES AGAVE STRAWBERRY MIXER
<details>
<summary><b>View Evaluation (TP: 7 | FP: 0 | FN: 2)</b></summary>

**Description:** *(None provided)*

**Ground Truth Trusted IDs:** `[1, 2, 3, 4, 5, 6, 8, 9, 10]`  
**LLM Predicted Trusted IDs:** `[2, 3, 4, 5, 8, 9, 10]`  

💡 **Global Pipeline Reasoning:** The search results were evaluated based on brand identity, product format, and flavor. Trusted results must match the brand 'Tres Agaves' and the product type 'Strawberry Mixer'. Results that included 'Organic Strawberry Margarita Mix' were rejected as they did not match the exact product title. Additionally, variations in flavor or additional ingredients that change the product type were also rejected.

| ID | Ground Truth | Prediction | Confidence | Decision Reasoning |
| :--- | :---: | :---: | :---: | :--- |
| 1 | 🟢 Trusted | ❌ 🔴 Rejected | 0.00 | This result is for 'Organic Strawberry Margarita Mix', which does not match the exact product title 'TRES AGAVE STRAWBERRY MIXER'. |
| 2 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result is for 'Tres Agaves Organic Strawberry Margarita Mix 1L', which matches the brand and product type exactly. |
| 3 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result is for 'Tres Agaves Strawberry Margarita Mix', which matches the brand and product type exactly. |
| 4 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result is for 'Tres Agaves Strawberry Margarita Mix 1.0 l', which matches the brand and product type exactly. |
| 5 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result is for 'Tres Agave Strawberry Margarita Mix 1Lt', which matches the brand and product type exactly. |
| 6 | 🟢 Trusted | ❌ 🔴 Rejected | 0.00 | This result is for 'Organic Strawberry Margarita Mix', which does not match the exact product title 'TRES AGAVE STRAWBERRY MIXER'. |
| 7 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result includes 'Lime and Strawberry', which indicates a different flavor combination and does not match the exact product. |
| 8 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result is for 'Tres Agave Strawberry Margarita Mix 1Lt', which matches the brand and product type exactly. |
| 9 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result is for 'Tres Agaves Strawberry Margarita Mix', which matches the brand and product type exactly. |
| 10 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result is for 'Tres Agaves Organic Strawberry Margarita Mix', which matches the brand and product type exactly. |

</details>

### 32. ⚠️ ALOHA PRTN PWDR VANILLA         1 EA
<details>
<summary><b>View Evaluation (TP: 7 | FP: 0 | FN: 3)</b></summary>

**Description:** *(None provided)*

**Ground Truth Trusted IDs:** `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`  
**LLM Predicted Trusted IDs:** `[2, 3, 4, 5, 7, 8, 10]`  

💡 **Global Pipeline Reasoning:** The evaluations focused on ensuring that the brand ALOHA was explicitly mentioned in the title of the search results. All results that matched the ALOHA brand and the vanilla flavor were trusted, while those that did not specify the brand or were generic were not trusted.

| ID | Ground Truth | Prediction | Confidence | Decision Reasoning |
| :--- | :---: | :---: | :---: | :--- |
| 1 | 🟢 Trusted | ❌ 🔴 Rejected | 0.80 | This result is for a vegan vanilla protein powder but does not specify the ALOHA brand explicitly in the title, which raises concerns about brand identity. |
| 2 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result is for ALOHA Organic Plant Based Protein Powder in vanilla flavor, matching the brand and flavor exactly. |
| 3 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result matches the ALOHA brand and specifies the vanilla flavor, making it a trusted result. |
| 4 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result is for ALOHA Plant Based Protein Powder in vanilla flavor, matching both the brand and flavor. |
| 5 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result is for Aloha Organic Plant-Based Protein Powder in vanilla flavor, matching the brand and flavor exactly. |
| 6 | 🟢 Trusted | ❌ 🔴 Rejected | 0.70 | This result is for a vegan vanilla protein powder but does not specify the ALOHA brand explicitly in the title, which raises concerns about brand identity. |
| 7 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result is for Aloha Organic Plant-Based Protein Powder in vanilla flavor, matching the brand and flavor exactly. |
| 8 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result is for ALOHA Plant Based Protein Powder in vanilla flavor, matching both the brand and flavor. |
| 9 | 🟢 Trusted | ❌ 🔴 Rejected | 0.60 | This result is for a generic 'best vanilla protein powder' and does not specify the ALOHA brand explicitly, which raises concerns about brand identity. |
| 10 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result matches the ALOHA brand and specifies the vanilla flavor, making it a trusted result. |

</details>

### 33. ⚠️ V8 V-Fusion 100% Juice 6 ea
<details>
<summary><b>View Evaluation (TP: 3 | FP: 0 | FN: 4)</b></summary>

**Description:** *100% Juice, Pomegranate Blueberry*

**Ground Truth Trusted IDs:** `[1, 2, 3, 4, 5, 6, 7]`  
**LLM Predicted Trusted IDs:** `[3, 4, 5]`  

💡 **Global Pipeline Reasoning:** The evaluations focused on matching the brand (V8), the product format (100% juice), and the flavor (Pomegranate Blueberry). Results that indicated a different product line or format, or did not specify the V8 brand, were rejected.

| ID | Ground Truth | Prediction | Confidence | Decision Reasoning |
| :--- | :---: | :---: | :---: | :--- |
| 1 | 🟢 Trusted | ❌ 🔴 Rejected | 0.00 | This result is a generic '100% Juice Pomegranate Blueberry Juice' and does not specify the V8 brand, violating the brand matching rule. |
| 2 | 🟢 Trusted | ❌ 🔴 Rejected | 0.00 | This result refers to 'V8® Fruits & Vegetables Blends', which indicates a different product line and does not match the exact product being queried. |
| 3 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result is for 'V8® Pomegranate Blueberry 100% Fruit and Vegetable Juice', which matches the brand, format, and flavor exactly. |
| 4 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result is for 'V8 V-Fusion 100% Pomegranate Blueberry Juice', which matches the brand, format, and flavor exactly. |
| 5 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result is for 'V8 V-Fusion Pomegranate Blueberry 6-PACK', which matches the brand and flavor, and the format is acceptable as it is a pack of the same product. |
| 6 | 🟢 Trusted | ❌ 🔴 Rejected | 0.00 | This result is a duplicate of result 2 and refers to 'V8® Fruits & Vegetables Blends', which indicates a different product line. |
| 7 | 🟢 Trusted | ❌ 🔴 Rejected | 0.00 | This result is for 'V8 Pomegranate Blueberry 100% Fruit and Vegetable Juice, 46 fl oz Bottle (6 Pack)', which is a different product format and does not match the exact product being queried. |
| 8 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is for 'V8 V Fusion + Energy Pomegranate Blueberry', which indicates a different product with added energy components, violating the format rule. |
| 9 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is for 'V8 Blends 100% Juice Pomegranate Blueberry Juice', which indicates a different product line and does not match the exact product being queried. |
| 10 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is a duplicate of result 1 and does not specify the V8 brand, violating the brand matching rule. |

</details>

### 34. ✅ Signature SELECT Cashew Chicken Salad - 0.50 Lb
<details>
<summary><b>View Evaluation (TP: 3 | FP: 0 | FN: 0)</b></summary>

**Description:** *(None provided)*

**Ground Truth Trusted IDs:** `[9, 10, 5]`  
**LLM Predicted Trusted IDs:** `[9, 10, 5]`  

💡 **Global Pipeline Reasoning:** The product being evaluated is 'Signature SELECT Cashew Chicken Salad', which requires exact brand and product name matching. Only results that explicitly mention 'Signature SELECT' and 'Cashew Chicken Salad' are trusted. Generic items or variations with different brands are not trusted.

| ID | Ground Truth | Prediction | Confidence | Decision Reasoning |
| :--- | :---: | :---: | :---: | :--- |
| 1 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result does not match the brand 'Signature SELECT' and is a generic item. |
| 2 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result does not match the brand 'Signature SELECT' and is a generic item. |
| 3 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result features 'Napa Valley' in the title, indicating a different brand or variation. |
| 4 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result does not match the brand 'Signature SELECT' and is a generic item. |
| 5 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the exact brand 'Signature SELECT' and the product name 'Cashew Chicken Salad'. |
| 6 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result does not match the brand 'Signature SELECT' and is a generic item. |
| 7 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result does not match the brand 'Signature SELECT' and is a generic item. |
| 8 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result does not match the brand 'Signature SELECT' and is a generic item. |
| 9 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the exact brand 'Signature SELECT' and the product name 'Cashew Chicken Salad'. |
| 10 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the exact brand 'Signature SELECT' and the product name 'Cashew Chicken Salad'. |

</details>

### 35. ⚠️ protein water water 4 ea
<details>
<summary><b>View Evaluation (TP: 0 | FP: 2 | FN: 0)</b></summary>

**Description:** *water, protein, punch*

**Ground Truth Trusted IDs:** `[]`  
**LLM Predicted Trusted IDs:** `[1, 6]`  

💡 **Global Pipeline Reasoning:** The trusted results are limited to those that match the brand TATU and the product type of protein water. Other results either represent different brands, specific flavors, or types of protein drinks that do not align with the generic description provided.

| ID | Ground Truth | Prediction | Confidence | Decision Reasoning |
| :--- | :---: | :---: | :---: | :--- |
| 1 | 🔴 Rejected | ❌ 🟢 Trusted | 0.90 | This result is for TATU Protein Water, which matches the brand and product type (protein water) in the query. |
| 2 | 🔴 Rejected | 🔴 Rejected | 0.80 | This product is a whey isolate protein drink but does not match the brand or specific product type of 'protein water' as it is more of a supplement. |
| 3 | 🔴 Rejected | 🔴 Rejected | 0.70 | This is a tropical punch protein drink, which indicates a specific flavor variation that does not match the generic 'punch' in the query. |
| 4 | 🔴 Rejected | 🔴 Rejected | 0.60 | This product is a protein water but contains different ingredients and flavoring, which does not match the generic description provided. |
| 5 | 🔴 Rejected | 🔴 Rejected | 0.50 | This is a berry-flavored protein water, which does not match the generic 'punch' flavor in the query. |
| 6 | 🔴 Rejected | ❌ 🟢 Trusted | 0.90 | This is another listing for TATU Protein Water, confirming the brand and product type match. |
| 7 | 🔴 Rejected | 🔴 Rejected | 0.40 | This product is a flavored protein water, which does not match the generic description of 'water, protein, punch'. |
| 8 | 🔴 Rejected | 🔴 Rejected | 0.50 | This is a different brand of protein water with multiple flavor options, which does not match the generic description. |
| 9 | 🔴 Rejected | 🔴 Rejected | 0.40 | This is a flavored protein water that does not match the generic description of 'water, protein, punch'. |
| 10 | 🔴 Rejected | 🔴 Rejected | 0.30 | This is a general category page for protein drinks and does not specify a product that matches the query. |

</details>

### 36. ⚠️ Birds Eye Oven Roasters, Zesty Ranch Broccoli, Frozen Vegetables, 14 oz. Bag
<details>
<summary><b>View Evaluation (TP: 6 | FP: 0 | FN: 3)</b></summary>

**Description:** *Broccoli, Zesty Ranch*

**Ground Truth Trusted IDs:** `[1, 2, 3, 4, 6, 7, 8, 9, 10]`  
**LLM Predicted Trusted IDs:** `[2, 3, 4, 7, 8, 9]`  

💡 **Global Pipeline Reasoning:** The evaluations focused on matching the brand, product name, and format. Results that indicated a 'meal' or were generic terms were not trusted. All trusted results matched the exact product description of 'Birds Eye Oven Roasters, Zesty Ranch Broccoli, Frozen Vegetables, 14 oz. Bag'.

| ID | Ground Truth | Prediction | Confidence | Decision Reasoning |
| :--- | :---: | :---: | :---: | :--- |
| 1 | 🟢 Trusted | ❌ 🔴 Rejected | 0.70 | This result refers to a 'meal' which implies additional components or ingredients not present in the original product, thus it is not the same as the queried product. |
| 2 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the brand, product name, and format exactly as specified in the query. |
| 3 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the brand, product name, and format exactly as specified in the query. |
| 4 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the brand, product name, and format exactly as specified in the query. |
| 5 | 🔴 Rejected | 🔴 Rejected | 0.50 | This result is a nutrition facts page and does not represent a product for sale, thus it cannot be trusted. |
| 6 | 🟢 Trusted | ❌ 🔴 Rejected | 0.70 | This result refers to a 'meal' which implies additional components or ingredients not present in the original product, thus it is not the same as the queried product. |
| 7 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the brand, product name, and format exactly as specified in the query. |
| 8 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the brand, product name, and format exactly as specified in the query. |
| 9 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the brand, product name, and format exactly as specified in the query. |
| 10 | 🟢 Trusted | ❌ 🔴 Rejected | 0.60 | This result refers to 'Birds Eye Broccoli' which is a generic term and does not specify the exact product as queried. |

</details>

### 37. ⚠️ Ghirardelli Peppermint Bark Dark Chocolate Squares 7.7 oz
<details>
<summary><b>View Evaluation (TP: 9 | FP: 0 | FN: 1)</b></summary>

**Description:** *Dark Chocolate Squares, Peppermint Bark*

**Ground Truth Trusted IDs:** `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`  
**LLM Predicted Trusted IDs:** `[1, 3, 4, 5, 6, 7, 8, 9, 10]`  

💡 **Global Pipeline Reasoning:** All trusted results match the brand Ghirardelli and the product type of Dark Chocolate Peppermint Bark Squares. The only untrusted result is a combo pack, which does not match the single product queried.

| ID | Ground Truth | Prediction | Confidence | Decision Reasoning |
| :--- | :---: | :---: | :---: | :--- |
| 1 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result matches the brand Ghirardelli and the product type (Dark Chocolate Peppermint Bark Squares) closely, making it a trusted result. |
| 2 | 🟢 Trusted | ❌ 🔴 Rejected | 0.70 | This result is for a case of Peppermint Bark & Dark Chocolate Squares, which implies a combo pack rather than the single product queried. |
| 3 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result matches the brand Ghirardelli and the product type (Dark Chocolate Peppermint Bark Squares) closely, making it a trusted result. |
| 4 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result matches the brand Ghirardelli and the product type (Dark Chocolate Peppermint Bark Squares) closely, making it a trusted result. |
| 5 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result matches the brand Ghirardelli and the product type (Dark Chocolate Peppermint Bark Chocolate Squares) closely, making it a trusted result. |
| 6 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result matches the brand Ghirardelli and the product type (Dark Chocolate Peppermint Bark Squares) closely, making it a trusted result. |
| 7 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result matches the brand Ghirardelli and the product type (Dark Chocolate Peppermint Bark Squares) closely, making it a trusted result. |
| 8 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result matches the brand Ghirardelli and the product type (Dark Chocolate Peppermint Bark Squares) closely, making it a trusted result. |
| 9 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result matches the brand Ghirardelli and the product type (Dark Chocolate Peppermint Bark Squares) closely, making it a trusted result. |
| 10 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result matches the brand Ghirardelli and the product type (Dark Chocolate Peppermint Bark Squares) closely, making it a trusted result. |

</details>

### 38. ⚠️ FRSH BKD FOCACCIA BRD
<details>
<summary><b>View Evaluation (TP: 0 | FP: 1 | FN: 0)</b></summary>

**Description:** *BREAD FRESH BAKED*

**Ground Truth Trusted IDs:** `[]`  
**LLM Predicted Trusted IDs:** `[5]`  

💡 **Global Pipeline Reasoning:** All results except for the last one are recipes for making focaccia bread, which do not represent a product for sale. The last result is a product listing for fresh baked focaccia bread, which aligns with the queried product.

| ID | Ground Truth | Prediction | Confidence | Decision Reasoning |
| :--- | :---: | :---: | :---: | :--- |
| 1 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is a recipe for making focaccia bread, not a product for sale, and does not match the product type. |
| 2 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is also a recipe for focaccia bread, not a product, and does not match the product type. |
| 3 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is another recipe for focaccia bread, not a product for sale, and does not match the product type. |
| 4 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result is a recipe for focaccia bread, not a product, and does not match the product type. |
| 5 | 🔴 Rejected | ❌ 🟢 Trusted | 0.90 | This result is for a product called 'Fresh Fresh Baked Focaccia Bread', which matches the brand and product type of fresh baked focaccia bread. |

</details>

### 39. ⚠️ Ultra Lift Deep Wrinkle Day Cream 1.6 oz
<details>
<summary><b>View Evaluation (TP: 3 | FP: 0 | FN: 1)</b></summary>

**Description:** *Deep Wrinkle Day Cream, Intensive*

**Ground Truth Trusted IDs:** `[9, 2, 3, 7]`  
**LLM Predicted Trusted IDs:** `[2, 3, 7]`  

💡 **Global Pipeline Reasoning:** The trusted results must match the exact product title and description, which includes the specific formulation and purpose. Results that deviate in product type (e.g., firming moisturizer vs. deep wrinkle cream) or do not match the exact title are not trusted.

| ID | Ground Truth | Prediction | Confidence | Decision Reasoning |
| :--- | :---: | :---: | :---: | :--- |
| 1 | 🔴 Rejected | 🔴 Rejected | 0.80 | This result is for an 'Anti-Wrinkle Firming Moisturizer' which is a different product than the 'Deep Wrinkle Day Cream' being queried. |
| 2 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the exact title and description of the queried product, 'Ultra Lift Deep Wrinkle Day Cream, Intensive'. |
| 3 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the exact title and description of the queried product, 'Ultra Lift Deep Wrinkle Day Cream, Intensive'. |
| 4 | 🔴 Rejected | 🔴 Rejected | 0.70 | This result is for a 'Daily Targeted Deep Wrinkle Treatment', which is a different product than the 'Deep Wrinkle Day Cream'. |
| 5 | 🔴 Rejected | 🔴 Rejected | 0.60 | This result is for an 'Anti-Aging Face Moisturizer' which is a different product than the 'Deep Wrinkle Day Cream'. |
| 6 | 🔴 Rejected | 🔴 Rejected | 0.80 | This result is for an 'Anti-Wrinkle Firming Moisturizer' which is a different product than the 'Deep Wrinkle Day Cream'. |
| 7 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the exact title and description of the queried product, 'Ultra Lift Deep Wrinkle Day Cream, Intensive'. |
| 8 | 🔴 Rejected | 🔴 Rejected | 0.50 | This result is for an 'Anti Ageing Day Cream' which does not match the specific 'Deep Wrinkle Day Cream' being queried. |
| 9 | 🟢 Trusted | ❌ 🔴 Rejected | 0.40 | This result does not provide enough information to confirm it matches the queried product and appears to be incomplete. |
| 10 | 🔴 Rejected | 🔴 Rejected | 0.60 | This result is for an 'Anti-Aging Face Moisturizer' which is a different product than the 'Deep Wrinkle Day Cream'. |

</details>

### 40. ⚠️ health warrior pumpkin seed bar dark chocolate 1.23 oz
<details>
<summary><b>View Evaluation (TP: 4 | FP: 0 | FN: 5)</b></summary>

**Description:** *pumpkin seed bar, dark chocolate flavor*

**Ground Truth Trusted IDs:** `[1, 2, 3, 4, 5, 6, 8, 9, 10]`  
**LLM Predicted Trusted IDs:** `[9, 2, 3, 5]`  

💡 **Global Pipeline Reasoning:** The evaluations were based on matching the brand, product format, and flavor. Exact matches were trusted, while variations or different formats (like peanut inclusion) were rejected.

| ID | Ground Truth | Prediction | Confidence | Decision Reasoning |
| :--- | :---: | :---: | :---: | :--- |
| 1 | 🟢 Trusted | ❌ 🔴 Rejected | 0.70 | The title 'Pumpkin Dark Chocolate' does not match the exact product title 'health warrior pumpkin seed bar dark chocolate', as it lacks the brand and specific product format. |
| 2 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the exact product title and description, including the brand, format, and flavor. |
| 3 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the exact product title and description, including the brand, format, and flavor. |
| 4 | 🟢 Trusted | ❌ 🔴 Rejected | 0.60 | While it includes the brand and flavor, the title 'Health Warrior, Dark Chocolate Flavor, Pumpkin Seed Bar' does not match the exact product title. |
| 5 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the exact product title and description, including the brand, format, and flavor. |
| 6 | 🟢 Trusted | ❌ 🔴 Rejected | 0.50 | This result is a duplicate of result 2 and does not provide new information. |
| 7 | 🔴 Rejected | 🔴 Rejected | 0.40 | This result includes 'Peanut' in the title, indicating a different product variation that is not the same as the queried product. |
| 8 | 🟢 Trusted | ❌ 🔴 Rejected | 0.50 | This result is a duplicate of result 3 and does not provide new information. |
| 9 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the exact product title and description, including the brand, format, and flavor. |
| 10 | 🟢 Trusted | ❌ 🔴 Rejected | 0.30 | This result includes 'Peanut' in the title, indicating a different product variation that is not the same as the queried product. |

</details>

### 41. ⚠️ ChapStick Classic Collection Lip Care 3 ea
<details>
<summary><b>View Evaluation (TP: 4 | FP: 0 | FN: 4)</b></summary>

**Description:** *Lip Care, Classic Collection*

**Ground Truth Trusted IDs:** `[1, 2, 3, 4, 5, 6, 8, 9]`  
**LLM Predicted Trusted IDs:** `[8, 2, 3, 6]`  

💡 **Global Pipeline Reasoning:** The evaluations focused on matching the exact product title and description, ensuring that only results for the Classic Collection were trusted. Variations in flavor and product type (e.g., bundles or different formulations) were critical in determining trustworthiness.

| ID | Ground Truth | Prediction | Confidence | Decision Reasoning |
| :--- | :---: | :---: | :---: | :--- |
| 1 | 🟢 Trusted | ❌ 🔴 Rejected | 0.80 | This result is a bundle that includes additional flavors (Spearmint, Cherry, and Strawberry) not present in the queried product, which is specifically for the Classic Collection. |
| 2 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the exact product title and description, confirming it is for the ChapStick Classic Collection Lip Care 3 ea. |
| 3 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result also matches the exact product title and description, confirming it is for the ChapStick Classic Collection Lip Care 3 ea. |
| 4 | 🟢 Trusted | ❌ 🔴 Rejected | 0.70 | This result refers to the Classic Original flavor but does not specify the Classic Collection, which may imply a different product. |
| 5 | 🟢 Trusted | ❌ 🔴 Rejected | 0.60 | This result is a variety pack that includes flavors (Spearmint, Cherry, and Strawberry) not present in the queried product, which is specifically for the Classic Collection. |
| 6 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the exact product title and description, confirming it is for the ChapStick Classic Collection Lip Care 3 ea. |
| 7 | 🔴 Rejected | 🔴 Rejected | 0.50 | This result is a variety pack that includes flavors (Spearmint, Cherry, and Strawberry) not present in the queried product, which is specifically for the Classic Collection. |
| 8 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the exact product title and description, confirming it is for the ChapStick Classic Collection Lip Care 3 ea. |
| 9 | 🟢 Trusted | ❌ 🔴 Rejected | 0.60 | This result specifies 'Classic Original', which is a different product from the Classic Collection queried. |
| 10 | 🔴 Rejected | 🔴 Rejected | 0.70 | This result refers to the Classic Original flavor but does not specify the Classic Collection, which may imply a different product. |

</details>

### 42. ⚠️ Porcelana Skin Lightening Cream 3 oz
<details>
<summary><b>View Evaluation (TP: 2 | FP: 0 | FN: 3)</b></summary>

**Description:** *Skin Lightening Cream, Fade Dark Spots Daytime Treatment*

**Ground Truth Trusted IDs:** `[2, 5, 6, 7, 10]`  
**LLM Predicted Trusted IDs:** `[2, 7]`  

💡 **Global Pipeline Reasoning:** The evaluations were based on the critical matching rules, focusing on brand identity, product format, and specific product variations. Trusted results were those that matched the exact title and description of the queried product, while others were rejected due to differences in formulation (day vs night), product type (hydration vs lightening), or lack of exact title match.

| ID | Ground Truth | Prediction | Confidence | Decision Reasoning |
| :--- | :---: | :---: | :---: | :--- |
| 1 | 🔴 Rejected | 🔴 Rejected | 0.70 | This result refers to a 'Daytime Hydration Skin Lightening Cream', which suggests a different formulation than the queried product, which is specifically a 'Skin Lightening Cream'. |
| 2 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the exact title and description of the queried product, 'Porcelana Skin Lightening Cream, 3 OZ', making it a trusted result. |
| 3 | 🔴 Rejected | 🔴 Rejected | 0.60 | This result is for a 'Nighttime Hydration Cream', which is a different product than the daytime treatment specified in the query. |
| 4 | 🔴 Rejected | 🔴 Rejected | 0.50 | This result is for a 'Skin Brightening Night Cream', which indicates it is a different product than the daytime skin lightening cream being queried. |
| 5 | 🟢 Trusted | ❌ 🔴 Rejected | 0.40 | This result refers to a 'Day Cream And Fade Dark Spots Treatment', which suggests a different formulation or combination than the queried product. |
| 6 | 🟢 Trusted | ❌ 🔴 Rejected | 0.50 | This result is for a 'Day Skin Lightening Cream', but it does not match the exact title of the queried product, which is specifically 'Skin Lightening Cream'. |
| 7 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the exact title and description of the queried product, 'Porcelana Skin Lightening Cream, 3 OZ', making it a trusted result. |
| 8 | 🔴 Rejected | 🔴 Rejected | 0.60 | This result refers to a 'Daytime Hydration Cream', which suggests a different formulation than the queried product, which is specifically a 'Skin Lightening Cream'. |
| 9 | 🔴 Rejected | 🔴 Rejected | 0.50 | This result is for a 'Skin Brightening Night Cream', which indicates it is a different product than the daytime treatment specified in the query. |
| 10 | 🟢 Trusted | ❌ 🔴 Rejected | 0.50 | This result is for a 'Day Skin Lightening' product, but it does not match the exact title of the queried product, which is specifically 'Skin Lightening Cream'. |

</details>

### 43. ⚠️ Carbon Theory Tea Tree Oil & Citric Acid Breakout Control Facial Purifying Tonic 8.45 fl oz
<details>
<summary><b>View Evaluation (TP: 5 | FP: 0 | FN: 2)</b></summary>

**Description:** *Facial Purifying Tonic, Breakout Control, Tea Tree Oil & Citric Acid*

**Ground Truth Trusted IDs:** `[1, 2, 3, 4, 7, 8, 9]`  
**LLM Predicted Trusted IDs:** `[2, 3, 4, 7, 8]`  

💡 **Global Pipeline Reasoning:** The evaluations focused on matching the brand 'Carbon Theory', the specific product name 'Tea Tree Oil & Citric Acid Breakout Control Facial Purifying Tonic', and ensuring that the ingredients were consistent. Results that did not include the full product name or brand were deemed untrusted.

| ID | Ground Truth | Prediction | Confidence | Decision Reasoning |
| :--- | :---: | :---: | :---: | :--- |
| 1 | 🟢 Trusted | ❌ 🔴 Rejected | 0.70 | This result does not specify the brand 'Carbon Theory' in the title, which is critical for trust. |
| 2 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result matches the exact product title and description, including the brand 'Carbon Theory' and the specific ingredients. |
| 3 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result includes the brand 'Carbon Theory' and matches the product description, confirming it is the same product. |
| 4 | 🟢 Trusted | 🟢 Trusted | 0.95 | This result matches the product title and description, including the brand 'Carbon Theory' and the specific ingredients. |
| 5 | 🔴 Rejected | 🔴 Rejected | 0.60 | This result does not include the specific 'Tea Tree Oil & Citric Acid' in the title, which is essential for matching. |
| 6 | 🔴 Rejected | 🔴 Rejected | 0.60 | This result does not include the specific 'Tea Tree Oil & Citric Acid' in the title, which is essential for matching. |
| 7 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result matches the exact product title and description, including the brand 'Carbon Theory' and the specific ingredients. |
| 8 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result includes the brand 'Carbon Theory' and matches the product description, confirming it is the same product. |
| 9 | 🟢 Trusted | ❌ 🔴 Rejected | 0.50 | This result does not specify the brand 'Carbon Theory' in the title, which is critical for trust. |
| 10 | 🔴 Rejected | 🔴 Rejected | 0.50 | This result does not include the specific 'Tea Tree Oil & Citric Acid' in the title, which is essential for matching. |

</details>

### 44. ⚠️ Standard Issue Waterproof 10 x 25 Binoculars
<details>
<summary><b>View Evaluation (TP: 3 | FP: 0 | FN: 1)</b></summary>

**Description:** *(None provided)*

**Ground Truth Trusted IDs:** `[1, 2, 3, 4]`  
**LLM Predicted Trusted IDs:** `[1, 2, 3]`  

💡 **Global Pipeline Reasoning:** All trusted results (1, 2, and 3) maintain the same brand 'Nocs Provisions' and match the product specifications of 10x25 waterproof binoculars. Result 4 lacks the brand identity, which is essential for trust.

| ID | Ground Truth | Prediction | Confidence | Decision Reasoning |
| :--- | :---: | :---: | :---: | :--- |
| 1 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result matches the product title and description closely, with the same brand and specifications (10x25, waterproof). |
| 2 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result also matches the product title and description, including the brand 'Nocs Provisions' and the specifications of being waterproof and 10x25. |
| 3 | 🟢 Trusted | 🟢 Trusted | 0.95 | This result is a perfect match for the product title and description, including the brand 'Nocs Provisions' and the exact specifications of 10 x 25 waterproof binoculars. |
| 4 | 🟢 Trusted | ❌ 🔴 Rejected | 0.50 | While this result mentions 'Standard Issue Waterproof Binoculars', it does not specify the brand 'Nocs Provisions', which is critical for trust. |

</details>

### 45. ✅ E Oxygen Cylinder Kit on Cart, 1630A-15E
<details>
<summary><b>View Evaluation (TP: 10 | FP: 0 | FN: 0)</b></summary>

**Description:** *Mada Medical 1602E Aluminum Oxygen Cylinder, 1335-15 Adjustable flow regulator (2-15 LPM), nasal cannula, and 370C Cart (Empty) is a complete oxygen therapy system that is ideal for home use.*

**Ground Truth Trusted IDs:** `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`  
**LLM Predicted Trusted IDs:** `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`  

💡 **Global Pipeline Reasoning:** All search results match the product title and description exactly, including the brand (Mada Medical) and all components (1602E Aluminum Oxygen Cylinder, 1335-15 Adjustable flow regulator, nasal cannula, and 370C Cart). There are no discrepancies in format, flavor, or variations.

| ID | Ground Truth | Prediction | Confidence | Decision Reasoning |
| :--- | :---: | :---: | :---: | :--- |
| 1 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the product title and description exactly, including the brand and components. |
| 2 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result is an exact match for the product title and description, including all components and the brand. |
| 3 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the product title and description, including the brand and all components listed. |
| 4 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the product title and description, including the brand and all components. |
| 5 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the product title and description, including the brand and all components. |
| 6 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the product title and description exactly, including the brand and components. |
| 7 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result is an exact match for the product title and description, including all components and the brand. |
| 8 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the product title and description, including the brand and all components listed. |
| 9 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the product title and description, including the brand and all components. |
| 10 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the product title and description, including the brand and all components. |

</details>

### 46. ⚠️ Rhythm P2-S3 Portable Concentrator
<details>
<summary><b>View Evaluation (TP: 6 | FP: 0 | FN: 2)</b></summary>

**Description:** *(None provided)*

**Ground Truth Trusted IDs:** `[1, 2, 3, 5, 6, 7, 8, 9]`  
**LLM Predicted Trusted IDs:** `[1, 2, 3, 5, 6, 8]`  

💡 **Global Pipeline Reasoning:** All trusted results (1, 2, 3, 5, 6, 8) match the exact product title 'Rhythm P2-S3 Portable Concentrator' and describe the same features. Untrusted results (4, 7, 9) either refer to different products or are not products for sale.

| ID | Ground Truth | Prediction | Confidence | Decision Reasoning |
| :--- | :---: | :---: | :---: | :--- |
| 1 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the exact product title and description, confirming it is the same Rhythm P2-S3 Portable Concentrator. |
| 2 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result includes the exact product name 'Rhythm P2-S3 Portable Oxygen Concentrator', which matches the queried product. |
| 3 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the product title and description, confirming it is the same Rhythm P2-S3 Portable Oxygen Concentrator. |
| 4 | 🔴 Rejected | 🔴 Rejected | 0.00 | This result refers to the 'Rhythm Healthcare P2 Portable Oxygen Concentrator', which is a different product and brand. |
| 5 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the exact product title and description, confirming it is the same Rhythm P2-S3 Portable Oxygen Concentrator. |
| 6 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the exact product title and description, confirming it is the same Rhythm P2-S3 Portable Concentrator. |
| 7 | 🟢 Trusted | ❌ 🔴 Rejected | 0.00 | This result is a user manual and does not represent a product for sale. |
| 8 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result matches the exact product title and description, confirming it is the same Rhythm P2-S3 Portable Oxygen Concentrator. |
| 9 | 🟢 Trusted | ❌ 🔴 Rejected | 0.00 | This result refers to the 'Lifestyle Rhythm P2-S3 Portable Oxygen Concentrator', which is a different product and brand. |

</details>

### 47. ✅ For Tots Apple White Grape
<details>
<summary><b>View Evaluation (TP: 8 | FP: 0 | FN: 0)</b></summary>

**Description:** *Juice Beverage, Apple White Grape*

**Ground Truth Trusted IDs:** `[1, 2, 3, 5, 6, 8, 9, 10]`  
**LLM Predicted Trusted IDs:** `[1, 2, 3, 5, 6, 8, 9, 10]`  

💡 **Global Pipeline Reasoning:** All trusted results are for 'Mott's for Tots' products that match the flavor 'Apple White Grape'. Results with '40% Less Sugar' are not trusted due to the significant difference in formulation.

| ID | Ground Truth | Prediction | Confidence | Decision Reasoning |
| :--- | :---: | :---: | :---: | :--- |
| 1 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result is for 'Mott's for Tots® Apple White Grape Flavored Juice Drink', which matches the brand and flavor of the queried product. |
| 2 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result is for 'Mott's For Tots Apple White Grape Fruit Juice', which matches the brand and flavor of the queried product. |
| 3 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result is for 'Mott's for Tots Apple White Grape Juice Beverage', which matches the brand and flavor of the queried product. |
| 4 | 🔴 Rejected | 🔴 Rejected | 0.50 | This result is for 'Motts Inc for Tots 40% Less Sugar Apple White Grape', which is a different product due to the '40% Less Sugar' variation. |
| 5 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result is for 'Mott's for Tots Apple White Grape Juice Drink', which matches the brand and flavor of the queried product. |
| 6 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result is for 'Mott's ® for Tots Apple White Grape', which matches the brand and flavor of the queried product. |
| 7 | 🔴 Rejected | 🔴 Rejected | 0.50 | This result is for 'Motts Inc for Tots 40% Less Sugar Apple White Grape', which is a different product due to the '40% Less Sugar' variation. |
| 8 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result is for 'Mott's for Tots Apple White Grape Juice', which matches the brand and flavor of the queried product. |
| 9 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result is for 'Mott's® for Tots® Apple White Grape Flavored Juice Drink', which matches the brand and flavor of the queried product. |
| 10 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result is for 'Mott's For Tots Apple White Grape Juice - 64 Fl Oz Bottle', which matches the brand and flavor of the queried product. |

</details>

### 48. ⚠️ Cocoa Krispies Cereal Bar 5 ea
<details>
<summary><b>View Evaluation (TP: 1 | FP: 1 | FN: 0)</b></summary>

**Description:** *Cereal Bar, Chewy, Chocolate*

**Ground Truth Trusted IDs:** `[2]`  
**LLM Predicted Trusted IDs:** `[2, 4]`  

💡 **Global Pipeline Reasoning:** The search results were evaluated based on brand identity, product format, and specific product variations. Trusted results were those that matched the brand 'Kellogg's' and the exact product type 'Cereal Bar', while granola bars and other brands were not trusted.

| ID | Ground Truth | Prediction | Confidence | Decision Reasoning |
| :--- | :---: | :---: | :---: | :--- |
| 1 | 🔴 Rejected | 🔴 Rejected | 0.70 | This result refers to a 'Cocoa Krispies Chocolate Chewy Granola Bar', which is a different product format (granola bar) compared to the 'Cocoa Krispies Cereal Bar'. |
| 2 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result is for 'Kelloggs Cocoa Krispies Chocolate Chewy Cereal Bar', which matches the brand and product format exactly. |
| 3 | 🔴 Rejected | 🔴 Rejected | 0.60 | This result is for a 'Cocoa Krispies Chewy Granola Bar Chocolate', which is a different product format (granola bar) compared to the 'Cocoa Krispies Cereal Bar'. |
| 4 | 🔴 Rejected | ❌ 🟢 Trusted | 0.90 | This result is for 'Kellogg's® Cocoa Krispies® Chewy Granola Bar Chocolate', which matches the brand and product format exactly. |
| 5 | 🔴 Rejected | 🔴 Rejected | 0.50 | This result is for a 'Cocoa Krispies Chewy Granola Bar Chocolate', which is a different product format (granola bar) compared to the 'Cocoa Krispies Cereal Bar'. |
| 6 | 🔴 Rejected | 🔴 Rejected | 0.40 | This result is for 'Kellogg's Cocoa Krispies Cereal', which is a different product type (cereal) and not a cereal bar. |
| 7 | 🔴 Rejected | 🔴 Rejected | 0.20 | This result is for 'Kashi Soft Baked Cereal Bars Cocoa', which is a different brand and product format. |
| 8 | 🔴 Rejected | 🔴 Rejected | 0.20 | This result is for 'Kashi Soft Baked Cereal Bars Cocoa', which is a different brand and product format. |
| 9 | 🔴 Rejected | 🔴 Rejected | 0.10 | This result is for 'Kraft Milk & Granola Bars', which is a different brand and product type. |
| 10 | 🔴 Rejected | 🔴 Rejected | 0.10 | This result is for 'Food Club Chewy Granola Bars Chocolate Chip', which is a different brand and product type. |

</details>

### 49. ⚠️ oaza cacao mocha cold brew coffee + electrolytes
<details>
<summary><b>View Evaluation (TP: 4 | FP: 0 | FN: 3)</b></summary>

**Description:** *coffee, cold brew, electrolytes, cacao mocha*

**Ground Truth Trusted IDs:** `[1, 2, 4, 5, 7, 8, 9]`  
**LLM Predicted Trusted IDs:** `[8, 1, 2, 7]`  

💡 **Global Pipeline Reasoning:** The evaluations focused on matching the brand 'Oaza', the product format of cold brew coffee, and the specific flavor of cacao mocha. Results that deviated from these criteria, such as generic products or different formulations (like '0 Sugar'), were not trusted.

| ID | Ground Truth | Prediction | Confidence | Decision Reasoning |
| :--- | :---: | :---: | :---: | :--- |
| 1 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result matches the brand 'Oaza' and the product format of cold brew coffee with cacao mocha flavor, making it a trusted match. |
| 2 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result is from the same brand 'Oaza' and matches the product description of cold brew coffee with cacao mocha and electrolytes. |
| 3 | 🔴 Rejected | 🔴 Rejected | 0.50 | While it has the same flavor, it is labeled as 'Oaza Performance Cold Brew', which may indicate a different formulation or purpose, thus not trusted. |
| 4 | 🟢 Trusted | ❌ 🔴 Rejected | 0.40 | This result does not include the brand 'Oaza' and is a generic product description, making it untrusted. |
| 5 | 🟢 Trusted | ❌ 🔴 Rejected | 0.40 | Similar to result 4, this is a generic product without the brand 'Oaza', thus not trusted. |
| 6 | 🔴 Rejected | 🔴 Rejected | 0.50 | This result specifies '0 Sugar', indicating a different formulation than the original product, which does not match the query. |
| 7 | 🟢 Trusted | 🟢 Trusted | 0.90 | This result matches the brand 'Oaza' and the product description of cold brew coffee with cacao mocha and electrolytes. |
| 8 | 🟢 Trusted | 🟢 Trusted | 1.00 | This result is an exact match for the queried product title and description, including the brand 'Oaza' and the specific flavor. |
| 9 | 🟢 Trusted | ❌ 🔴 Rejected | 0.40 | This is a generic product without the brand 'Oaza', thus not trusted. |
| 10 | 🔴 Rejected | 🔴 Rejected | 0.40 | This result indicates a combo pack, which is different from the single product queried, making it untrusted. |

</details>

### 50. ✅ Numi Tea 12 oz
<details>
<summary><b>View Evaluation (TP: 0 | FP: 0 | FN: 0)</b></summary>

**Description:** *Tea, Organic, Pure Black*

**Ground Truth Trusted IDs:** `[]`  
**LLM Predicted Trusted IDs:** `[]`  

💡 **Global Pipeline Reasoning:** All search results either represent different flavors, formats (loose vs liquid), or variations that do not match the exact product of 'Numi Tea 12 oz, Organic, Pure Black'. None of the results meet the critical matching rules for brand, format, or flavor.

| ID | Ground Truth | Prediction | Confidence | Decision Reasoning |
| :--- | :---: | :---: | :---: | :--- |
| 1 | 🔴 Rejected | 🔴 Rejected | 0.90 | This result is for 'Breakfast Blend' in loose format, which is different from the queried product that is a liquid tea. |
| 2 | 🔴 Rejected | 🔴 Rejected | 0.90 | This result is for 'Breakfast Blend' in a non-liquid format, which does not match the liquid format of the queried product. |
| 3 | 🔴 Rejected | 🔴 Rejected | 0.80 | This result is for a bottled tea with lemon, which is a different flavor and formulation than the pure black tea queried. |
| 4 | 🔴 Rejected | 🔴 Rejected | 0.80 | This result is for an iced tea product, which is a different format than the queried pure black tea. |
| 5 | 🔴 Rejected | 🔴 Rejected | 0.70 | This result is for 'Aged Earl Grey', which is a different flavor than the 'Pure Black' tea queried. |
| 6 | 🔴 Rejected | 🔴 Rejected | 0.90 | This result is for black tea bags, which is a different format than the liquid tea queried. |
| 7 | 🔴 Rejected | 🔴 Rejected | 0.80 | This result is for a bottled tea with lemon, which is a different flavor and formulation than the pure black tea queried. |
| 8 | 🔴 Rejected | 🔴 Rejected | 0.80 | This result is for an iced tea product, which is a different format than the queried pure black tea. |
| 9 | 🔴 Rejected | 🔴 Rejected | 0.90 | This result is for 'Breakfast Blend' in loose format, which is different from the queried product that is a liquid tea. |
| 10 | 🔴 Rejected | 🔴 Rejected | 0.70 | This result is for 'Black Lemon', which is a different flavor than the 'Pure Black' tea queried. |

</details>