from collections import deque

bricks = [list(map(int, line.replace('~', ',').split(','))) for line in open('input').read().splitlines()]
bricks.sort(key=lambda b: b[2])


def overlaps(a, b):
    return (max(a[0], b[0]) <= min(a[3], b[3]) and
            max(a[1], b[1]) <= min(a[4], b[4]))


for j, brick in enumerate(bricks):
    max_z = 1
    for under in bricks[:j]:
        if overlaps(brick, under):
            max_z = max(max_z, under[5] + 1)
    brick[5] -= brick[2] - max_z
    brick[2] = max_z

bricks.sort(key=lambda b: b[2])

k_supports_v = {i: set() for i in range(len(bricks))}
v_supports_k = {i: set() for i in range(len(bricks))}

for i, higher in enumerate(bricks):
    for j, lower in enumerate(bricks[:i]):
        if overlaps(lower, higher) and higher[2] == lower[5] + 1:
            k_supports_v[j].add(i)
            v_supports_k[i].add(j)

total = 0
for i in range(len(bricks)):
    q = deque(j for j in k_supports_v[i] if len(v_supports_k[j]) == 1)
    falling = set(q)
    falling.add(i)

    while q:
        j = q.popleft()
        for k in k_supports_v[j] - falling:
            if v_supports_k[k] <= falling:
                q.append(k)
                falling.add(k)

    total += len(falling) - 1

print(total)
