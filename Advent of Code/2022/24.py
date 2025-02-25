import math
from collections import deque

blizzards = tuple(set() for _ in range(4))

for x, line in enumerate(open('input').read().splitlines()[1:]):
    for y, item in enumerate(line[1:]):
        if item in "<>^v":
            blizzards["<>^v".find(item)].add((x, y))

queue = deque([(0, -1, 0)])
seen = set()
target = (x, y - 1)

lcm = x * y // math.gcd(x, y)

while queue:
    time, cx, cy = queue.popleft()

    time += 1

    for dx, dy in ((0, 1), (0, -1), (-1, 0), (1, 0), (0, 0)):
        nx = cx + dx
        ny = cy + dy

        if (nx, ny) == target:
            print(time)
            exit(0)

        if (nx < 0 or ny < 0 or nx >= x or ny >= y) and not (nx, ny) == (-1, 0):
            continue

        fail = False

        if (nx, ny) != (-1, 0):
            for i, tx, ty in ((0, 0, -1), (1, 0, 1), (2, -1, 0), (3, 1, 0)):
                if ((nx - tx * time) % x, (ny - ty * time) % y) in blizzards[i]:
                    fail = True
                    break

        if not fail:
            key = (nx, ny, time % lcm)

            if key in seen:
                continue

            seen.add(key)
            queue.append((time, nx, ny))