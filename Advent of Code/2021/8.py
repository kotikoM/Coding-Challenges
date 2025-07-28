def decode_line(ten_signals, output_values):
    patterns = [''.join(sorted(p)) for p in ten_signals]
    patterns_set = [set(p) for p in patterns]

    digits = {}

    for p in patterns_set:
        if len(p) == 2:
            digits[1] = p
        elif len(p) == 3:
            digits[7] = p
        elif len(p) == 4:
            digits[4] = p
        elif len(p) == 7:
            digits[8] = p

    for p in patterns_set:
        if len(p) == 5:  # 2, 3, 5
            if digits[1] <= p:
                digits[3] = p
            elif len(p & digits[4]) == 3:
                digits[5] = p
            else:
                digits[2] = p
        elif len(p) == 6:  # 0, 6, 9
            if digits[4] <= p:
                digits[9] = p
            elif digits[1] <= p:
                digits[0] = p
            else:
                digits[6] = p

    pattern_to_digit = {''.join(sorted(v)): str(k) for k, v in digits.items()}

    output_number = int(''.join([pattern_to_digit[''.join(sorted(o))] for o in output_values]))
    return output_number


total = 0
for l in open('input').read().split('\n'):
    ten, four = l.strip().split(' | ')
    total += decode_line(ten.split(), four.split())

print(total)
