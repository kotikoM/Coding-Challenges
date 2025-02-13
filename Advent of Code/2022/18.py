cubes = [tuple(map(int, l.split(','))) for l in open('input').read().splitlines()]

exposed_sides = 0
for x, y, z in cubes:
    possible_sides = 6
    for dx, dy, dz in [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]:
        nx, ny, nz = x + dx, y + dy, z + dz
        if (nx, ny, nz) in cubes:
            possible_sides -= 1

    exposed_sides += possible_sides

print(exposed_sides)
