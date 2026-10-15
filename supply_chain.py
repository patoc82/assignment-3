
warehouses = [
    {
        "name": "Warehouse A",
        "inventory": {"apples": 100, "bananas": 150}
    },
    {
        "name": "Warehouse B",
        "inventory": {"apples": 200, "bananas": 100}
    }
]

total_apples = 0
total_bananas = 0

for warehouse in warehouses:
    print(warehouse["name"])

    for product in warehouse["inventory"]:
        quantity = warehouse["inventory"][product]
        print(product, ":", quantity)

        if product == "apples":
            total_apples = total_apples + quantity
        elif product == "bananas":
            total_bananas = total_bananas + quantity

print("\n--- Total Supply Chain Inventory ---")
print("Apples:", total_apples)
print("Bananas:", total_bananas)