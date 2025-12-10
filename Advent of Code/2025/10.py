import z3

total_button_sum = 0
for line in open('input').read().splitlines():
    parts = line.split()
    button_strings = parts[1:-1]
    expected_joltage_string = parts[-1]

    # Parse button connections
    button_indices = []
    for button_str in button_strings:
        indices = [int(x) for x in button_str[1:-1].split(',')]
        button_indices.append(indices)

    # Parse expected output
    expected_joltage = [int(x) for x in expected_joltage_string[1:-1].split(',')]

    # Create integer variables for each button
    button_vars = [z3.Int(f'Button{i}') for i in range(len(button_strings))]

    # Create equations linking buttons to expected output
    equations = []
    for i in range(len(expected_joltage)):
        involved_buttons = [button_vars[j] for j in range(len(button_indices)) if i in button_indices[j]]
        equations.append(sum(involved_buttons) == expected_joltage[i])

    # Set up the solver
    solver = z3.Optimize()
    solver.minimize(sum(button_vars))
    for eq in equations:
        solver.add(eq)
    for var in button_vars:
        solver.add(var >= 0)

    # Solve
    assert solver.check()
    model = solver.model()
    for var in model.decls():
        total_button_sum += model[var].as_long()

print(total_button_sum)
