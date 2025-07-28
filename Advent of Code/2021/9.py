grid = [list(map(int, l.strip())) for l in open('input').read().split()]

low_points = []
for x in range(len(grid)):
    for y in range(len(grid[x])):
        neighbors = []
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[x]):
                neighbors.append(grid[x + dx][y + dy])

        if all(grid[x][y] < n for n in neighbors):
            low_points.append((x, y))

print(sum(grid[x][y] + 1 for x, y in low_points))
