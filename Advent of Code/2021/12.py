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


def find_paths(current_node, path, visited):
    global total

    if current_node.value == 'end':
        total += 1
        print(path + [current_node.value])
        return

    neighbors = current_node.edges_to

    for n in neighbors:
        if n.value.islower() and n.value in visited:
            continue

        new_visited = visited.copy()
        if n.value.islower():
            new_visited.append(n.value)

        find_paths(n, path + [current_node.value], new_visited)


nodes = {}
for line in open('input').read().splitlines():
    node1, node2 = line.split('-')
    if node1 not in nodes:
        nodes[node1] = Node(node1)
    if node2 not in nodes:
        nodes[node2] = Node(node2)

    nodes[node1].add_child(nodes[node2])
    nodes[node2].add_child(nodes[node1])

find_paths(nodes['start'], [], ['start'])
print(total)
