groups = open('input').read().split('\n\n')
shapes = [g[3:].split('\n') for g in groups[:6]]
shape_sizes = {i: ''.join(shape).count('#') for i, shape in enumerate(shapes)}

total = 0
for region in groups[-1].split('\n'):
    size, quantity = region.split(': ')
    width, length = [int(s) for s in size.split('x')]
    quantity = [int(q) for q in quantity.split()]

    total_present_size = sum(n * shape_sizes[i] for i, n in enumerate(quantity))
    total_grid_size = width * length

    # chicanery
    total += 1 if total_present_size * 1.2 < total_grid_size else 0

print(total)
