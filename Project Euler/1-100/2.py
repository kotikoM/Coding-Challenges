def sum_even_fibonacci(limit):
    fib = [1, 2]
    even_sum = 2  # Include the second term since it is even

    while True:
        next_term = fib[-1] + fib[-2]

        if next_term > limit:
            break

        fib.append(next_term)
        if next_term % 2 == 0:
            even_sum += next_term

    return even_sum


limit = 4_000_000
result = sum_even_fibonacci(limit)
print(f"Sum of even Fibonacci numbers up to {limit}: {result}")
