import heapq

grid = [list(map(int, line)) for line in open('input').read().splitlines()]
rows, cols = len(grid), len(grid[0])

expanded = [[0] * (cols * 5) for _ in range(rows * 5)]
for i in range(5):
    for j in range(5):
        for x in range(rows):
            for y in range(cols):
                new_value = (grid[x][y] + i + j - 1) % 9 + 1
                expanded[x + i * rows][y + j * cols] = new_value

rows, cols = len(expanded), len(expanded[0])
visited = [[False] * cols for _ in range(rows)]
min_risk = [[float('inf')] * cols for _ in range(rows)]

pq = [(0, 0, 0)]
while pq:
    risk, x, y = heapq.heappop(pq)

    if visited[x][y]: continue
    visited[x][y] = True

    if x == rows - 1 and y == cols - 1:
        print(risk)
        break

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            new_risk = risk + expanded[nx][ny]

            if new_risk < min_risk[nx][ny]:
                min_risk[nx][ny] = new_risk
                heapq.heappush(pq, (new_risk, nx, ny))
