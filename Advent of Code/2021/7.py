positions = list(map(int, open('input').read().split(',')))
positions.sort()

def costs(pos, target):
    n = abs(pos - target)
    return n * (n + 1) // 2

min_fuel = float('inf')
min_value = positions[0]
for i in range(len(positions)):
    fuel = sum(costs(pos, positions[i]) for pos in positions)
    if fuel < min_fuel:
        min_fuel = fuel
        min_value = positions[i]

print(min_fuel)
