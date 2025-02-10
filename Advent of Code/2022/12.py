from collections import deque

grid = [list(l) for l in open('input').read().splitlines()]

A = []
ex, ey = 0, 0
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y] == 'S':
            grid[x][y] = 'a'
            A.append((x, y))
        elif grid[x][y] == 'a':
            A.append((x, y))
        elif grid[x][y] == 'E':
            ex, ey = x, y
            grid[x][y] = 'z'


def bfs(sx, sy):
    q = deque([(sx, sy, 0)])
    visited = {(sx, sy)}

    while q:
        x, y, s = q.popleft()
        for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx, ny) not in visited and ord(grid[nx][ny]) - ord(grid[x][y]) <= 1:
                if nx == ex and ny == ey:
                    return s + 1

                visited.add((nx, ny))
                q.append((nx, ny, s + 1))

    return None


min_path = float('inf')
for sx, sy in A:
    path = bfs(sx, sy)
    if path and path < min_path:
        min_path = path
print(min_path)

