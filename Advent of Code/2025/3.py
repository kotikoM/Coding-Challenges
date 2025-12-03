total = 0
for l in open('input').read().splitlines():
    nums = list(map(int, l))
    k = 12
    drop = len(nums) - k
    out = []
    for x in nums:
        while drop and out and out[-1] < x:
            out.pop()
            drop -= 1
        out.append(x)
    out = out[:k]
    total += int(''.join(map(str, out)))

print(total)
