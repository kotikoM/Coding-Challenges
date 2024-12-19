with open("input", "r") as file:
    stripes, towels = file.read().split("\n\n")
    stripes = stripes.split(", ")
    towels = towels.split("\n")

print(stripes)
print(towels)

memo = {}


def is_possible(towel):
    if towel in memo:
        return memo[towel]

    if towel == "":
        return 1

    ways = 0
    for sub in range(1, len(towel) + 1):
        if towel[:sub] in stripes:
            ways += is_possible(towel[sub:])

    memo[towel] = ways
    return ways


results = {}
for towel in towels:
    results[towel] = is_possible(towel)

t = 0
for s, n in results.items():
    if n > 0:
        t += n
print(t)
