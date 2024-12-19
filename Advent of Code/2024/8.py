from collections import defaultdict

with open('input', 'r') as file:
    lines = [list(line) for line in file.read().split('\n')]

empty = "."
rows = len(lines)
cols = len(lines[0])

# char - [positions]
nodes = defaultdict(list)
for i, r in enumerate(lines):
    for j, c in enumerate(r):
        if c != empty:
            nodes[c].append((i, j))

unique = set()
for pos in nodes.values():
    if len(pos) > 1:
        for i in range(len(pos)):
            for j in range(i + 1, len(pos)):
                x1, y1 = pos[i]
                x2, y2 = pos[j]
                dx, dy = (x1 - x2), (y1 - y2)  # pos[i] - pos[j]

                # puzzle 1 solution
                # antinodes = [(x2 - dx, y2 - dy), (x1 + dx, y1 + dy)]
                # for x, y in antinodes:
                #     if 0 <= x < rows and 0 <= y < cols:
                #         unique.add((x, y))
                #         if lines[x][y] == empty:
                #             lines[x][y] = "#"

                current_x, current_y = x1, y1
                while 0 <= current_x < rows and 0 <= current_y < cols:
                    unique.add((current_x, current_y))
                    if lines[current_x][current_y] == empty:
                        lines[current_x][current_y] = "#"
                    current_x += dx
                    current_y += dy

                current_x, current_y = x2, y2
                while 0 <= current_x < rows and 0 <= current_y < cols:
                    unique.add((current_x, current_y))
                    if lines[current_x][current_y] == empty:
                        lines[current_x][current_y] = "#"
                    current_x -= dx
                    current_y -= dy

for line in lines:
    print("".join(line))
print(f"Total unique antinodes: {len(unique)}")
