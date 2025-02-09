bags = [l for l in open('input').read().splitlines()]

appears_both = []
for b in bags:
    assert len(b) % 2 == 0

    left, right = b[:len(b) // 2], b[len(b) // 2:]
    intersection = set(left) & set(right)
    appears_both.append(intersection.pop())


def char_to_int(c):
    return ord(c) - 96 if 'a' <= c <= 'z' else ord(c) - 38


print(sum(map(char_to_int, appears_both)))
