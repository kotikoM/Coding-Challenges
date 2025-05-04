lines = open('input').read().splitlines()

bin = ''.join(
    '1' if sum(1 if line[i] == '1' else -1 for line in lines) > 0
    else '0' for i in range(len(lines[0]))
)

int1 = int(bin, 2)
int2 = (1 << len(bin)) - 1 - int1

print(int1 * int2)
