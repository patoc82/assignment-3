preferences = ["coffee", "tea", "coffee", "soda"]

counts = {}

for product in preferences:
    if product in counts:
        counts[product] = counts[product] + 1
    else:
        counts[product] = 1

total_responses = len(preferences)

print("--- Market Survey Results ---")

for product in counts:
    percentage = counts[product] / total_responses * 100
    print(product, ":", round(percentage, 1), "%")