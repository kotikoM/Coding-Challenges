from itertools import product

dict = {}
with open('input', 'r') as file:
    for line in file:
        key, values = line.split(":")
        key = int(key)
        value_list = list(map(int, values.strip().split()))
        dict[key] = value_list


def evaluate_expression(values, operators):
    result = values[0]
    for i in range(1, len(values)):
        if operators[i - 1] == "+":
            result += values[i]
        elif operators[i - 1] == "*":
            result *= values[i]
        else:
            result = int(str(result) + str(values[i]))
    return result


calibration = 0
ops = "+*|"
for key, values in dict.items():
    is_valid = False
    num_ops = len(values) - 1
    op_combs = list(product(ops, repeat=num_ops))

    for comb in op_combs:
        result = evaluate_expression(values, comb)
        if result == key:
            is_valid = True
            calibration += key
            print(f"Answer: {key} with values: {values}, is {is_valid}, with operators: {comb}")
            break

print(f"Calibration is {calibration}, for operations {ops}")
