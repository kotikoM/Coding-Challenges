triangle = [list(map(int, l.split(" "))) for l in open("a").read().split("\n")]

def add_previous_row(rows):
    if len(rows) == 1:
        return rows

    parents = rows[0]
    children = rows[1]

    for i, c in enumerate(children):
        if i == 0:
            children[i] += parents[0]
        elif i == len(children) - 1:
            children[i] += parents[-1]
        else:
            children[i] += max(parents[i-1], parents[i])

    if len(rows) == 2:
        return children
    return add_previous_row(rows[1:])


print(triangle)
arr = add_previous_row(triangle)
print(arr)
print(max(arr))
