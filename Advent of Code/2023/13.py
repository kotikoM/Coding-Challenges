def get_mirror(pattern):
    for r in range(1, len(pattern)):
        above = pattern[:r][::-1]
        below = pattern[r:]

        if sum(sum(0 if ac == bc else 1 for ac, bc, in zip(a, b)) for a, b in zip(above, below)) == 1:
            return r

    return 0


total = 0
for pattern in open('input').read().split('\n\n'):
    pattern = pattern.split('\n')

    row = get_mirror(pattern)
    total += row * 100

    col = get_mirror(list(zip(*pattern)))
    total += col

print(total)
