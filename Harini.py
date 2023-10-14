def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Replace 5 with the number for which you want to calculate the factorial
number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}")