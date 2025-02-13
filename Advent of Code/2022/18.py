from collections import defaultdict

cubes = [tuple(map(int, l.split(','))) for l in open('input').read().splitlines()]

cubes_along_z = defaultdict(list)
cubes_along_x = defaultdict(list)
cubes_along_y = defaultdict(list)
for x, y, z in cubes:
    cubes_along_z[(x, y)].append(z)
    cubes_along_y[(x, z)].append(y)
    cubes_along_x[(y, z)].append(x)

air_cubes = []
for k, v in cubes_along_z.items():
    x, y = k
    v = sorted(v)
    for i in range(1, len(v)):
        if v[i] - v[i - 1] > 1:
            for z in range(v[i - 1] + 1, v[i]):
                # air cube iff 2 blocks on the same x and y axis
                cubes_on_y_axis = cubes_along_y[(x, z)]
                cubes_on_x_axis = cubes_along_x[(y, z)]

                if len(cubes_on_x_axis) > 1 and len(cubes_on_y_axis) > 1:
                    min_x, max_x = min(cubes_on_x_axis), max(cubes_on_x_axis)
                    min_y, max_y = min(cubes_on_y_axis), max(cubes_on_y_axis)
                    if min_x < x < max_x and min_y < y < max_y:
                        air_cubes.append((x, y, z))

exposed_sides = 0
for x, y, z in cubes:
    possible_sides = 6
    for dx, dy, dz in [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]:
        nx, ny, nz = x + dx, y + dy, z + dz
        if (nx, ny, nz) in cubes:
            possible_sides -= 1

        if (nx, ny, nz) in air_cubes:
            possible_sides -= 1

    exposed_sides += possible_sides

print(exposed_sides)
