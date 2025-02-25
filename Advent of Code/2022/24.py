import math
from collections import deque

blizzards = tuple(set() for _ in range(4))

for x, line in enumerate(open('input').read().splitlines()[1:]):
    for y, item in enumerate(line[1:]):
        if item in "<>^v":
            blizzards["<>^v".find(item)].add((x, y))

queue = deque([(0, -1, 0, 0)])
seen = set()
target = [(x, y - 1), (-1, 0)]

lcm = x * y // math.gcd(x, y)

while queue:
    time, cx, cy, stage = queue.popleft()

    time += 1

    for dx, dy in ((0, 1), (0, -1), (-1, 0), (1, 0), (0, 0)):
        nx = cx + dx
        ny = cy + dy

        nstage = stage
        if (nx, ny) == target[stage % 2]:
            if stage == 2:
                print(time)
                exit(0)
            nstage += 1

        if (nx < 0 or ny < 0 or nx >= x or ny >= y) and (nx, ny) not in target:
            continue

        fail = False

        if (nx, ny) not in target:
            for i, tx, ty in ((0, 0, -1), (1, 0, 1), (2, -1, 0), (3, 1, 0)):
                if ((nx - tx * time) % x, (ny - ty * time) % y) in blizzards[i]:
                    fail = True
                    break

        if not fail:
            key = (nx, ny, nstage, time % lcm)

            if key in seen:
                continue

            seen.add(key)
            queue.append((time, nx, ny, nstage))
