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
        cdx = dx
        cdy = dy
        nx = x + dx
        ny = y + dy
        if nx < 0 and 50 <= ny < 100 and dx == -1:
            dx, dy = 0, 1
            nx, ny = ny + 100, 0
        elif ny < 0 and 150 <= nx < 200 and dy == -1:
            dx, dy = 1, 0
            nx, ny = 0, nx - 100
        elif nx < 0 and 100 <= ny < 150 and dx == -1:
            nx, ny = 199, ny - 100
        elif nx >= 200 and 0 <= ny < 50 and dx == 1:
            nx, ny = 0, ny + 100
        elif ny >= 150 and 0 <= nx < 50 and dy == 1:
            dy = -1
            nx, ny = 149 - nx, 99
        elif ny == 100 and 100 <= nx < 150 and dy == 1:
            dy = -1
            nx, ny = 149 - nx, 149
        elif nx == 50 and 100 <= ny < 150 and dx == 1:
            dx, dy = 0, -1
            nx, ny = ny - 50, 99
        elif ny == 100 and 50 <= nx < 100 and dy == 1:
            dx, dy = -1, 0
            nx, ny = 49, nx + 50
        elif nx == 150 and 50 <= ny < 100 and dx == 1:
            dx, dy = 0, -1
            nx, ny = ny + 100, 49
        elif ny == 50 and 150 <= nx < 200 and dy == 1:
            dx, dy = -1, 0
            nx, ny = 149, nx - 100
        elif nx == 99 and 0 <= ny < 50 and dx == -1:
            dx, dy = 0, 1
            nx, ny = ny + 50, 50
        elif ny == 49 and 50 <= nx < 100 and dy == -1:
            dx, dy = 1, 0
            nx, ny = 100, nx - 50
        elif ny == 49 and 0 <= nx < 50 and dy == -1:
            dy = 1
            nx, ny = 149 - nx, 0
        elif ny < 0 and 100 <= nx < 150 and dy == -1:
            dy = 1
            nx, ny = 149 - nx, 50
        if grid[nx][ny] == "#":
            dx = cdx
            dy = cdy
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