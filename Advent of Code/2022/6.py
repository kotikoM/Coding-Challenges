def has_duplicates(s):
    return len(set(s)) == len(s)


signals = list(open('input').read().split()[0])
for i in range(0, len(signals)):
    if has_duplicates(signals[i:i + 14]):
        print(i + 14)
        break
