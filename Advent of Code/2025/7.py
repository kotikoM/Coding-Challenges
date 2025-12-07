from collections import deque

grid = [list(l) for l in open('input').read().splitlines()]
sx, sy = 0, ''.join(grid[0]).index('S')

split_count = 0
q = deque([(sx + 1, sy)])
visited = set()
while q:
    x, y = q.pop()
    if (x, y) in visited or x + 1 >= len(grid):
        continue
    visited.add((x, y))

    if grid[x][y] == '^':
        split_count += 1
        if y - 1 >= 0:
            q.append((x + 1, y - 1))
        if y + 1 < len(grid[0]):
            q.append((x + 1, y + 1))
    elif grid[x][y] == '.':
        q.append((x + 1, y))

print(split_count)
