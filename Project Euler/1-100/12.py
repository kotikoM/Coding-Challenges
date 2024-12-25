import math

def count_divisors(n):
    count = 0
    sqrt_n = int(math.sqrt(n))
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            count += 2  # i and n / i
    if sqrt_n * sqrt_n == n:
        count -= 1  # Correct for a perfect square
    return count

def find_triangle_with_divisors(limit):
    n = 1
    triangle = 1
    while True:
        divisors = count_divisors(triangle)
        if divisors > limit:
            return triangle
        n += 1
        triangle += n  # Add the next natural number

result = find_triangle_with_divisors(500)
print("The first triangle number with over 500 divisors is:", result)
