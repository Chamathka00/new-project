#Python code to generate random number
import random

random_number = random.randint(1, 10)
print("Random number:", random_number)

#Python code to calculates the sum of all even numbers from 1 to a specified number
def sum_of_evens(n):
    total = 0
    for i in range(2, n + 1, 2):
        total += i
    return total

# Replace 10 with the number up to which you want to calculate the sum of even numbers
number = 10
result = sum_of_evens(number)
print(f"The sum of even numbers from 2 to {number} is {result}")