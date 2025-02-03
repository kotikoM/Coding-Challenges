from collections import deque

grid = open('input').read().splitlines()
assert len(grid) == len(grid[0])


def fill(sx, sy, ss):
    ans = set()
    seen = {(sx, sy)}
    q = deque([(sx, sy, ss)])

    while q:
        x, y, s = q.popleft()

        if s % 2 == 0:
            ans.add((x, y))
        if s == 0:
            continue

        for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]) or grid[nx][ny] == "#" or (nx, ny) in seen:
                continue
            seen.add((nx, ny))
            q.append((nx, ny, s - 1))

    return len(ans)


x, y = -1, -1
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'S':
            x, y = i, j
            break
    else:
        continue

size = len(grid)
steps = 26501365

assert x == y == size // 2
assert steps % size == size // 2

grid_width = steps // size - 1

odd = (grid_width // 2 * 2 + 1) ** 2
even = ((grid_width + 1) // 2 * 2) ** 2

odd_points = fill(x, y, size * 2 + 1)
even_points = fill(x, y, size * 2)

corner_t = fill(size - 1, y, size - 1)
corner_r = fill(x, 0, size - 1)
corner_b = fill(0, y, size - 1)
corner_l = fill(x, size - 1, size - 1)

small_tr = fill(size - 1, 0, size // 2 - 1)
small_tl = fill(size - 1, size - 1, size // 2 - 1)
small_br = fill(0, 0, size // 2 - 1)
small_bl = fill(0, size - 1, size // 2 - 1)

large_tr = fill(size - 1, 0, size * 3 // 2 - 1)
large_tl = fill(size - 1, size - 1, size * 3 // 2 - 1)
large_br = fill(0, 0, size * 3 // 2 - 1)
large_bl = fill(0, size - 1, size * 3 // 2 - 1)

print(
    odd * odd_points +
    even * even_points +
    corner_t + corner_r + corner_b + corner_l +
    (grid_width + 1) * (small_tr + small_tl + small_br + small_bl) +
    grid_width * (large_tr + large_tl + large_br + large_bl)
)
