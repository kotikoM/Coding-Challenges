from collections import deque

grid = [list(l) for l in open('input').read().splitlines()]

sx, sy, ex, ey = 0, 0, 0, 0
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y] == 'S':
            sx, sy = x, y
            grid[x][y] = 'a'

        elif grid[x][y] == 'E':
            ex, ey = x, y
            grid[x][y] = 'z'

q = deque([(sx, sy, 0)])
visited = {(sx, sy)}
while q:
    x, y, s = q.popleft()
    for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx, ny) not in visited and ord(grid[nx][ny]) - ord(grid[x][y]) <= 1:
            if nx == ex and ny == ey:
                print(s + 1)
                exit(0)
            visited.add((nx, ny))
            q.append((nx, ny, s + 1))
