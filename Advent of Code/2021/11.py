grid = [list(map(int, line)) for line in open('input').read().splitlines()]

def step(grid):
    flashes = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j] += 1

    flashed = set()
    while True:
        new_flash = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 9 and (i, j) not in flashed:
                    flashed.add((i, j))
                    flashes += 1
                    new_flash = True
                    for di in [-1, 0, 1]:
                        for dj in [-1, 0, 1]:
                            if di == 0 and dj == 0:
                                continue
                            ni, nj = i + di, j + dj
                            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                                grid[ni][nj] += 1
        if not new_flash:
            break

    for i, j in flashed:
        grid[i][j] = 0

    return flashes

total_flashes = 0
for _ in range(100):
    total_flashes += step(grid)

print(total_flashes)
