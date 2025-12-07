lines = [line.strip("\n") for line in open('input')]
cols = list(zip(*lines))

groups = []
group = []

for col in cols:
    if set(col) == {" "}:
        groups.append(group)
        group = []
    else:
        group.append(col)

groups.append(group)

total = 0

for group in groups:
    total += eval(group[0][-1].join("".join(line[:-1]) for line in group))

print(total)
