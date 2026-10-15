
prices = []

while True:
    price = float(input("Enter item price (or 0 to finish): $"))

    if price == 0:
        break
    elif price < 0:
        print("Price cannot be negative.")
    else:
        prices.append(price)

total = sum(prices)
number_of_items = len(prices)

if number_of_items > 0:
    average = total / number_of_items
else:
    average = 0

print("\n--- Checkout Summary ---")
print("Total purchase: $", round(total, 2))
print("Average item cost: $", round(average, 2))
print("Number of items:", number_of_items)
