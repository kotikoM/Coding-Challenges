import ast
import functools


def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return None if a == b else a < b

    if isinstance(a, list) and isinstance(b, list):
        for x, y in zip(a, b):
            result = compare(x, y)
            if result is not None:
                return result
        return len(a) < len(b) if len(a) != len(b) else None

    if isinstance(a, int):
        return compare([a], b)
    if isinstance(b, int):
        return compare(a, [b])

    return False


def compare_wrapper(a, b):
    result = compare(a, b)
    return -1 if result else (1 if not result else 0)


key1, key2 = [[2]], [[6]]
all_pairs = [key1, key2]
for i, pair in enumerate(open('input').read().split('\n\n')):
    a, b = map(ast.literal_eval, pair.split('\n'))
    all_pairs.append(a)
    all_pairs.append(b)

all_pairs.sort(key=functools.cmp_to_key(compare_wrapper))
print((all_pairs.index(key1) + 1) * (all_pairs.index(key2) + 1))
