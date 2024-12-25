from functools import cache

buyers = [int(x) for x in open("input").read().split("\n")]


@cache
def mix_prune(secret, num):
    secret = secret ^ num
    secret = secret % 16777216
    return secret


@cache
def calculate(secret):
    num = secret * 64
    secret = mix_prune(secret, num)

    num = secret // 32
    secret = mix_prune(secret, num)

    num = secret * 2048
    secret = mix_prune(secret, num)
    return secret


seq_to_total = {}
for secret in buyers:
    num = secret
    buyer = [num % 10]

    for _ in range(2000):
        num = calculate(num)
        buyer.append(num % 10)

    seen = set()
    for i in range(len(buyer) - 4):
        a, b, c, d, e = buyer[i:i + 5]
        seq = (b - a, c - b, d - c  , e - d)
        if seq in seen: continue

        seen.add(seq)
        if seq not in seq_to_total: seq_to_total[seq] = 0

        seq_to_total[seq] += e

print(max(seq_to_total.values()))
