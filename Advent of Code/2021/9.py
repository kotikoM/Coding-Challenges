from collections import deque
from math import prod

grid = [list(map(int, l.strip())) for l in open('input').read().split()]
dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

low_points = []
for x in range(len(grid)):
    for y in range(len(grid[x])):
        neighbors = []
        for dx, dy in dirs:
            if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[x]):
                neighbors.append(grid[x + dx][y + dy])

        if all(grid[x][y] < n for n in neighbors):
            low_points.append((x, y))

basin_sizes = []
while low_points:
    x, y = low_points.pop()
    q = deque([(x, y)])
    basin = set()

    while q:
        x, y = q.popleft()
        if (x, y) in basin or grid[x][y] == 9:
            continue

        basin.add((x, y))
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[nx]):
                q.append((nx, ny))

    basin_sizes.append(len(basin))

print(prod(sorted(basin_sizes)[-3:]))
