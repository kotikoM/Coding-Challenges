def roll(grid):
    height = len(grid)
    width = len(grid[0])

    for dx, dy, orient in [(-1, 0, 'n'), (0, -1, 'w'), (1, 0, 's'), (0, 1, 'e')]:
        marbles = []
        for x in range(height):
            for y in range(width):
                marbles.append((x, y))

        if orient == 'n':
            marbles = sorted(marbles, key=lambda x: x[0])
        elif orient == 'w':
            marbles = sorted(marbles, key=lambda x: x[1])
        elif orient == 's':
            marbles = reversed(sorted(marbles, key=lambda x: x[0]))
        elif orient == 'e':
            marbles = reversed(sorted(marbles, key=lambda x: x[1]))

        for x, y in marbles:
            if grid[x][y] == 'O':
                cx, cy = x, y

                while (-1 < cx + dx < height and -1 < cy + dy < width
                       and grid[cx + dx][cy + dy] != '#'
                       and grid[cx + dx][cy + dy] != 'O'):
                    grid[cx][cy] = '.'
                    cx += dx
                    cy += dy
                    grid[cx][cy] = 'O'


grid = [list(l) for l in open('input').read().splitlines()]
print(''.join([''.join(g) + '\n' for g in grid]))
for i in range(1_000_000_000):
    roll(grid)
    total = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 'O':
                total += len(grid) - x
    print(f'iteration: {i + 1}, total: {total}')
    # Manually inspect the length of a repeating pattern:
    # 1. Wait until the values of `total` start repeating.
    # 2. Note the size (length) of the repeating pattern and the iteration where it starts.

    # Optimize the calculation:
    # - Divide target iterations by the pattern length to determine:
    #   - The remainder (leftover iterations after completing the full cycles).
    # - Use the results to compute the final total for target iterations as:
    #   - Length of a repeating pattern times some integer + remainder.
    #   - Resulted number is the iteration number which has same total score as target iteration.
