def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("FUNCTION CALCULATOR")

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose add, subtract, multiply or divide: ").lower()

    if operation == "add":
        print("Result:", add(num1, num2))
    elif operation == "subtract":
        print("Result:", subtract(num1, num2))
    elif operation == "multiply":
        print("Result:", multiply(num1, num2))
    elif operation == "divide":
        print("Result:", divide(num1, num2))
    else:
        print("Unknown operation.")

except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("Thank you for using the calculator!")