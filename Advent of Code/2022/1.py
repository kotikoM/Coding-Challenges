calories = [sum(map(int, elf.splitlines())) for elf in open('input').read().split('\n\n')]
print(max(calories))