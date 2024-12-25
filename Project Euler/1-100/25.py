fib = [1, 1]

while len(str(fib[-1])) < 1000:
    fib.append(fib[-2] + fib[-1])

print(len(fib))
