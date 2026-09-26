import json

with open('search_results_ground_truth_train.json', 'r') as f:
    data = json.load(f)

print(f"Total products: {len(data)}")
total_results = 0
total_trusted = 0
trusted_distribution = {}

for prod_id, prod_info in data.items():
    results = prod_info.get('search_results', {})
    trusted = prod_info.get('trusted_search_results', [])
    num_results = len(results)
    num_trusted = len(trusted)
    total_results += num_results
    total_trusted += num_trusted
    
    trusted_distribution[num_trusted] = trusted_distribution.get(num_trusted, 0) + 1

print(f"Total search results: {total_results}")
print(f"Total trusted search results: {total_trusted}")
print(f"Average search results per product: {total_results / len(data):.2f}")
print(f"Average trusted results per product: {total_trusted / len(data):.2f}")
print("Distribution of trusted results per product:")
for num_t, count in sorted(trusted_distribution.items()):
    print(f"  {num_t} trusted results: {count} products")
