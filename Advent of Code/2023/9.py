lines = open('input').read().splitlines()

sequences = []
for line in lines:
    sequences.append([int(x) for x in line.split()])


def predict(numbers):
    numbers = [numbers]
    while True:
        res = numbers[-1]
        if res.count(0) == len(res):
            break

        new = []
        for i in range(1, len(res)):
            new.append(res[i] - res[i - 1])
        numbers.append(new)

    # Part 1
    # prediction = sum([n[-1] for n in numbers])

    # Part 2
    prediction = 0
    for n in reversed(numbers[:-1]):
        prediction = n[0] - prediction

    return prediction


total = 0
for s in sequences:
    total += predict(s)
print(total)
