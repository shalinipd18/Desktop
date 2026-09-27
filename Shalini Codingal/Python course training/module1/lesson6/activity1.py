print("=== Smart School Day Planner ===")
print("Answer 3 quick questions and I will plan your day!\n")

current_day    = input("What day is it? (Monday to Sunday): ").strip().capitalize()
sky_condition  = input("What is the weather? (sunny / rainy / cloudy): ").strip().lower()
task_done      = input("Is your homework done? (yes / no): ").strip().lower()

print()
print(f"=== Your Plan for {current_day} ===")
print("-" * 35)

if current_day in ("Saturday", "Sunday"):
    print("Day type    : Weekend - enjoy your free time!")
elif current_day == "Monday":
    print("Day type    : First day of the week. Pack your weekly planner.")
elif current_day == "Friday":
    print("Day type    : Last school day. Return library books today.")
elif current_day in ("Tuesday", "Wednesday", "Thursday"):
    print("Day type    : Regular school day. Stay focused!")
else:
    print("Day type    : Day not recognised. Please check the spelling.")

if sky_condition == "sunny" and task_done == "yes":
    print("After school: Head to the park - great weather and homework is done!")

if sky_condition == "rainy" or sky_condition == "cloudy":
    print("Weather tip : Pack your umbrella - it may get wet outside.")

if not (task_done == "yes"):
    print("Homework    : Not done yet. Finish it before going out!")

if sky_condition == "rainy" and not (task_done == "yes"):
    print("Best plan   : Stay in, finish homework, then watch your favourite show.")
elif sky_condition == "sunny" and task_done == "yes" and not (current_day in ("Saturday", "Sunday")):
    print("Best plan   : All set for a great school day - you are prepared!")
elif current_day in ("Saturday", "Sunday") and sky_condition == "sunny":
    print("Best plan   : Perfect weekend weather - head outside and have fun!")
else:
    print("Best plan   : Take it one step at a time - you have got this!")

print()
print("Plan complete! Have a wonderful day!")