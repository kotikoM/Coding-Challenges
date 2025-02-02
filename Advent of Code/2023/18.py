dig_plan = []
dirs_code = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}
for l in open('input'):
    _, _, hex = l.strip().split(' ')
    dir = dirs_code[hex[-2]]
    dist = int(hex[2:-2], 16)
    dig_plan.append((dir, dist, hex))

b = 0
trench = [(0, 0)]
dirs = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}
for dir, dist, _ in dig_plan:
    dx, dy = dirs[dir]
    dist = int(dist)
    x, y = trench[-1]
    b += dist
    trench.append((x + dx * dist, y + dy * dist))

area = abs(sum(trench[i][0] * (trench[i - 1][1] - trench[(i + 1) % len(trench)][1]) for i in range(len(trench)))) // 2
i = area - b // 2 + 1
print(b + i)
