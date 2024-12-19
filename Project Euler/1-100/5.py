import math
from functools import reduce

# Function to calculate the LCM of two numbers
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

# Find the LCM of all numbers from 1 to 10
numbers = range(1, 21)
result = reduce(lcm, numbers)

print(f"The smallest number divisible by all numbers from 1 to 10 is: {result}")
