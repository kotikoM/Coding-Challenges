input = "70949 6183 4 3825336 613971 0 15 182"
stones = [int(x) for x in input.split(" ")]

steps = {}


def blink(stone, t):
    if (stone, t) in steps:
        return steps[(stone, t)]

    if t == 0:
        res = 1
    elif stone == 0:
        res = blink(1, t - 1)
    elif len(str(stone)) % 2 == 0:
        stone_str = str(stone)
        left = int(stone_str[:len(stone_str) // 2])
        right = int(stone_str[len(stone_str) // 2:])

        res = blink(left, t - 1) + blink(right, t - 1)
    else:
        res = blink(stone * 2024, t - 1)

    steps[(stone, t)] = res
    return res


def plutonian_pebble(t):
    return sum(blink(x, t) for x in stones)


print(plutonian_pebble(25))
print(plutonian_pebble(75))
