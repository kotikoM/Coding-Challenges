import re

lines = open("input").read().splitlines()
times, distances = [list(map(int, re.findall(r"\d+", line))) for line in lines]

winning = []
for i in range(len(times)):

    group = set()
    for speed in range(1, times[i] // 2 + 1):
        if (times[i] - speed) * speed > distances[i]:
            group.add(speed)
            group.add(times[i] - speed)

    winning.append(group)

res = 1
for x in winning:
    res *= len(x)

print(res)
