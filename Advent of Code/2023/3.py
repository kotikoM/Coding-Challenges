from collections import defaultdict

lines = [list(x) for x in open("input").read().split("\n\n")[0].split("\n")]

grid = [[c for c in line] for line in lines]

total1 = 0
nums = defaultdict(list)
for r in range(len(grid)):
    gears = set()  # positions of '*' characters next to the current number
    n = 0
    has_part = False

    for c in range(len(grid[r]) + 1):
        if c < len(grid[0]) and grid[r][c].isdigit():
            n = n * 10 + int(grid[r][c])

            for rr in [-1, 0, 1]:
                for cc in [-1, 0, 1]:
                    if 0 <= r + rr < len(grid) and 0 <= c + cc < len(grid[0]):
                        ch = grid[r + rr][c + cc]

                        if not ch.isdigit() and ch != '.':
                            has_part = True

                        if ch == '*':
                            gears.add((r + rr, c + cc))

        elif n > 0:
            for gear in gears:
                nums[gear].append(n)
            if has_part:
                total1 += n

            n = 0
            has_part = False
            gears = set()

print(total1)
total2 = 0
for k, v in nums.items():
    if len(v) == 2:
        total2 += v[0] * v[1]
print(total2)
