bags = [l for l in open('input').read().splitlines()]

appears_both = []
for i in range(0, len(bags), 3):
    b1, b2, b3 = bags[i], bags[i + 1], bags[i + 2]

    intersection = set(b1) & set(b2) & set(b3)
    appears_both.append(intersection.pop())


def char_to_int(c):
    return ord(c) - 96 if 'a' <= c <= 'z' else ord(c) - 38


print(sum(map(char_to_int, appears_both)))
