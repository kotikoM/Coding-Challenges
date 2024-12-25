lines = open("a").read().split("\n")

r = len(lines)
c = len(lines[0])

first = 10_000_000_000
print(r)
print(c)

res = 0
for i in range(r):
    res = (res + int(lines[i]))

print(res)
