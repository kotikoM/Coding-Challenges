def repeated_numbers_in_range(L, R):
    results = []

    min_len = len(str(L))
    max_len = len(str(R))

    for total_len in range(min_len, max_len + 1):
        if total_len % 2 == 1:
            continue

        half_len = total_len // 2
        start = 10 ** (half_len - 1)
        end = 10 ** half_len - 1

        for s in range(start, end + 1):
            n = int(str(s) * 2)
            if n > R:
                break
            if n >= L:
                results.append(n)

    return results


print(sum(
    n
    for part in open('input').read().strip().split(',')
    for L, R in [tuple(map(int, part.split('-')))]
    for n in repeated_numbers_in_range(L, R)
))
