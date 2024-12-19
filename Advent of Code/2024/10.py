with open('input', 'r') as file:
    tmap = [list(line.strip()) for line in file]

heads = {}
for i, r in enumerate(tmap):
    for j, c in enumerate(r):
        if c == '0':
            # Puzzle 1
            heads[(i, j)] = set()

            # Puzzle 2
            #heads[(i, j)] = list()

rows = len(tmap)
cols = len(tmap[0])


def find_paths(head, pos):
    x, y = pos
    if tmap[x][y] == '9':
        # Puzzle 1
        heads[head].add(pos)

        # Puzzle 2
        # heads[head].append(pos)
    else:
        prev_num = int(tmap[x][y])

        if -1 < x - 1 < rows and int(tmap[x - 1][y]) - prev_num == 1:
            find_paths(head, (x - 1, y))

        if -1 < y + 1 < cols and int(tmap[x][y + 1]) - prev_num == 1:
            find_paths(head, (x, y + 1))

        if -1 < x + 1 < rows and int(tmap[x + 1][y]) - prev_num == 1:
            find_paths(head, (x + 1, y))

        if -1 < y - 1 < cols and int(tmap[x][y - 1]) - prev_num == 1:
            find_paths(head, (x, y - 1))


for line in tmap:
    print(line)

trail_heads = heads.keys()
for head in trail_heads:
    find_paths(head, head)

score = 0
for head, lst in heads.items():
    score += len(lst)
    print(f"Trail heads: {head}, has score {(len(lst))}")

print(f"Puzzle solution: {score}")
