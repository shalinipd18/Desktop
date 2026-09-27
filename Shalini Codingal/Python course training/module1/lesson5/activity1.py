temperature = 15

if temperature <15:
    outfit = "jacket"
    print("It is cold today.")
    print("Wear a", outfit)
else:
    outfit = "t-shirt"
    print("It is warm today.")
    print("Wear a", outfit)

is_raining = input("Is it raining today? (yes/no): ")

if is_raining == "yes":
    print("Bring an umbrella!")

wind_speed = int(input("Enter the wind speed in km/h: "))

if wind_speed > 40:
    needs_windbreaker = "yes"
    print("It is windy today.")
    print("Wear a windbreaker over your", outfit)
else:
    needs_windbreaker = "no"
    print("It is calm today.")
    print("No windbreaker needed over your", outfit)

has_puddles = input("Are there puddles on the ground? (yes/no): ")

if has_puddles == "yes":
    shoes = "boots"
    print("The ground is wet.")
    print("Wear", shoes)
else:
    shoes = "sneakers"
    print("The ground is dry.")
    print("Wear", shoes)

print("")
print("Weather check complete!")

print("===== WEATHER OUTFIT PICKER =====")
print("Temperature:", temperature)
print("Outfit Chosen:", outfit)
print("Raining:", is_raining)
print("Windbreaker Needed:", needs_windbreaker)
print("Shoes Chosen:", shoes)
print("===================================")