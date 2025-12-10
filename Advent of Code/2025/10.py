from itertools import combinations_with_replacement
import re

lights, all_buttons = [], []
for line in open('input').read().splitlines():
    light = re.search(r'\[(.*?)\]', line).group(1)
    lights.append(light)

    parens = re.findall(r'\((.*?)\)', line)
    buttons = [list(map(int, p.split(','))) if ',' in p else [int(p)] for p in parens]
    all_buttons.append(buttons)

total_presses = []
for light, buttons in zip(lights, all_buttons):
    target = list(light)
    n = len(light)
    i = 1
    found = False

    while not found:
        button_combinations = combinations_with_replacement(buttons, i)

        for combo in button_combinations:
            result = ['.'] * n

            for button_set in combo:
                for b in button_set:
                    result[b] = '#' if result[b] == '.' else '.'

            if result == target:
                print("  → Found match using", i, "presses:", combo)
                found = True
                total_presses.append(i)
                break

        i += 1

print(sum(total_presses))
