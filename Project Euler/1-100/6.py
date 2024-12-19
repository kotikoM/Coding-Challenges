
res = 0

limit = 100
for i in range(1, limit + 1):
    for j in range(1, limit + 1):
        if i != j:
            res += i * j

print(res)
