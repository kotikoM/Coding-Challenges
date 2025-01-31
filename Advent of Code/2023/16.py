from collections import deque

mirror = {
    '/ UP': ['RIGHT'],
    '/ DOWN': ['LEFT'],
    '/ RIGHT': ['UP'],
    '/ LEFT': ['DOWN'],

    '\ UP': ['LEFT'],
    '\ DOWN': ['RIGHT'],
    '\ RIGHT': ['DOWN'],
    '\ LEFT': ['UP'],

    '| UP': ['UP'],
    '| DOWN': ['DOWN'],
    '| RIGHT': ['UP', 'DOWN'],
    '| LEFT': ['DOWN', 'UP'],

    '- UP': ['LEFT', 'RIGHT'],
    '- DOWN': ['LEFT', 'RIGHT'],
    '- RIGHT': ['RIGHT'],
    '- LEFT': ['LEFT'],

    '. UP': ['UP'],
    '. DOWN': ['DOWN'],
    '. RIGHT': ['RIGHT'],
    '. LEFT': ['LEFT'],
}

dirs = {
    'UP': (-1, 0),
    'DOWN': (1, 0),
    'RIGHT': (0, 1),
    'LEFT': (0, -1),
}

grid = [list(l) for l in open('input').read().splitlines()]


def energize(start):
    q = deque([start])
    visited_with_d = set()
    visited = set()
    while q:
        x, y, d = q.popleft()
        if (x, y, d) in visited_with_d:
            continue

        visited_with_d.add((x, y, d))
        visited.add((x, y))

        c = grid[x][y]
        for new_d in mirror[c + ' ' + d]:
            dx, dy = dirs[new_d]
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
                q.append((new_x, new_y, new_d))
    return len(visited)


max_e = -1
h = len(grid) - 1
w = len(grid[0]) - 1
x, y = 0, 0
dir = 'DOWN'
while True:
    if x == 0 and y == 0 and dir == 'RIGHT':
        break

    if dir == 'DOWN':
        # going right
        _, dy = dirs['RIGHT']
        if y + dy >= len(grid[0]):
            dir = 'LEFT'
            continue
        y += dy
    elif dir == 'LEFT':
        # going down
        dx, _ = dirs['DOWN']
        if x + dx >= len(grid):
            dir = 'UP'
            continue
        x += dx
    elif dir == 'UP':
        # going left
        _, dy = dirs['LEFT']
        if y + dy < 0:
            dir = 'RIGHT'
            continue
        y += dy
    elif dir == 'RIGHT':
        # going up
        dx, _ = dirs['UP']
        if x + dx < 0:
            dir = 'DOWN'
            continue
        x += dx

    e = energize((x, y, dir))
    if e > max_e:
        max_e = e

print(max_e)
