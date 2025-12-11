from functools import lru_cache

devices = {
    i: o.split(' ')
    for l in open('input').read().split('\n')
    for i, o in [l.split(': ', 1)]
}

@lru_cache(None)
def count_paths(start, end):
    if start == end:
        return 1
    if start == 'out':
        return 0
    return sum(count_paths(n, end) for n in devices[start])


print(count_paths('svr', 'fft') * count_paths('fft', 'dac') * count_paths('dac', 'out') +
      count_paths('svr', 'dac') * count_paths('dac', 'fft') * count_paths('fft', 'out'))
