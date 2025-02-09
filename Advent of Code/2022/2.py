def play(a, b):
    scores = {'A': 1, 'B': 2, 'C': 3, 'X': 0, 'Y': 3, 'Z': 6}
    lose = {'A': 'C', 'B': 'A', 'C': 'B'}
    tie = {'A': 'A', 'B': 'B', 'C': 'C'}
    win = {'A': 'B', 'B': 'C', 'C': 'A'}

    # A - rock, B - paper, C - scissors
    select_score = 0
    if b == 'X':
        select_score = scores[lose[a]]
    elif b == 'Y':
        select_score = scores[tie[a]]
    elif b == 'Z':
        select_score = scores[win[a]]

    return select_score + scores[b]


total = 0
for line in open('input'):
    a, b = line.strip().split()
    total += play(a, b)
print(total)
