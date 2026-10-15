
expenses = {
    "Travel": [500, 200],
    "Meals": [40, 60, 30],
    "Supplies": [100]
}

grand_total = 0

print("--- Expense Summary Report ---")

for category in expenses:
    category_total = 0

    for amount in expenses[category]:
        category_total = category_total + amount

    print(category, ": $", round(category_total, 2))
    grand_total = grand_total + category_total

print("------------------------------")
print("Grand Total: $", round(grand_total, 2))