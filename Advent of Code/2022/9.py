visited = set()
dirs = {'R': (0, 1), 'L': (0, -1), 'D': (1, 0), 'U': (-1, 0)}

head = (0, 0)
tail = (0, 0)

for line in open('input').read().splitlines():
    direction, steps = line.split()
    dx, dy = dirs[direction]

    for _ in range(int(steps)):
        hx, hy = head
        head = (hx + dx, hy + dy)

        tx, ty = tail
        hx, hy = head

        if max(abs(hx - tx), abs(hy - ty)) > 1:
            tx += (hx > tx) - (hx < tx)
            ty += (hy > ty) - (hy < ty)

        tail = (tx, ty)
        visited.add(tail)

print(len(visited))
