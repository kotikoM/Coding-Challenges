with open('input', 'r') as file:
    lines = [list(line) for line in file.read().split('\n')]

guard = "^"
step = "X"
obs = "#"

x, y = 0, 0
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == guard:
            x, y = i, j

dir = 0
order = ["up", "right", "down", "left"]
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
rows = len(lines)
cols = len(lines[0])
total = 1
moves = set()

while 0 <= x < rows and 0 <= y < cols:
    if lines[x][y] == obs:
        x -= dirs[dir][0]
        y -= dirs[dir][1]
        dir = (dir + 1) % 4
    else:
        # Unvisited cell
        if lines[x][y] == ".":
            total += 1
        moves.add((x, y, dir))
        lines[x][y] = step
        x += dirs[dir][0]
        y += dirs[dir][1]

print(moves)
print(len(moves))
print(f"Total unique steps: {total}")
for line in lines:
    print(''.join(line))
