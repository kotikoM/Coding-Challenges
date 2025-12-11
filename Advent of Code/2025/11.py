devices = {
    i: o.split(' ')
    for l in open('input').read().split('\n')
    for i, o in [l.split(': ', 1)]
}

def count_paths(start, end):
    if start == end:
        return 1
    return sum(count_paths(n, end) for n in devices[start])

print(count_paths('you', 'out'))
