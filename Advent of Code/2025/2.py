def repeated_numbers_in_range(L, R):
    results = set()

    min_len = len(str(L))
    max_len = len(str(R))

    for total_len in range(min_len, max_len + 1):
        for k in range(2, total_len + 1):
            if total_len % k != 0:
                continue

            block_len = total_len // k

            start = 10 ** (block_len - 1)
            end = 10 ** block_len - 1

            for s in range(start, end + 1):
                n = int(str(s) * k)
                if n > R:
                    break
                if n >= L:
                    results.add(n)

    return results

print(sum(
    n
    for part in open('input').read().strip().split(',')
    for L, R in [tuple(map(int, part.split('-')))]
    for n in repeated_numbers_in_range(L, R)
))
