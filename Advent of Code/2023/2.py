import re
from math import prod


def calculate_power(game):
    subsets = game.split(";")

    max_red = max_green = max_blue = 0

    for subset in subsets:
        red = sum(map(int, re.findall(r"(\d+)\sred", subset)))
        green = sum(map(int, re.findall(r"(\d+)\sgreen", subset)))
        blue = sum(map(int, re.findall(r"(\d+)\sblue", subset)))

        max_red = max(max_red, red)
        max_green = max(max_green, green)
        max_blue = max(max_blue, blue)

    power = prod([max_red, max_green, max_blue])
    return power

total_power = 0
with open("input") as file:
    for game in file.read().splitlines():
        total_power += calculate_power(game)

print("Sum of the power of minimum sets:", total_power)
