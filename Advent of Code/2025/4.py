grid = [list(line) for line in open('input').read().split('\n')]

accessible_rolls = 0
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y] != '@':
            continue

        neighbors = 0
        for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            nx, ny = x + dx, y + dy
            if -1 < nx < len(grid) and -1 < ny < len(grid[0]) and grid[nx][ny] == '@':
                neighbors += 1

        if neighbors < 4:
            accessible_rolls += 1

print(accessible_rolls)
