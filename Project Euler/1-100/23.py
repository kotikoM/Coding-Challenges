def sum_of_proper_divisors(n):
    divisors_sum = 1  # 1 is always a divisor
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    return divisors_sum

limit = 28123
abundant_numbers = []

for i in range(12, limit + 1):
    if sum_of_proper_divisors(i) > i:
        abundant_numbers.append(i)

can_be_written_as_sum = [False] * (limit + 1)

for i in range(len(abundant_numbers)):
    for j in range(i, len(abundant_numbers)):
        abundant_sum = abundant_numbers[i] + abundant_numbers[j]
        if abundant_sum <= limit:
            can_be_written_as_sum[abundant_sum] = True

non_abundant_sum = sum(i for i in range(1, limit + 1) if not can_be_written_as_sum[i])

print(non_abundant_sum)
