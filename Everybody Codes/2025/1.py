names, instructions = open('input').read().split('\n\n')
names, instructions = names.split(','), instructions.split(',')

for d in instructions:
    direction = 1 if d[0] == 'R' else -1
    steps = int(d[1:])
    j = (direction * steps) % len(names)

    names[0], names[j] = names[j], names[0]

print(names[0])
