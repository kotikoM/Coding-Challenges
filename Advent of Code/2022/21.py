import sympy

monkeys = {"humn": sympy.Symbol("x")}

ms = [line.strip() for line in open('input')]

ops = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}

for m in ms:
    name, expr = m.split(": ")
    if name in monkeys: continue
    if expr.isdigit():
        monkeys[name] = sympy.Integer(expr)
    else:
        left, op, right = expr.split()
        if left in monkeys and right in monkeys:
            if name == "root":
                print(sympy.solve(monkeys[left] - monkeys[right])[0])
                break
            monkeys[name] = ops[op](monkeys[left], monkeys[right])
        else:
            ms.append(m)
