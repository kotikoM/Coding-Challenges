import math
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

feed, = [k for k, v in conjunctions.items() if 'rx' in v[1]]
cycle_lengths = {}
seen = {name: 0 for name, v in conjunctions.items() if feed in v[1]}

def press(presses):
    q = deque(broadcasts)
    while q:
        node, signal, sender = q.popleft()

        if node == feed and signal == 'H':
            seen[sender] += 1

            if sender not in cycle_lengths:
                cycle_lengths[sender] = presses
            else:
                assert presses == seen[sender] * cycle_lengths[sender]

            if all(seen.values()):
                ans = 1
                print(cycle_lengths)
                for lengths in cycle_lengths.values():
                    ans = math.lcm(ans, lengths)
                print(ans)
                exit(0)

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


presses = 0
while True:
    presses += 1
    press(presses)
