print("Enter Marks Obtained in 5 Subjects:")

markOne = int(input())
markTwo = int(input())
markThree = int(input())
markFour = int(input())
markFive = int(input())

tot = markOne + markTwo + markThree + markFour + markFive
avg = int(tot / 5)

validRange = range(0, 101)

if avg not in validRange:
    print("Invalid Input")

elif avg in range(91, 101):
    print("Grade A1")

elif avg in range(81, 91):
    print("Grade A2")

elif avg in range(71, 81):
    print("Grade B1")

elif avg in range(61, 71):
    print("Grade B2")

elif avg in range(51, 61):
    print("Grade C1")

elif avg in range(41, 51):
    print("Grade C2")

elif avg in range(33, 41):
    print("Grade D")

elif avg in range(21, 33):
    print("Grade E1")

elif avg in range(0, 21):
    print("Grade E2")
