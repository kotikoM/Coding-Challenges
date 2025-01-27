grid = [list(s) for s in open('input').read().splitlines()]

x, y = 0, 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == 'S':
            x, y = r, c
            break
    else:
        continue

dirs = {
    'DOWN': (1, 0),
    'UP': (-1, 0),
    'LEFT': (0, -1),
    'RIGHT': (0, 1)
}
def next(x, y, dir):
    piping = {
        '| DOWN': 'DOWN',
        '| UP': 'UP',

        '- LEFT': 'LEFT',
        '- RIGHT': 'RIGHT',

        'L DOWN': 'RIGHT',
        'L LEFT': 'UP',

        'J DOWN': 'LEFT',
        'J RIGHT': 'UP',

        '7 RIGHT': 'DOWN',
        '7 UP': 'LEFT',

        'F UP': 'RIGHT',
        'F LEFT': 'DOWN'
    }
    current_pipe = grid[x][y]
    next_dir = piping[current_pipe + ' ' + dir]
    dx, dy = dirs[next_dir]
    return x + dx, y + dy, next_dir


def create_path(current_dir):
    visited = []
    dx, dy = dirs[current_dir]
    cx, cy = x + dx, y + dy
    while True:
        visited.append((cx, cy))
        nx, ny, next_dir = next(cx, cy, current_dir)
        current_dir = next_dir
        cx, cy = nx, ny
        if cx == x and cy == y:
            break
    return visited

visited1 = create_path('LEFT')
visited2 = create_path('DOWN')
path = {}
for i, v in enumerate(visited1):
    i += 1
    path[v] = i

for i, v in enumerate(visited2):
    i += 1
    if v in path.keys():
        path[v] = min(path[v], i)
    else:
        path[v] = i


print(max(path.values()))
