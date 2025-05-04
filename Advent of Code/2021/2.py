x, y, aim = 0, 0, 0

for l in open('input').read().split('\n'):
    dir, dist = l.split()
    if dir == 'forward':
        x += int(dist)
        y += aim * int(dist)
    elif dir == 'up':
        aim -= int(dist)
    elif dir == 'down':
        aim += int(dist)

print(x * y)
