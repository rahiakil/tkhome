import json

with open('search_results_ground_truth_train.json', 'r') as f:
    data = json.load(f)

for target in ["Labatt Ale 12 ea ", "Numi Tea 12 oz Tea, Organic, Pure Black"]:
    if target in data:
        print("="*60)
        print(f"PRODUCT: {target}")
        print(f"DESC: {data[target].get('product_description')}")
        print(f"TRUSTED: {data[target].get('trusted_search_results')}")
        print("RESULTS:")
        for k, v in data[target].get('search_results', {}).items():
            print(f"  {k}: {v[:300]}...")
