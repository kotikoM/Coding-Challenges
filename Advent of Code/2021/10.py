cost = {')': 3, ']': 57, '}': 1197, '>': 25137}
opposite = {'(': ')', '[': ']', '{': '}', '<': '>'}


def parse(line):
    stack = []
    for c in line:
        if c in '([{<':
            stack.append(c)
        else:
            if not stack:
                return cost[c]

            last = stack.pop()
            if c != opposite[last]:
                return cost[c]

    return 0


total = sum([parse(line) for line in open('input').read().splitlines()])
print(total)
