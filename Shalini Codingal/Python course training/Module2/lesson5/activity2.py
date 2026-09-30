rows = int(input("Rows: "))
number = 1

print("Floyd's Triangle")

for row in range(1, rows + 1):
    for col in range(1, row + 1):
        print(number, end='  ')
        number = number + 1
    print()