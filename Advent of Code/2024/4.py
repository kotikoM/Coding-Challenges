def count_xmas(s: str):
    return s.count('XMAS') + s.count('SAMX')


def puzzle1():
    puzzle = []

    with open('input', 'r') as file:
        for line in file:
            puzzle.append(line.strip())

    total = 0

    # Check horizontal
    for line in puzzle:
        total += count_xmas(line)

    # Check vertical
    for i in range(len(puzzle[0])):  # Length of a row
        vertical = ''
        for j in range(len(puzzle)):  # Length of a puzzle
            vertical += puzzle[j][i]
        total += count_xmas(vertical)

    # Check diagonal left to right
    for i in range(len(puzzle)):
        if i == 0:
            j_values = range(len(puzzle[0]))
        else:
            j_values = [0]

        for j in j_values:
            diagonal = ''
            a, b = i, j
            while a < len(puzzle) and b < len(puzzle[a]):
                diagonal += puzzle[a][b]
                a += 1
                b += 1
            total += count_xmas(diagonal)

    # Check diagonal right to left
    for i in range(len(puzzle)):
        if i == 0:
            j_values = range(len(puzzle[0]) - 1, -1, -1)
        else:
            j_values = [len(puzzle[0]) - 1]

        for j in j_values:
            diagonal = ''
            a, b = i, j
            while a < len(puzzle) and b > -1:
                diagonal += puzzle[a][b]
                a += 1
                b -= 1
            total += count_xmas(diagonal)

    print(f'Final total: {total}')
    return total


def count_mas(row1, row2, row3):
    diagonal1 = row1[0] + row2[1] + row3[2]
    diagonal2 = row1[2] + row2[1] + row3[0]
    print(diagonal1)
    print(diagonal2)
    if (diagonal1 == 'MAS' or diagonal1 == 'SAM') and (diagonal2 == 'MAS' or diagonal2 == 'SAM'):
        return 1
    return 0


def puzzle2():
    puzzle = []

    with open('input', 'r') as file:
        for line in file:
            puzzle.append(line.strip())

    total = 0

    for i in range(len(puzzle) - 2):
        for j in range(len(puzzle[i]) - 2):
            # First Row
            grid1 = puzzle[i][j:j + 3]
            grid2 = puzzle[i + 1][j:j + 3]
            grid3 = puzzle[i + 2][j:j + 3]

            total += count_mas(grid1, grid2, grid3)

    print(f'Final total: {total}')
    return total


puzzle1()
puzzle2()
