with open("a", 'r') as file:
    content = file.read()

names = [name.strip().replace('"', '') for name in content.split(',')]

total = 0
for i, name in enumerate(sorted(names)):
    total += (i + 1) * sum(ord(c) - ord('A') + 1 for c in name)

print(total)