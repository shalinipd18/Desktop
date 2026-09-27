print("Enter Numerator: ")
numn = int(input())
print("Enter Denominator: ")
numd = int(input())

if numn % numd == 0:
    print(numn, "is divisible by", numd)
else:
    print(numn, "is not divisible by", numd)