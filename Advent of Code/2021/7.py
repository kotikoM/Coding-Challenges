positions = list(map(int, open('input').read().split(',')))
positions.sort()

n = len(positions)
if n % 2 == 1:
    median = positions[n // 2]
else:
    median = (positions[n // 2 - 1] + positions[n // 2]) // 2

fuel = sum(abs(p - median) for p in positions)

print(fuel)
