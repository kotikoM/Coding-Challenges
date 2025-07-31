cords, folds = open('input').read().split('\n\n')

cords = set(tuple(map(int, l.split(','))) for l in cords.split('\n'))
folds = [line.split('=') for line in folds.split('\n')]

new_cords = set()
for f in folds:
    axis, value = f
    axis = axis.split(' ')[-1]
    value = int(value)

    for x, y in cords:
        if axis == 'x':
            if x > value:
                x = 2 * value - x
        elif axis == 'y':
            if y > value:
                y = 2 * value - y
        new_cords.add((x, y))

    cords = new_cords
    new_cords = set()
