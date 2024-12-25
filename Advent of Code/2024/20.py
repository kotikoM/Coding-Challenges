with open("input", "r") as file:
    grid = file.read().split("\n")
    grid = [list(i) for i in grid]

rows = len(grid)
cols = len(grid[0])

x, y, = 0, 0
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == "S":
            x = i
            y = j
            break

dists = [[-1] * cols for _ in range(rows)]
dists[x][y] = 0

while grid[x][y] != "E":
    for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != "#" and dists[nx][ny] == -1:
            dists[nx][ny] = dists[x][y] + 1
            x, y = nx, ny
            break

count = 0
for x in range(rows):
    for y in range(cols):
        if grid[x][y] != "#":
            for radius in range(2, 21):
                for dx in range(radius + 1):
                    dy = radius - dx

                    for nx, ny in {(x + dx, y + dy), (x - dx, y + dy), (x + dx, y - dy), (x - dx, y - dy)}:
                        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != "#":
                            if dists[x][y] - dists[nx][ny] >= 100 + radius:
                                count += 1

for row in dists:
    print(*row, sep="\t")
print(count)
