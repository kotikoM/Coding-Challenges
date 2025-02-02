w, r = open('input').read().split('\n\n')

workflows = {}
for l in w.split('\n'):
    name, b = l[:-1].split('{')
    rules = b.split(',')
    workflows[name] = ([], rules.pop())
    for rule in rules:
        comp, t = rule.split(':')
        key = comp[0]
        cmp = comp[1]
        n = int(comp[2:])
        workflows[name][0].append((key, cmp, n, t))


def count(ranges, name='in'):
    if name == 'R':
        return 0
    if name == 'A':
        product = 1
        for low, high in ranges.values():
            product *= high - low + 1
        return product

    rules, fallback = workflows[name]
    total = 0
    for key, cmp, n, t in rules:
        low, high = ranges[key]
        if cmp == '<':
            T = (low, n - 1)
            F = (n, high)
        elif cmp == '>':
            T = (n + 1, high)
            F = (low, n)

        if T[0] <= T[1]:
            copy = dict(ranges)
            copy[key] = T
            total += count(copy, t)

        if F[0] <= F[1]:
            ranges = dict(ranges)
            ranges[key] = F
        else:
            break
    else:
        total += count(ranges, fallback)

    return total


print(count({key: (1, 4000) for key in 'xmas'}))
