from collections import deque

pipes = {}
rates = {}
for line in open('input').read().splitlines():
    name, rate = line[6:8], int(line[line.index('=') + 1: line.index(';')])
    s = 'to valves' if 'to valves' in line else 'to valve'
    _, next_pipes = line.split(s)
    next_pipes = next_pipes.strip().split(', ')
    rates[name] = rate
    pipes[name] = next_pipes

distances_from_k = {}
for name, next_pipes in pipes.items():
    seen = [name]
    distance = []
    q = deque([(name, 0)])
    while q:
        node, dist = q.popleft()

        for next_node in pipes[node]:
            if next_node not in seen:
                seen.append(next_node)
                distance.append((next_node, dist + 1))
                q.append((next_node, dist + 1))

    distances_from_k[name] = distance

max_pressure = 0
def open_pipes(name, pressure_so_far, time_left, left_to_open):
    global max_pressure
    if time_left <= 0 or left_to_open == []:
        max_pressure = max(max_pressure, pressure_so_far)
        return

    for next_pipe, distance in distances_from_k[name]:
        # if next pipe is of interest i.e. it has a positive rate
        # and there is enough time to turn it on
        if next_pipe in left_to_open and time_left - distance >= 1:
            open_pipes(next_pipe,
                       pressure_so_far + rates[next_pipe] * (time_left - distance - 1),
                       time_left - distance - 1,
                       [k for k in left_to_open if k != next_pipe])

    max_pressure = max(max_pressure, pressure_so_far)


openable_pipes = [k for k, v in rates.items() if v > 0]
open_pipes('AA', 0, 30, openable_pipes)

print(max_pressure)
