text = input("Please enter your own String : ")

reversed_text = ''

for char in text:
    reversed_text = char + reversed_text

print("\nThe Original String = ", text)
print("The Reversed String = ", reversed_text)