visited = set()
dirs = {'R': (0, 1), 'L': (0, -1), 'D': (1, 0), 'U': (-1, 0)}

rope = [(0, 0) for _ in range(10)]

for line in open('input').read().splitlines():
    direction, steps = line.split()
    dx, dy = dirs[direction]

    for _ in range(int(steps)):
        hx, hy = rope[0]
        rope[0] = (hx + dx, hy + dy)

        for i in range(1, 10):
            hx, hy = rope[i - 1]
            tx, ty = rope[i]

            if max(abs(hx - tx), abs(hy - ty)) > 1:
                tx += (hx > tx) - (hx < tx)
                ty += (hy > ty) - (hy < ty)

            rope[i] = (tx, ty)

        visited.add(rope[9])

print(len(visited))
