def puzzle1():
    col1 = []
    col2 = []

    with open('input', 'r') as file:
        for line in file:
            # Split each line into two numbers and append them to the respective lists
            num1, num2 = line.split()
            col1.append(int(num1))
            col2.append(int(num2))

    col1.sort()
    col2.sort()

    result = 0
    for i in range(len(col1)):
        result += abs(col1[i] - col2[i])

    print(col1)
    print(col2)
    print(result)


def puzzle2():
    col1 = []
    col2 = []

    with open('input', 'r') as file:
        for line in file:
            # Split each line into two numbers and append them to the respective lists
            num1, num2 = line.split()
            col1.append(int(num1))
            col2.append(int(num2))

    col1.sort()
    col2.sort()

    result = 0
    for i in range(len(col1)):
        times = 0
        j = 0
        while j < len(col2) and col1[i] >= col2[j]:
            if col1[i] == col2[j]:
                times += 1
            j += 1

        result += col1[i] * times

    print(col1)
    print(col2)
    print(result)

puzzle1()
puzzle2()
