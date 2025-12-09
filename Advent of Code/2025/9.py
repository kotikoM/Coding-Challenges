tiles = [list(map(int, l.split(','))) for l in open('input').read().splitlines()]

max_area = 0
for i in range(len(tiles) - 1):
    for j in range(i + 1, len(tiles)):
        a, b = tiles[i], tiles[j]
        area = (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)
        max_area = max(max_area, area)

print(max_area)
