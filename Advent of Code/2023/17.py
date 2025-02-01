from heapq import heappush, heappop

grid = [list(map(int, line.strip())) for line in open('input').read().splitlines()]

seen = set()
pq = [(0, 0, 0, 0, 0, 0)]

while pq:
    hl, x, y, dx, dy, n = heappop(pq)

    if x == len(grid) - 1 and y == len(grid[0]) - 1 and n >= 4:
        print(hl)
        break

    if (x, y, dx, dy, n) in seen:
        continue

    seen.add((x, y, dx, dy, n))

    if n < 10 and (dx, dy) != (0, 0):
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            heappush(pq, (hl + grid[nx][ny], nx, ny, dx, dy, n + 1))

    if n >= 4 or (dx, dy) == (0, 0):
        for ndx, ndy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if (ndx, ndy) == (dx, dy) or (ndx, ndy) == (-dx, -dy):
                continue
            nx, ny = x + ndx, y + ndy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                heappush(pq, (hl + grid[nx][ny], nx, ny, ndx, ndy, 1))
