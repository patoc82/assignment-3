revenue = float(input("Enter initial annual revenue: $"))
growth_rate = float(input("Enter annual growth rate (%): "))

print("\n--- 10-Year Revenue Projection ---")
print("Year 0: $", round(revenue, 2))

for year in range(1, 11):
    revenue = revenue * (1 + growth_rate / 100)
    print("Year", year, ": $", round(revenue, 2))
