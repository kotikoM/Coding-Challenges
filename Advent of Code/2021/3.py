def common(lines, i):
    return '1' if sum(1 if l[i] == '1' else -1 for l in lines) >= 0 else '0'


lines = open('input').read().splitlines()
a, b = lines, lines
i = 0
while len(a) != 1:
    bit = common(a, i)
    a = [l for l in a if l[i] == bit]
    i += 1

i = 0
while len(b) != 1:
    bit = '0' if common(b, i) == '1' else '1'
    b = [l for l in b if l[i] == bit]
    i += 1

print(int(a[0], 2) * int(b[0], 2))
