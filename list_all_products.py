import json

with open('search_results_ground_truth_train.json', 'r') as f:
    data = json.load(f)

print("List of all products in the JSON:")
for i, title in enumerate(data.keys()):
    info = data[title]
    trusted = info.get('trusted_search_results', [])
    print(f"{i+1:2d}. {title[:60]} -> {len(trusted)} trusted results: {trusted}")
