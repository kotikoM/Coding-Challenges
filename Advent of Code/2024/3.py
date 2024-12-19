import re


def puzzle1():
    input = open('input', 'r').read()
    pattern = r"mul\(([0-9]+),([0-9]+)\)"
    muls = re.findall(pattern, input)

    result = 0
    for mul in muls:
        num1, num2 = mul
        result += int(num1) * int(num2)

    print(result)
    return result


def puzzle2():
    input = open('input', 'r').read()
    pattern = r"mul\([0-9]+,[0-9]+\)|don't\(\)|do\(\)"
    muls = re.findall(pattern, input)

    result = 0
    mode = "do"
    for mul in muls:
        if mul == "don't()":
            mode = "dont"
            continue
        elif mul == "do()":
            mode = "do"
            continue

        if mode == "do":
            numbers_str = mul[4:-1]
            num1, num2 = numbers_str.split(',')
            result += int(num1) * int(num2)

    print(result)
    return result


puzzle1()
puzzle2()
