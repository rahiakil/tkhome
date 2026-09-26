import json

with open('search_results_ground_truth_train.json', 'r') as f:
    data = json.load(f)

# Let's print products that have different numbers of trusted results
for count_to_find in [0, 3, 4, 9]:
    for title, info in data.items():
        trusted = info.get('trusted_search_results', [])
        if len(trusted) == count_to_find:
            print("="*60)
            print(f"PRODUCT TITLE: {title}")
            print(f"PRODUCT DESC: {info.get('product_description')}")
            print(f"TRUSTED INDICES: {trusted}")
            print("SEARCH RESULTS:")
            for idx, res in info.get('search_results', {}).items():
                is_t = int(idx) in trusted
                prefix = "[TRUSTED]" if is_t else "[NOT TRUST]"
                # Print first 200 chars of result
                res_clean = res.replace('\n', ' | ')
                print(f"  {idx} {prefix}: {res_clean[:180]}...")
            break
