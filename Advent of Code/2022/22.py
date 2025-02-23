import re

grid = []
done = False

for line in open('input'):
    line = line[:-1]
    if line == "":
        done = True

    if done:
        sequence = line
    else:
        grid.append(line)

width = max(map(len, grid))
grid = [line + " " * (width - len(line)) for line in grid]

x, y = 0, 0
dx, dy = 0, 1

while grid[x][y] != ".":
    y += 1

for steps, dir in re.findall(r"(\d+)([RL]?)", sequence):
    steps = int(steps)
    for _ in range(steps):
        nx = x
        ny = y
        while True:
            nx = (nx + dx) % len(grid)
            ny = (ny + dy) % len(grid[0])
            if grid[nx][ny] != " ":
                break

        if grid[nx][ny] == "#":
            break

        x = nx
        y = ny

    if dir == "R":
        dx, dy = dy, -dx
    elif dir == "L":
        dx, dy = -dy, dx

if dx == 0:
    if dy == 1:
        k = 0
    else:
        k = 2
else:
    if dx == 1:
        k = 1
    else:
        k = 3

print(1000 * (x + 1) + 4 * (y + 1) + k)
