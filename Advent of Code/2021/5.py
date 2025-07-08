grid = {}

for line in open('input').read().splitlines():
    l, r = line.split(" -> ")
    x1, y1 = map(int, l.split(","))
    x2, y2 = map(int, r.split(","))

    dx = (x2 - x1)
    dy = (y2 - y1)

    if dx != 0:
        dx = dx // abs(dx)
    if dy != 0:
        dy = dy // abs(dy)

    steps = max(abs(x2 - x1), abs(y2 - y1))

    for i in range(steps + 1):
        x = x1 + dx * i
        y = y1 + dy * i
        grid[(x, y)] = grid.get((x, y), 0) + 1

print(len([v for v in grid.values() if v > 1]))
