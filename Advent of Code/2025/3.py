total = 0
for l in open('input').read().splitlines():
    numbers = list(map(int, l))

    left = max(numbers[:-1])
    i = numbers.index(left)
    right = max(numbers[i + 1:])
    total += left * 10 + right

print(total)