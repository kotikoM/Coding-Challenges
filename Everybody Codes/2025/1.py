names, instructions = open('input').read().split('\n\n')
names, instructions = names.split(','), instructions.split(',')

i = 0
for d in instructions:
    i += int(d[1]) * (1 if d[0] == 'R' else -1)
    i = max(0, min(i, len(names) - 1))

print(names[i])
