from functools import lru_cache


@lru_cache(maxsize=None)
def dfs(r, c):
    if r >= len(grid) or c < 0 or c >= len(grid[0]):
        return 1

    cell = grid[r][c]

    if cell == '.':
        return dfs(r + 1, c)
    elif cell == '^':
        left = dfs(r + 1, c - 1)
        right = dfs(r + 1, c + 1)
        return left + right
    else:
        return dfs(r + 1, c)


grid = [list(line.strip()) for line in open('input')]

sx, sy = 0, ''.join(grid[0]).index('S')
print(dfs(sx + 1, sy))
