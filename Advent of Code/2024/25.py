all_data = open("input").read().split("\n\n")

locks = []
keys = []

for item in all_data:
    lines = item.strip().split("\n")

    # locks
    if lines[0] == "#####":
        lock = []

        for c in range(len(lines[0])):
            for r in range(len(lines)):
                if lines[r][c] == ".":
                    lock.append(r - 1)
                    break
            else:
                lock.append(len(lines) - 1)

        locks.append(lock)

    # keys
    if lines[-1] == "#####":
        key = []
        for c in range(len(lines[0])):
            for r in range(len(lines) - 1, -1, -1):
                if lines[r][c] == ".":
                    key.append(len(lines) - r - 2)
                    break
            else:
                key.append(len(lines) - 1)
        keys.append(key)

print("Length of keys:", len(keys))
print("Length of locks:", len(locks))

for i, lock in enumerate(locks):
    print(f"Lock {i + 1}: {lock}")

for i, key in enumerate(keys):
    print(f"Lock {i + 1}: {key}")


fit = set()
for key in keys:
    for lock in locks:
        for i in range(5):
            if key[i] + lock[i] > 5:
                break
        else:
            fit.add((tuple(key), tuple(lock)))

print(fit)
print(len(fit))
