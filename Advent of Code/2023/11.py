grid = [list(l) for l in open('input').read().split()]

scale = 1_000_000

rows_to_expand = []
for i, r in enumerate(grid):
    if '#' not in r:
        rows_to_expand.append(i)

cols_to_expand = []
for c in range(len(grid[0])):
    if all(grid[r][c] == '.' for r in range(len(grid))):
        cols_to_expand.append(c)

galaxies = []
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == '#':
            galaxies.append((r, c))

new_rows = [rows_to_expand[0]]
for i in range(1, len(rows_to_expand)):
    new_rows.append(rows_to_expand[i] + i * (scale - 1))
rows_to_expand = new_rows

new_cols = [cols_to_expand[0]]
for i in range(1, len(cols_to_expand)):
    new_cols.append(cols_to_expand[i] + i * (scale - 1))
cols_to_expand = new_cols

for r in rows_to_expand:
    for i, (gr, gc) in enumerate(galaxies):
        if gr > r:
            galaxies[i] = (gr + (scale - 1), gc)
        else:
            galaxies[i] = (gr, gc)

for c in cols_to_expand:
    for i, (gr, gc) in enumerate(galaxies):
        if gc > c:
            galaxies[i] = (gr, gc + (scale - 1))
        else:
            galaxies[i] = (gr, gc)

total = 0
for i in range(0, len(galaxies) - 1):
    for j in range(i + 1, len(galaxies)):
        total += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])

print(total)
