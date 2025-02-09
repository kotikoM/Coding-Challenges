def contains(a1, a2, b1, b2):
    return (b1 <= a1 <= b2 or b1 <= a2 <= b2 or
            a1 <= b1 <= a2 or a1 <= b2 <= a2)


total = 0
for line in open('input').read().splitlines():
    a1, a2, b1, b2 = map(int, line.replace(',', '-').split('-'))
    if contains(int(a1), int(a2), int(b1), int(b2)):
        total += 1

print(total)
