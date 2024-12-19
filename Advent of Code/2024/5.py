from collections import defaultdict, deque

with open('input', 'r') as file:
    rules, updates = file.read().split('\n\n')
    rules = [tuple(map(int, rule.split('|'))) for rule in rules.split('\n')]
    updates = [list(map(int, update.split(','))) for update in updates.split('\n')]

edges_before = defaultdict(set)  # set of updates that should come before the key
edges_after = defaultdict(set)  # set of updates that should come after the key
for num1, num2 in rules:  # num1 should be printed before  num2
    edges_before[num2].add(num1)
    edges_after[num1].add(num2)

total1 = 0
total2 = 0
print(edges_before)
print(edges_after)
for update in updates:
    is_valid = True
    for i, x in enumerate(update):
        for j, y in enumerate(update):
            if i < j and y in edges_before[x]:
                is_valid = False

    if is_valid:
        total1 += update[(len(update) // 2)]
    else:
        # Sort topologically non-valid updates
        print(f"Invalid update: {update}")
        good = []
        queue = deque([])
        pre_reqs = {v: len(edges_before[v] & set(update)) for v in update}
        print(pre_reqs)

        for num in update:
            # number has no pre-reqs
            if pre_reqs[num] == 0:
                queue.append(num)

        while queue:
            x = queue.popleft()
            good.append(x)
            for y in edges_after[x]:
                if y in pre_reqs:
                    pre_reqs[y] -= 1
                    if pre_reqs[y] == 0:
                        queue.append(y)

        total2 += good[(len(good) // 2)]

print(f"Puzzle 1 answer, total: {total1}")
print(f"Puzzle 2 answer, total: {total2}")
