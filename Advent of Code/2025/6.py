from math import prod

lines = [l.split() for l in open("input")]
numbers = [list(map(int, r)) for r in lines[:-1]]
ops = lines[-1]

total = 0
for col, op in enumerate(ops):
    nums = [row[col] for row in numbers]
    total += (prod(nums) if op == '*' else sum(nums))

print(total)
