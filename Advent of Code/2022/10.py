X = [1]
for line in open('input').read().splitlines():
    X.append(X[-1])
    if line.startswith('addx'):
        _, v = line.split()
        X.append(X[-1] + int(v))

screen = list('.' * 240)
for i in range(1, 240):
    if (i % 40) in [X[i], X[i] + 1, X[i] - 1]:
        screen[i] = '#'

for line in [screen[i:i + 40] for i in range(0, len(screen), 40)]:
    print(''.join(line))

# .##..#....#..#.#....#..#.###..####.#..#.
# #..#.#....#..#.#....#.#..#..#....#.#..#.
# #..#.#....#..#.#....##...###....#..####.
# ###..#....#..#.#....#.#..#..#..#...#..#.
# #....#....#..#.#....#.#..#..#.#....#..#.
# #....####..##..####.#..#.###..####.#..#.
