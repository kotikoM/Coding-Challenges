import re

lines = [list(map(int, re.findall(r"-?\d+", line))) for line in open('input')]

target_row = 20

for Y in range(target_row + 1):
    intervals = []

    for sx, sy, bx, by in lines:
        max_dist = abs(sx - bx) + abs(sy - by)
        overlap = max_dist - abs(sy - Y)

        if overlap < 0:
            continue

        lx = sx - overlap
        hx = sx + overlap

        intervals.append((lx, hx))

    intervals.sort()

    q = []
    for lo, hi in intervals:
        if not q:
            q.append([lo, hi])
            continue

        qlo, qhi = q[-1]

        if lo > qhi + 1:
            q.append([lo, hi])
            continue

        q[-1][1] = max(qhi, hi)

    x = 0
    for lo, hi in q:
        if x < lo:
            print(x * 4000000 + Y)
            exit(0)
        x = max(x, hi + 1)
        if x > target_row:
            break
