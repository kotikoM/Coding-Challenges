import networkx as nx

graph = nx.Graph()
for line in open('input').read().splitlines():
    left, right = line.split(':')
    for r in right.strip().split():
        graph.add_edge(left, r)
        graph.add_edge(r, left)

graph.remove_edges_from(nx.minimum_edge_cut(graph))
first, second = nx.connected_components(graph)
print(len(first) * len(second))