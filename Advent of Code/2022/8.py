grid = [list(map(int, l)) for l in open('input').read().splitlines()]


def score(x, y):
    final_score = 1
    for dx, dy in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
        total = 0
        nx, ny = x, y
        while 0 <= nx + dx < len(grid) and 0 <= ny + dy < len(grid[0]):
            nx, ny = nx + dx, ny + dy
            if grid[nx][ny] >= grid[x][y]:
                total += 1
                break
            total += 1
        final_score *= total

    return final_score


scores = [score(x, y) for x in range(len(grid)) for y in range(len(grid[0]))]
print(max(scores))
