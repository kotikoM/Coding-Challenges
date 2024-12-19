from collections import deque

with open("input", "r") as file:
    tuples = file.read().split("\n")

    corrupted = []
    for s in tuples:
        x, y = s.split(",")
        corrupted.append((int(x), int(y)))

size = 71
fell = 1024
grid = [['.' for _ in range(size)] for _ in range(size)]
for x, y in corrupted[0:fell]:
    grid[y][x] = "#"
for r in grid:
    print(''.join(r))

q = deque(())
visited = set()
q.append((0, 0, 0))

fell = 1024
while True:
    size = 71
    grid = [['.' for _ in range(size)] for _ in range(size)]
    for x, y in corrupted[0:fell]:
        grid[y][x] = "#"
    # for r in grid:
    #     print(''.join(r))
    print(fell)

    q = deque(())
    visited = set()
    q.append((0, 0, 0))

    found = False
    while q:
        s, r, c = q.popleft()
        if r == len(grid) - 1 and c == len(grid[0]) - 1:
            print(f'Found exit in {s} steps')
            found = True
            break

        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != "#" and (nr, nc) not in visited:
                visited.add((nr, nc))
                q.append((s + 1, nr, nc))

    if found:
        fell += 1
    else:
        print(f"{fell}'th falling block made non-reachable exit")
        print(corrupted[fell - 1])
        break
