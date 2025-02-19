monkeys = {}
for line in open('input').read().splitlines():
    name, action = line.split(': ')
    if any(op in action for op in '+-*/'):
        monkeys[name] = ('op', action)
    else:
        monkeys[name] = ('val', int(action))


def evaluate(name):
    type, action = monkeys[name]

    if type == 'val':
        return action
    else:
        m1, op, m2 = action.split()
        return eval(str(evaluate(m1)) + op + str(evaluate(m2)))


print(evaluate('root'))
