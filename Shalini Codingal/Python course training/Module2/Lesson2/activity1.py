limit = int(input("Enter the number whose sum you want to find: "))
total = 0

for num in range(1, limit + 1):
    total = total + num
    print("\nSum =", total)