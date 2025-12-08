from itertools import combinations
from math import prod


def distance(a, b):
    return ((a.x - b.x) ** 2 + (a.y - b.y) ** 2 + (a.z - b.z) ** 2) ** 0.5


class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.connections = []

    def make_connection(self, other_box):
        if other_box not in self.connections:
            self.connections.append(other_box)
        if self not in other_box.connections:
            other_box.connections.append(self)

    def __repr__(self):
        return f"Box({self.x}, {self.y}, {self.z})"

    @property
    def connected_to(self):
        return [f"({b.x},{b.y},{b.z})" for b in self.connections]


boxes = [Box(*list(map(int, l.split(',')))) for l in open('input').read().splitlines()]

pairs = [(a, b, distance(a, b)) for a, b in combinations(boxes, 2)]
pairs.sort(key=lambda x: x[2])

for i in range(1000):
    a, b, _ = pairs[i]
    a.make_connection(b)

for b in boxes:
    visited = set()
    stack = [b]
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            for neighbor in current.connections:
                stack.append(neighbor)

    b.connections = list(visited - {b})

groups = []
visited = set()
for b in boxes:
    if b in visited: continue
    visited.add(b)
    for c in b.connections:
        visited.add(c)
    groups.append(1 + len(b.connections))

print(prod(sorted(groups, reverse=True)[:3]))
