from collections import deque

with open('input', 'r') as file:
     flowers = [list(line.strip()) for line in file]

rows = len(flowers)
cols = len(flowers[0])
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

groups = []
visited = set()

for r in range(rows):
    for c in range(cols):
        if (r, c) not in visited:
            visited.add((r, c))
            region = {(r, c)}

            q = deque([(r, c)])
            flower = flowers[r][c]
            while q:
                cx, cy = q.popleft()
                for dx, dy in directions:
                    nx, ny = cx + dx, cy + dy
                    if nx < 0 or nx >= rows or ny < 0 or ny >= cols: continue  # out of bounds
                    if flowers[nx][ny] != flower: continue  # different flower
                    if (nx, ny) in region: continue  # already seen

                    visited.add((nx, ny))
                    region.add((nx, ny))
                    q .append((nx, ny))
            groups.append(region)


total = 0
for group_cells in groups:
    total_area = len(group_cells)
    total_perimeter = 0

    for x, y in group_cells:
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in group_cells:
                total_perimeter += 1

    print(f"Group has area {total_area} and perimeter {total_perimeter}")
    total += total_area * total_perimeter

total_sides = 0
for group in groups:
    total_area = len(group)
    sides = 0
    seen = set()

    for (x, y) in group:
        if (x, y) not in seen:
            sides += 1

            q = deque([(x, y)])
            while q:
                cx, cy = q.popleft()
                if (cx, cy) in seen: continue

                seen.add((cx, cy))
                for (dx, dy) in directions:
                    nx, ny = cx + dx, cy + dy
                    if (nx, ny) in group:
                        q.append((nx, ny))

    print(f"Group has area {total_area} and sides {sides}")
    total_sides += total_area * sides

print("Total score with perimeter:", total)
print("Total score with sides:", total_sides)
