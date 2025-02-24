elves = []
for i, l in enumerate(open('input').read().splitlines()):
    for j, c in enumerate(l):
        if c == '#':
            elves.append((i, j))

directions = ['N', 'S', 'W', 'E']

for _ in range(20):
    proposed_positions = {}
    for idx, (x, y) in enumerate(elves):
        N, S, W, E = (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)
        NW, NE, SW, SE = (x - 1, y - 1), (x - 1, y + 1), (x + 1, y - 1), (x + 1, y + 1)

        if all(p not in elves for p in [N, NE, NW, S, SE, SW, W, E, E]):
            proposed_positions[idx] = (x, y)
            continue

        for d in directions:
            if d == 'N' and all(p not in elves for p in [N, NE, NW]):
                proposed_positions[idx] = N
                break
            elif d == 'S' and all(p not in elves for p in [S, SE, SW]):
                proposed_positions[idx] = S
                break
            elif d == 'W' and all(p not in elves for p in [W, NW, SW]):
                proposed_positions[idx] = W
                break
            elif d == 'E' and all(p not in elves for p in [E, NE, SE]):
                proposed_positions[idx] = E
                break
        else:
            proposed_positions[idx] = (x, y)

    new_positions = {}
    for idx, pos in proposed_positions.items():
        if list(proposed_positions.values()).count(pos) == 1:
            new_positions[idx] = pos
        else:
            new_positions[idx] = elves[idx]

    elves = [new_positions[idx] for idx in range(len(elves))]
    directions.append(directions.pop(0))

xs, ys = zip(*elves)
width = max(ys) - min(ys) + 1
height = max(xs) - min(xs) + 1
print(width * height - len(elves))
