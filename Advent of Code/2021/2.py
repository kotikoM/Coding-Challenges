x, y = 0, 0

for l in open('input').read().split('\n'):
    dir, dist = l.split()
    if dir == 'forward':
        x += int(dist)
    elif dir == 'up':
        y -= int(dist)
    elif dir == 'down':
        y += int(dist)

print(x * y)
