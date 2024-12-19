with open("input", "r") as file:
    grid, moves = file.read().split("\n\n")
    grid = [list(line) for line in grid.splitlines()]
    grid.replace(".", "..")
    grid.replace("O", "[]")
    grid.replace("@", "@.")
    moves = moves.replace("\n", "")

x, y = 0, 0
for i, row in enumerate(grid):
    for j, cell in enumerate(row):
        if cell == "@":
            x, y = i, j
            break


def shift(x, y, dir):
    dx, dy = dir
    ex, ey = x + dx, y + dy  # Start from the adjacent cell

    # Check boundaries and find the stopping point for the box
    while 0 <= ex < len(grid) and 0 <= ey < len(grid[0]) and grid[ex][ey] != "#":
        if grid[ex][ey] == ".":  # Found an empty spot
            break
        ex += dx
        ey += dy

    # If out of bounds or blocked, return False
    if not (0 <= ex < len(grid) and 0 <= ey < len(grid[0])) or grid[ex][ey] == "#":
        return False

    # Shift boxes from stopping point back to the player
    while (ex, ey) != (x, y):
        grid[ex][ey] = "O"
        ex -= dx
        ey -= dy
        grid[ex][ey] = "."

    return True


def perform_move(move):
    global x, y
    # Map directions
    directions = {
        "^": (-1, 0),
        ">": (0, 1),
        "v": (1, 0),
        "<": (0, -1),
    }

    dx, dy = directions[move]
    nx, ny = x + dx, y + dy  # New player position

    # Check boundaries
    if not (0 <= nx < len(grid) and 0 <= ny < len(grid[0])):
        return

    # Move player
    if grid[nx][ny] == ".":
        grid[x][y] = "."
        x, y = nx, ny
        grid[x][y] = "@"
    elif grid[nx][ny] == "O":
        # Try shifting the box
        if shift(nx, ny, (dx, dy)):
            grid[x][y] = "."
            x, y = nx, ny
            grid[x][y] = "@"


# Simulate the moves
for move in moves:
    perform_move(move)

for row in grid:
    print("".join(row))

total = 0
for i, r in enumerate(grid):
    for j, c in enumerate(r):
        if c == 'O':
            total += 100 * i + j

print(total)


# Part 2
# top, bottom = open("input").read().split("\n\n")
#
# expansion = {"#": "##", "O": "[]", ".": "..", "@": "@."}
#
# grid = [list("".join(expansion[char] for char in line)) for line in top.splitlines()]
# moves = bottom.replace("\n", "")
#
# rows = len(grid)
# cols = len(grid[0])
#
# for r in range(rows):
#     for c in range(cols):
#         if grid[r][c] == "@":
#             break
#     else:
#         continue
#     break
#
# for move in moves:
#     dr = {"^": -1, "v": 1}.get(move, 0)
#     dc = {"<": -1, ">": 1}.get(move, 0)
#     targets = [(r, c)]
#     go = True
#     for cr, cc in targets:
#         nr = cr + dr
#         nc = cc + dc
#         if (nr, nc) in targets: continue
#         char = grid[nr][nc]
#         if char == "#":
#             go = False
#             break
#         if char == "[":
#             targets.append((nr, nc))
#             targets.append((nr, nc + 1))
#         if char == "]":
#             targets.append((nr, nc))
#             targets.append((nr, nc - 1))
#     if not go: continue
#     copy = [list(row) for row in grid]
#     grid[r][c] = "."
#     grid[r + dr][c + dc] = "@"
#     for br, bc in targets[1:]:
#         grid[br][bc] = "."
#     for br, bc in targets[1:]:
#         grid[br + dr][bc + dc] = copy[br][bc]
#     r += dr
#     c += dc
#
# print(sum(100 * r + c for r in range(rows) for c in range(cols) if grid[r][c] == "["))
