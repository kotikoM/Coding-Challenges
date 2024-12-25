memo = {}
def divisors(n):
    if n in memo:
        return memo[n]

    divs = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divs.add(i)
            if i != n // i:
                divs.add(n // i)

    divs.discard(n)

    all_divisors = set(divs)
    for d in divs:
        if d != n:
            all_divisors.update(divisors(d))

    memo[n] = sorted(all_divisors)
    return memo[n]


num_to_div_sum = {}
for i in range(1, 10000):
    num_to_div_sum[i] = sum(divisors(i))

amicable = []
seen = set()
for num, div_sum in num_to_div_sum.items():
    if num not in seen:
        if div_sum in num_to_div_sum and num_to_div_sum[div_sum] == num and num != div_sum:
            amicable.append((num, div_sum))

    seen.add(num)
    seen.add(div_sum)

amicable_numbers = set(x for pair in amicable for x in pair)

# Calculate the sum of all amicable numbers
total_sum = sum(amicable_numbers)

# Output the result
print(total_sum)
