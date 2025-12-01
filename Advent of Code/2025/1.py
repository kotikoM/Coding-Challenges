current_position = 50
zero_count = 0

for line in open('input').read().strip().split('\n'):
    direction = line[0]
    distance = int(line[1:])

    if direction == 'R':
        steps_to_zero = (100 - current_position) % 100
        if steps_to_zero == 0 and current_position == 0:
            steps_to_zero = 100
        elif steps_to_zero == 0:
            steps_to_zero = 100
    else:
        steps_to_zero = current_position

        if steps_to_zero == 0 and current_position == 0:
            steps_to_zero = 100
        elif steps_to_zero == 0:
            steps_to_zero = 100

    if distance >= steps_to_zero:
        remaining_distance = distance - steps_to_zero
        additional_zeros = remaining_distance // 100

        rotation_zeros = 1 + additional_zeros
        zero_count += rotation_zeros

    if direction == 'R':
        current_position = (current_position + distance) % 100
    else:
        current_position = (current_position - distance) % 100

print(zero_count)
