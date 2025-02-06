grid = open('input').read().splitlines()

start = (0, grid[0].index("."))
end = (len(grid) - 1, grid[-1].index("."))

points = [start, end]
for x, row in enumerate(grid):
    for y, ch in enumerate(row):
        if ch == "#":
            continue

        neighbors = 0
        for nr, nc in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != "#":
                neighbors += 1
        if neighbors >= 3:
            points.append((x, y))

distances_graph = {pt: {} for pt in points}
for sx, sy in points:
    stack = [(0, sx, sy)]
    seen = {(sx, sy)}

    while stack:
        n, x, y = stack.pop()

        if n != 0 and (x, y) in points:
            distances_graph[(sx, sy)][(x, y)] = n
            continue

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr = x + dr
            nc = y + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != "#" and (nr, nc) not in seen:
                stack.append((n + 1, nr, nc))
                seen.add((nr, nc))

seen = set()
def dfs(pt):
    if pt == end:
        return 0

    m = -float("inf")

    seen.add(pt)
    for nx in distances_graph[pt]:
        if nx not in seen:
            m = max(m, dfs(nx) + distances_graph[pt][nx])
    seen.remove(pt)

    return m


print(dfs(start))
