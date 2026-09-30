total_rows = int(input("Rows: "))
if total_rows % 2 == 0:
    half_rows = int(total_rows / 2)
else:
    half_rows = int(total_rows / 2) + 1
spaces = half_rows - 1

for row in range(1, half_rows + 1):
    for col in range(1, spaces + 1):
        print(end=" ")
    spaces = spaces - 1
    digit = 1
    for col in range(2 * row - 1):
        print(end=str(digit))
        digit = digit + 1
    print()

spaces = 1

for row in range(1, half_rows):
    for col in range(1, spaces + 1):
        print(end=" ")
    spaces = spaces + 1
    digit = 1
    for col in range(1, 2 * (half_rows - row)):
        print(end=str(digit))
        digit = digit + 1
    print()