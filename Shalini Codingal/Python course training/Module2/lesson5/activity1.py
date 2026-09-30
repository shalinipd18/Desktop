print("Half Pyramid:")
rows = int(input("Rows: "))

for row in range(rows):
    for col in range(row + 1):
        print("+ ", end="")
    print()