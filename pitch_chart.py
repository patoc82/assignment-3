revenues = [100, 200, 300, 400, 500]

print("--- Projected Revenue Growth ---")

for year in range(len(revenues)):
    bar = "#" * (year + 1) * 3
    print("Year", year + 1, ":", bar)