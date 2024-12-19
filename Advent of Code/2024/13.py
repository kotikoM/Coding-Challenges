import re


part2 = False
machines = []
for block in open("input").read().split("\n\n"):
    ax, ay, bx, by, tx, ty = re.findall(r"\d+", block)
    if part2:
        tx = int(tx) + 10000000000000
        ty = int(ty) + 10000000000000
    machine = (int(ax), int(ay), int(bx), int(by), int(tx), int(ty))
    machines.append(machine)


def find_combination(ax, ay, bx, by, tx, ty):
    for b in range(101, -1, -1):
        for a in range(101, -1, -1):
            tokens = 3 * a + b

            rx = a * ax + b * bx
            ry = a * ay + b * by

            if rx == tx and ry == ty:
                print(f"Found combination: Pressed A {a} times, pressed B {b} times")
                return tokens

    return -1


def solve(ax, ay, bx, by, tx, ty):
    # pressed A button - a times
    # pressed B button - b times
    # ax * a  + bx * b = tx
    # ay * a + by * b = ty

    a = (ty * bx - by * tx) / (ay * bx - ax * by)
    b = (tx - ax * a) / bx

    if a % 1 == b % 1 == 0 and a >= 0 and b >= 0:
        return 3 * a + b

    return -1


total = 0
for machine in machines:
    tokens = solve(*machine)
    if tokens != -1:
        total += tokens

print(f"Total number of machines that can be won: {total}")
