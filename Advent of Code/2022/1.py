calories = [sum(map(int, elf.splitlines())) for elf in open('input').read().split('\n\n')]
calories = sorted(calories)
print(sum(calories[-3:]))
