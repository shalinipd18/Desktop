
def factorial(x):
    '''This is a recursive function to find the factorial of an integer.'''

    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)

print(factorial.__doc__)
print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(5))
print(factorial(10))