lines = open("a").read().split("\n")
grid = [line.split() for line in lines]

avg = 0
r = len(grid)
c = len(grid[0])

# Convert grid values to integers and calculate the average
for i in range(r):
    for j in range(c):
        num = int(grid[i][j])
        avg += num
        grid[i][j] = num

avg = int(avg / (r * c))

# Horizontal check
max_r = 0
for i in range(r):
    for j in range(c - 3):  # Change to c - 3 to consider 4 points
        if (grid[i][j] > avg and
            grid[i][j + 1] > avg and
            grid[i][j + 2] > avg and
            grid[i][j + 3] > avg):
            res = grid[i][j] * grid[i][j + 1] * grid[i][j + 2] * grid[i][j + 3]
            if res > max_r:
                max_r = res

print("Max on horizontal: ", max_r)

# Vertical check
max_d = 0
for j in range(c):
    for i in range(r - 3):  # Change to r - 3 to consider 4 points
        if (grid[i][j] > avg and
            grid[i + 1][j] > avg and
            grid[i + 2][j] > avg and
            grid[i + 3][j] > avg):
            res = grid[i][j] * grid[i + 1][j] * grid[i + 2][j] * grid[i + 3][j]
            if res > max_d:
                max_d = res
print("Max on vertical: ", max_d)

# Diagonal check
max_diag = 0

# Top-left to bottom-right diagonal
for i in range(r - 3):  # Change to r - 3
    for j in range(c - 3):  # Change to c - 3
        if (grid[i][j] > avg and
            grid[i + 1][j + 1] > avg and
            grid[i + 2][j + 2] > avg and
            grid[i + 3][j + 3] > avg):
            res = grid[i][j] * grid[i + 1][j + 1] * grid[i + 2][j + 2] * grid[i + 3][j + 3]
            if res > max_diag:
                max_diag = res

# Top-right to bottom-left diagonal
for i in range(r - 3):  # Change to r - 3
    for j in range(3, c):  # Change to start from 3 and consider 4 points
        if (grid[i][j] > avg and
            grid[i + 1][j - 1] > avg and
            grid[i + 2][j - 2] > avg and
            grid[i + 3][j - 3] > avg):
            res = grid[i][j] * grid[i + 1][j - 1] * grid[i + 2][j - 2] * grid[i + 3][j - 3]
            if res > max_diag:
                max_diag = res

print("Max on diagonal: ", max_diag)

# Overall max
overall_max = max(max_r, max_d, max_diag)
print("Overall max: ", overall_max)
