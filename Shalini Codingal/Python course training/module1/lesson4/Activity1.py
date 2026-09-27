fields = [120, 85, 150, 95, 110]

total = sum(fields)
average = total / len(fields)

print("Total harvest      :", total, "kg")
print("Average per field  :", average, "kg")

def calculate_earnings(kg, rate):
    return kg * rate

price_per_kg = 15
earnings = calculate_earnings(total, price_per_kg)
print("Total earnings     : Rs.", earnings)

bag_size = 25
bags     = total // bag_size
leftover = total % bag_size

print("Full bags packed   :", bags)
print("Leftover grain     :", leftover, "kg")

last_year = 500
print("Better than last year?  :", total > last_year)
print("Same as last year?      :", total == last_year)
print("At least as good?       :", total >= last_year)

bonus_field   = 30
seed_reserve  = 15

total += bonus_field
print("After bonus crop   :", total, "kg")

total -= seed_reserve
print("After seed reserve :", total, "kg")

bags = total // bag_size
print("Final bags packed  :", bags)

print("\nHarvest breakdown by field:")
for i, kg in enumerate(fields, start=1):
    print(f"  Field {i}: {kg} kg")