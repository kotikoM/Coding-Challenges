def play(a, b):
    scores = {'X': 1, 'A': 1, 'B': 2, 'Y': 2, 'C': 3, 'Z': 3}

    round_score = 0
    if (a == 'A' and b == 'X') or (a == 'B' and b == 'Y') or (a == 'C' and b == 'Z'):
        round_score = 3

    # A - rock, B - paper, C - scissors
    # X - rock, Y - paper, Z - scissors
    elif (b == 'X' and a == 'C') or (b == 'Y' and a == 'A') or (b == 'Z' and a == 'B'):
        round_score = 6
    return scores[b] + round_score


total = 0
for line in open('input'):
    a, b = line.strip().split()
    total += play(a, b)
print(total)
