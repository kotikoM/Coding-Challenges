from collections import defaultdict

# Step 1: Read input and build the adjacency list
lines = open("input").read().splitlines()

connections = defaultdict(list)

for nodes in lines:
    node1, node2 = nodes.split("-")
    connections[node1].append(node2)
    connections[node2].append(node1)


def find_triads(connections):
    triads = set()

    for node in connections:
        neighbors = connections[node]

        for i in range(len(neighbors)):
            for j in range(i + 1, len(neighbors)):
                n1, n2 = neighbors[i], neighbors[j]

                if n2 in connections[n1]:
                    triad = tuple(sorted([node, n1, n2]))
                    triads.add(triad)

    return triads

def bron_kerbosch(R, P, X, graph, cliques):
    if not P and not X:
        cliques.append(R)
        return
    for node in list(P):
        bron_kerbosch(
            R.union({node}),
            P.intersection(graph[node]),
            X.intersection(graph[node]),
            graph,
            cliques,
        )
        P.remove(node)
        X.add(node)

def find_largest_clique(connections):
    graph = {node: set(neighbors) for node, neighbors in connections.items()}
    cliques = []
    bron_kerbosch(set(), set(graph.keys()), set(), graph, cliques)
    largest_clique = max(cliques, key=len)
    return largest_clique


largest_clique = find_largest_clique(connections)
password = ",".join(sorted(largest_clique))

print("The password to get into the LAN party is:", password)
