from math import factorial

# Find combination of 20 ups and 20 downs
res = factorial(40) // (factorial(20) * factorial(20))
print(res)
