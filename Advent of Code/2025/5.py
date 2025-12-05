ranges, _ = open('input').read().split('\n\n')
ranges = [tuple(map(int, t.split('-'))) for t in ranges.split('\n')]
ranges.sort()

merged = []
for l, r in ranges:
    if not merged or l > merged[-1][1] + 1:
        merged.append([l, r])
    else:
        merged[-1][1] = max(merged[-1][1], r)

total = sum(r - l + 1 for l, r in merged)
print(total)
