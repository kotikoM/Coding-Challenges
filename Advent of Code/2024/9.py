with open('input', 'r') as file:
    disk = list(file.read())

file_id = 0
file = []  # list of position, size, file_id
free = []  # list of position, size
s = []     # string of encoded disk
pos = 0
part2 = False

for i, c in enumerate(disk):
    if i % 2 == 0:
        if part2:
            file.append((pos, int(c), file_id))
        for i in range(int(c)):
            s.append(file_id)
            if not part2:
                file.append((pos, 1, file_id))
            pos += 1
        file_id += 1
    else:
        free.append((pos, int(c)))
        for i in range(int(c)):
            s.append(".")
            pos += 1

print("S:", s)

# compacting logic
for (file_pos, file_size, file_id) in reversed(file):
    for space_i, (space_pos, space_size) in enumerate(free):
        if space_pos < file_pos and file_size <= space_size:
            for i in range(file_size):
                s[file_pos + i] = "."
                s[space_pos + i] = file_id
            free[space_i] = (space_pos + file_size, space_size - file_size)
            break

total = 0
for i, c in enumerate(s):
    if not c == ".":
        total += i * int(c)

print("S:", s)
print("Total:", total)
