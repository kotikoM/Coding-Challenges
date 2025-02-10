monkeys = []
modulo = 1


def send(to, item):
    for m in monkeys:
        if m.name == to:
            m.__receive__(item)
            break


class Monkey:
    def __init__(self, name, items, op, test, true, false):
        self.name = name
        self.items = items
        self.op = op
        self.test = test
        self.true = true
        self.false = false
        self.inspected = 0

    def __receive__(self, item):
        self.items.append(item)

    def __play__(self):
        new_items = [((self.op(item)) % modulo) for item in self.items]
        self.inspected += len(new_items)
        self.items = []

        for i in new_items:
            send(self.true if self.test(i) else self.false, i)

    def __repr__(self):
        return f"Monkey {self.name}, {self.inspected}"


for monkey in open('input').read().split('\n\n'):
    name, items, op, test, true, false = monkey.split('\n')

    name = name[7:-1]
    items = list(map(int, items[18:].strip().split(',')))

    operator, operand = op[op.index('old') + 4:].split()
    if operand == 'old':
        if operator == "*":
            func = lambda old: old * old
        else:
            func = lambda old: old + old
    else:
        if operator == "*":
            func = lambda old, val=int(operand): old * val
        else:
            func = lambda old, val=int(operand): old + val

    divisible_by = int(test.split()[-1])
    modulo *= divisible_by
    test = lambda n, div_by=divisible_by: n % div_by == 0

    true_monkey = true.split()[-1]
    false_monkey = false.split()[-1]

    monkeys.append(Monkey(name, items, func, test, true_monkey, false_monkey))

for _ in range(10_000):
    for m in monkeys:
        m.__play__()

inspects = []
for m in monkeys:
    inspects.append(m.inspected)

a, b = sorted(inspects)[len(inspects) - 2:]
print(a * b)
