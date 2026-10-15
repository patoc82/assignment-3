
import random

portfolio = {
    "AAPL": {"shares": 10, "price": 170},
    "TSLA": {"shares": 4, "price": 250},
    "AMZN": {"shares": 2, "price": 130}
}

for day in range(1, 6):
    total_value = 0

    for stock in portfolio:
        change = random.uniform(-0.05, 0.05)
        portfolio[stock]["price"] = portfolio[stock]["price"] * (1 + change)

        stock_value = (
            portfolio[stock]["shares"] * portfolio[stock]["price"]
        )
        total_value = total_value + stock_value

    print("Day", day, "- Portfolio Value: $", round(total_value, 2))