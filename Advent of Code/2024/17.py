with open("input", "r") as file:
    registers, program = file.read().split("\n\n")

regs = {}
for line in registers.split("\n"):
    key, value = line.split(":")
    regs[key.strip()] = int(value.strip())


def cpu(A, B, C, program):
    def get_combo(op):
        if op in [0, 1, 2, 3]:
            return op
        elif op == 4:
            return A
        elif op == 5:
            return B
        elif op == 6:
            return C

        return -1

    ip = 0
    out = []
    while ip < len(program):
        code = program[ip]
        operand = program[ip + 1]
        combo = get_combo(operand)

        if code == 0:
            denum = 2 ** combo
            A = A // denum
        elif code == 1:
            B = B ^ operand
        elif code == 2:
            B = combo % 8
        elif code == 3:
            if A != 0:
                ip = operand
                continue
        elif code == 4:
            B = B ^ C
        elif code == 5:
            out.append(int(combo % 8))
        elif code == 6:
            denum = 2 ** combo
            B = A // denum
        elif code == 7:
            denum = 2 ** combo
            C = A // denum

        ip += 2
    return out


program = [int(x) for x in program.replace("Program:", "").strip().split(",")]
A, B, C = regs["Register A"], regs["Register B"], regs["Register C"]

out = cpu(A, B, C, program)

print("A: ", A)
print("B: ", B)
print("C: ", C)
print("Instructions:", program)
print("Out: " + ",".join([str(o) for o in out]))
print("--------------")

# Program: 2,4 / 1,2 / 7,5 / 0,3 / 4,7 / 1,7 / 5,5 / 3,0
# (code, operand), combo = get_combo(operand)
# 0.    A = A // 2 ** (combo)
# 1.    B = B ^ operand
# 2.    B = get_combo(operand) % 8
# 3.    if A != 0: ip = operand
# 4.    B = B ^ C
# 5.    ADD int(combo % 8) - MAKE THIS EQUAL TO code
# 6.    B = A // 2 ** combo
# 7.    C = A // 2 ** combo

def find(target, ans):
    if not target: return ans
    for t in range(8):
        a = ans << 3 | t
        b = 0
        c = 0
        output = None

        def combo(operand):
            if 0 <= operand <= 3: return operand
            if operand == 4: return a
            if operand == 5: return b
            if operand == 6: return c
            raise AssertionError(f"unrecognized combo operand {operand}")

        for pointer in range(0, len(program) - 2, 2):
            ins = program[pointer]
            operand = program[pointer + 1]

            if ins == 1:
                b = b ^ operand
            elif ins == 2:
                b = combo(operand) % 8
            elif ins == 3:
                raise AssertionError("program has JNZ inside expected loop body")
            elif ins == 4:
                b = b ^ c
            elif ins == 5:
                output = combo(operand) % 8
            elif ins == 6:
                b = a >> combo(operand)
            elif ins == 7:
                c = a >> combo(operand)

            if output == target[-1]:
                sub = find(target[:-1], a)
                if sub is None: continue
                return sub


print("A value for self-printing:", find(program, 0))
