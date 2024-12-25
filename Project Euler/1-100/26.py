def find_cycle_length(d):
    # We are looking for the smallest k such that 10^k ≡ 1 (mod d)
    remainder = 1
    for length in range(1, d + 1):
        remainder = (remainder * 10) % d
        if remainder == 1:
            return length
    return 0  # If no cycle, it is a terminating decimal


def find_longest_recurring_cycle(limit):
    max_cycle_length = 0
    number_with_max_cycle = 0

    for d in range(2, limit):
        cycle_length = find_cycle_length(d)
        if cycle_length > max_cycle_length:
            max_cycle_length = cycle_length
            number_with_max_cycle = d

    return number_with_max_cycle, max_cycle_length


# Example: Finding the number with the longest recurring cycle up to 1000
limit = 1000
result = find_longest_recurring_cycle(limit)
print(f"The number with the longest recurring cycle is {result[0]} with a cycle length of {result[1]}")
