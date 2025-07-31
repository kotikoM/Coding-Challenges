from collections import Counter
from functools import lru_cache

template, pairs_raw = open('input').read().split('\n\n')
pairs = dict(line.split(' -> ') for line in pairs_raw.split('\n'))


@lru_cache(maxsize=None)
def count_chars(pair, steps):
    if steps == 0 or pair not in pairs:
        return Counter()

    insert = pairs[pair]
    left = pair[0] + insert
    right = insert + pair[1]

    counter = Counter(insert)
    counter += count_chars(left, steps - 1)
    counter += count_chars(right, steps - 1)
    return counter


steps = 40
total_count = Counter(template)
for a, b in zip(template, template[1:]):
    pair = a + b
    total_count += count_chars(pair, steps)

most = max(total_count.values())
least = min(total_count.values())
print(most - least)
