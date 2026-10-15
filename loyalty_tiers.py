
customers = {
    "Alice": 750,
    "Bob": 2500,
    "Carol": 6000,
    "David": 1200,
    "Emma": 400
}

bronze = 0
silver = 0
gold = 0

print("--- Customer Loyalty Tiers ---")

for customer in customers:
    purchases = customers[customer]

    if purchases < 1000:
        tier = "Bronze"
        bronze = bronze + 1
    elif purchases < 5000:
        tier = "Silver"
        silver = silver + 1
    else:
        tier = "Gold"
        gold = gold + 1

    print(customer, "- ", tier)

print("\n--- Tier Summary ---")
print("Bronze customers:", bronze)
print("Silver customers:", silver)
print("Gold customers:", gold)