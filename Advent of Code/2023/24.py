class HailStone:
    def __init__(self, x, y, z, dx, dy, dz):
        self.x = x
        self.y = y
        self.z = z
        self.dx = dx
        self.dy = dy
        self.dz = dz

        # y = kx + b
        self.k = dy / dx
        self.b = y - self.k * x

    def __repr__(self):
        return f'({self.k}, {self.b})'


def find_intersection_point(a, b):
    x = (b.b - a.b) / (a.k - b.k)
    y = a.k * x + a.b
    return x, y


def in_past(a, x, y):
    return ((a.x - x) / a.dx) > 0 and ((a.y - y) / a.dy) > 0


hailStones = [HailStone(*map(int, line.replace(' @', ',').split(', '))) for line in open('input')]
print(hailStones)

lower_limit = 200000000000000
higher_limit = 400000000000000
intersections = []
for i in range(len(hailStones) - 1):
    for j in range(i + 1, len(hailStones)):
        a = hailStones[i]
        b = hailStones[j]
        if a.k == b.k: continue

        x, y = find_intersection_point(a, b)
        print(x, y)
        if not (lower_limit <= x <= higher_limit and lower_limit <= y <= higher_limit):
            print('not inside limits')
            continue
        print('inside limits')

        if in_past(a, x, y) or in_past(b, x, y):
            print('in the past')
            continue

        intersections.append((x, y))

print(intersections)
print(len(intersections))
