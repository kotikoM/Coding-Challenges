import math


def find_lexicographic_permutation(n, digits):
    result = []
    available_digits = digits[:]

    n -= 1

    for i in range(len(digits), 0, -1):
        fact = math.factorial(i - 1)

        index = n // fact
        result.append(available_digits[index])

        available_digits.pop(index)
        n %= fact

    return ''.join(map(str, result))


digits = list(range(10))
millionth_permutation = find_lexicographic_permutation(1000000, digits)

print(millionth_permutation)
