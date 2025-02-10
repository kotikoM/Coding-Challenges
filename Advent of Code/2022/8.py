grid = [list(map(int, l)) for l in open('input').read().splitlines()]


def is_visible(x, y):
    for dx, dy in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
        around_trees = []
        nx, ny = x, y
        while 0 <= nx + dx < len(grid) and 0 <= ny + dy < len(grid[0]):
            nx, ny = nx + dx, ny + dy
            around_trees.append(grid[nx][ny])

        if all(a < grid[x][y] for a in around_trees):
            return True

    return False


visible = 2 * len(grid) + 2 * len(grid[0]) - 4

for x in range(1, len(grid) - 1):
    for y in range(1, len(grid[0]) - 1):
        if is_visible(x, y):
            visible += 1

print(visible)
