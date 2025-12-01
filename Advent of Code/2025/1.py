dial = 50
total = 0
for line in open('input'):
    line = line.strip()
    direction = line[0]
    num = int(line[1:])
    dial = (dial + (num if direction == 'R' else -num)) % 100
    if dial == 0: total += 1

print(total)
