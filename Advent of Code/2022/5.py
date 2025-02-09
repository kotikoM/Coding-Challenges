import re

columns = [[],
           ['B', 'L', 'D', 'T', 'W', 'C', 'F', 'M'],
           ['N', 'B', 'L'],
           ['J', 'C', 'H', 'T', 'L', 'V'],
           ['S', 'P', 'J', 'W'],
           ['Z', 'S', 'C', 'F', 'T', 'L', 'R'],
           ['W', 'D', 'G', 'B', 'H', 'N', 'Z'],
           ['F', 'M', 'S', 'P', 'V', 'G', 'C', 'N'],
           ['W', 'Q', 'R', 'J', 'F', 'V', 'C', 'Z'],
           ['R', 'P', 'M', 'L', 'H']]


def operate(n, s, e):
    moved = []
    for _ in range(n):
        a = columns[s].pop()
        moved.append(a)

    columns[e] += moved


_, instructions = open('input').read().split('\n\n')

for i in instructions.split('\n'):
    n, s, e = map(int, re.findall(r'\d+', i))
    operate(n, s, e)

top = ''
for c in columns:
    if c:
        top += c[-1]

print(top)
