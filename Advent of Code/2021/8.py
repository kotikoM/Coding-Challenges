#  aaaa
# b    c
# b    c
#  dddd
# e    f
# e    f
#  gggg

total = 0
for l in open('input').read().split('\n'):
    ten, four = l.split(' | ')
    ten, four = ten.split(), four.split()
    total += sum([1 if len(s) in (2, 3, 4, 7) else 0 for s in four])

print(total)
