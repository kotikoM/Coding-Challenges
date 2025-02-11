import ast


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


total = 0
for i, pair in enumerate(open('input').read().split('\n\n')):
    a, b = map(ast.literal_eval, pair.split('\n'))
    if compare(a, b):
        total += (i + 1)

print(total)
