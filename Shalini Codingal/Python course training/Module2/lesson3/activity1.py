total_chores = 4
original_count = total_chores
print(f"{original_count} chores today!\n")

completed_count = 0
chore_num = 1

while chore_num <= total_chores:

    if chore_num == 1: next_chore = "Make your bed"
    elif chore_num == 2: next_chore = "Feed the pet"
    elif chore_num == 3: next_chore = "Take out the trash"
    else: next_chore = "Wash the dishes"

    answer = input(f"Done: {next_chore}? (yes/no): ")

    if answer == "yes":
        completed_count += 1
        chore_num += 1
        print("Done!")
    else:
        print("Finish it first!")

    print("Remaining:", total_chores - completed_count)
    print()

print("== ALL DONE! ==\n")

print("Infinite loop demo...")
test_value = 0
safety_counter = 0
while test_value <= 0:
    print("Runs forever!")
    safety_counter += 1
    if safety_counter == 3:
        print("(Stopped on purpose)")
        break

print("\n== SUMMARY ==")
print("Assigned:", original_count)
print("Completed:", completed_count)
print("Remaining:", total_chores - completed_count)
print("=============")
