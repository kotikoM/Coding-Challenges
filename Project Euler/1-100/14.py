memo = {}

def collatz_iterative(n):
    sequence = []
    current = n

    while current != 1:
        if current in memo:
            # Extend the sequence with the memoized results and break
            sequence += memo[current]
            break
        sequence.append(current)
        if current % 2 == 0:
            current = current // 2
        else:
            current = 3 * current + 1

    sequence.append(1)

    # Memoize the sequence for each number in the chain
    for i, val in enumerate(sequence):
        if val not in memo:
            memo[val] = sequence[i:]

    return sequence

# Find the number with the longest Collatz sequence under 1 million
max_len = 0
max_num = 0
for i in range(1, 10**6):
    print(i)
    lst = collatz_iterative(i)
    if len(lst) > max_len:
        max_len = len(lst)
        max_num = i

print("Length of memory: ", len(memo))
print("Number: ", max_num)
print("Collatz length: ", max_len)
