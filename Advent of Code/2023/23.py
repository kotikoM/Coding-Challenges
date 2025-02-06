from collections import deque

grid = [list(l) for l in open('input').read().splitlines()]

hike_trails = []
ex, ey = len(grid) - 1, grid[-1].index('.')

q = deque([([], 0, 0, grid[0].index('.'))]) # visited, steps, x, y

while q:
    visited, steps, x, y = q.popleft()

    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    valid_next_step = {(-1, 0): '^.', (0, 1): '>.', (1, 0): 'v.', (0, -1): '<.'}

    if x == ex and y == ey:
        hike_trails.append(steps)
        continue

    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] in valid_next_step[(dx, dy)] and (nx, ny) not in visited:
            new = visited.copy()
            new.append((nx, ny))
            q.append((new, steps + 1, nx, ny))


print(max(hike_trails))
