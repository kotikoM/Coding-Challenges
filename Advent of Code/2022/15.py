import re

interested_row = set()
target_row = 2_000_000

for line in open('input').read().splitlines():
    sx, sy, bx, by = map(int, re.findall(r'-?\d+', line))
    max_dist = abs(bx - sx) + abs(by - sy)

    if abs(sy - target_row) > max_dist:
        continue

    dx = max_dist - abs(sy - target_row)
    for x in range(sx - dx, sx + dx + 1):
        if x != bx:
            interested_row.add(x)

print(len(interested_row))
