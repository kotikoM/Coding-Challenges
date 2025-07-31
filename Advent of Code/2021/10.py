cost = {'(': 1, '[': 2, '{': 3, '<': 4}
match = {'(': ')', '[': ']', '{': '}', '<': '>'}


def parse(line):
    stack = []
    for c in line:
        if c in match:
            stack.append(c)
        elif not stack or match[stack.pop()] != c:
            return None
    return stack


def get_score(s):
    score = 0
    for c in reversed(s):
        score = score * 5 + cost[c]
    return score


lines = open('input').read().splitlines()
sums = [
    get_score(stack)
    for line in lines
    if (stack := parse(line))
]

sums.sort()
print(sums[len(sums) // 2])
