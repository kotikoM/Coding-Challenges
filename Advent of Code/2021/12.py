class Node:
    def __init__(self, value):
        self.value = value
        self.edges_to = []

    def add_child(self, child):
        self.edges_to.append(child)

    def __repr__(self):
        edges = ', '.join(child.value for child in self.edges_to)
        return f"Node({self.value}) → [{edges}]"


total = 0


def find_paths(current_node, path, visited, visited_twice):
    global total

    if current_node.value == 'end':
        total += 1
        print(path + [current_node.value])
        return

    neighbors = current_node.edges_to

    for n in neighbors:
        if n.value == 'start':
            continue

        is_small = n.value.islower()

        if is_small and n.value in visited:
            if visited_twice:
                continue
            else:
                find_paths(n, path + [current_node.value], visited, True)
        else:
            new_visited = visited.copy()
            if is_small:
                new_visited.append(n.value)

            find_paths(n, path + [current_node.value], new_visited, visited_twice)


nodes = {}
for line in open('input').read().splitlines():
    node1, node2 = line.split('-')
    if node1 not in nodes:
        nodes[node1] = Node(node1)
    if node2 not in nodes:
        nodes[node2] = Node(node2)

    nodes[node1].add_child(nodes[node2])
    nodes[node2].add_child(nodes[node1])

find_paths(nodes['start'], [], ['start'], False)
print(total)
