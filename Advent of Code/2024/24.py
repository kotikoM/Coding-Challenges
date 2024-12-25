from collections import deque

terms, instructions = open("input").read().split("\n\n")

regs = {}
for term in terms.split("\n"):
    name, val = term.split(": ")
    regs[name] = int(val)


def part1(instrs):
    q = deque(instrs)
    while q:
        instr = q.popleft()
        val1, op, val2, _, res = instr.split(" ")

        if val1 not in regs or val2 not in regs:
            q.append(instr)
            continue

        val1 = regs[val1]
        val2 = regs[val2]

        out = None
        if op == "AND":
            out = val1 & val2
        elif op == "OR":
            out = val1 | val2
        elif op == "XOR":
            out = val1 ^ val2

        regs[res] = out

    zs = {k: v for k, v in regs.items() if "y" in k}
    sorted_zs = dict(sorted(zs.items(), key=lambda item: int(item[0][1:]), reverse=True))
    binary_string = ''.join(str(value) for value in sorted_zs.values())
    decimal_value = int(binary_string, 2)
    print(decimal_value)
    return binary_string


instrs = instructions.split("\n")
s = part1(instrs)
print(s)
print(s == "1010011110101010001101100100100000011011100110")
# x - 101101000011011001101001111001001111011001101
# y - 100110110001111000000010101010110100000011001
# z - 1010011110101010001101100100100000011011100110
# w - 100110110001111000000010101010110100000011001
