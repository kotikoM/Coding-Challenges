X = [1]
for line in open('input').read().splitlines():
    X.append(X[-1])
    if line.startswith('addx'):
        _, v = line.split()
        X.append(X[-1] + int(v))

print(sum(X[i - 1] * i for i in [20, 60, 100, 140, 180, 220]))
