from collections import deque

lines = open('input').read().split('\n')
broadcasts = None
flip_flops = {}
conjunctions = {}
for line in lines:
    if 'broadcaster ->' in line:
        broadcasts = [(i, 'L', 'brd') for i in line[15:].split(', ')]
        continue

    k, v = line[1:].split(' -> ')
    v = v.split(', ')
    if line[0] == '%':
        flip_flops[k] = ('OFF', v)
    elif line[0] == '&':
        inputs = []
        for l in lines:
            if k in l.split(' -> ')[1]:
                inputs.append((l[1:].split(' -> ')[0], 'L'))

        conjunctions[k] = (inputs, v)


def press(l, h):
    print('button -low-> brd')
    l += 1
    q = deque(broadcasts)
    while q:
        node, signal, sender = q.popleft()
        pretty_signal = 'high' if signal == 'H' else 'low'
        print(f'{sender} -{pretty_signal}> {node}')

        if signal == 'L':
            l += 1
        elif signal:
            h += 1

        if node in flip_flops:
            if signal == 'H':
                continue

            current_state, outputs = flip_flops[node]
            next_state = 'OFF' if current_state == 'ON' else 'ON'
            next_signal = 'H' if next_state == 'ON' else 'L'
            flip_flops[node] = (next_state, outputs)

            for o in outputs:
                q.append((o, next_signal, node))

        elif node in conjunctions:
            inputs, outputs = conjunctions[node]
            for i in range(len(inputs)):
                input_node, prev_signal = inputs[i]
                if input_node == sender:
                    inputs[i] = (input_node, signal)

            next_signal = 'H'
            if all([s == 'H' for _, s in inputs]):
                next_signal = 'L'

            for o in outputs:
                q.append((o, next_signal, node))

    return l, h

l, h = 0, 0
for _ in range(1000):
    l, h = press(l, h)
print(l, h)
print(l * h)
