import heapq

grid = [list(map(int, line)) for line in open('input').read().splitlines()]

rows, cols = len(grid), len(grid[0])
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
            new_risk = risk + grid[nx][ny]

            if new_risk < min_risk[nx][ny]:
                min_risk[nx][ny] = new_risk
                heapq.heappush(pq, (new_risk, nx, ny))
