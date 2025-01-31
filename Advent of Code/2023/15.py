from collections import defaultdict


def hash(sequence):
    val = 0
    for s in sequence:
        val += ord(s)
        val *= 17
        val %= 256
    return val


boxes = defaultdict(list)
for s in open('input').read().split(','):
    if '=' in s:
        code, lens = s.split('=')
        current = boxes[hash(code)]
        res = code + ' ' + lens

        if current:
            for i, c in enumerate(current):
                if code in c:
                    current[i] = res
                    break
            else:
                current.append(res)

        else:
            current.append(res)

    elif '-' in s:
        code = s[:-1]
        current = boxes[hash(code)]
        for i, c in enumerate(current):
            if code in c:
                current.remove(c)

total = 0
for k, v in boxes.items():
    res = 0
    for i, lens in enumerate(v):
        _, num = lens.split(' ')
        res += (k + 1) * (i + 1) * int(num)

    total += res

print(total)
