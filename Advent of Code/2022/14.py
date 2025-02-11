rocks = set()

abyss = 0

for line in open('input'):
    points = [tuple(map(int, p.split(","))) for p in line.strip().split(" -> ")]
    for (x1, y1), (x2, y2) in zip(points, points[1:]):
        x1, x2 = sorted([x1, x2])
        y1, y2 = sorted([y1, y2])
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                rocks.add((x, y))
                abyss = max(abyss, y + 1)

n = 0
while (500, 0) not in rocks:
    s = (500, 0)

    while True:
        x, y = s
        if y >= abyss:
            break
        if (x, y + 1) not in rocks:
            s = (x, y + 1)
            continue
        if (x - 1, y + 1) not in rocks:
            s = (x - 1, y + 1)
            continue
        if (x + 1, y + 1) not in rocks:
            s = (x + 1, y + 1)
            continue
        break
    rocks.add(s)
    n += 1

print(n)
