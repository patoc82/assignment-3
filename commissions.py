sales = {
    "Alice": 5000,
    "Bob": 7000,
    "Carol": 3000
}

def calculate_commission(sales_amount):
    return sales_amount * 0.10

print("--- Sales Commission Leaderboard ---")

for employee in sales:
    commission = calculate_commission(sales[employee])
    print(employee, "- Commission: $", round(commission, 2))
