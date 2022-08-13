from collections import deque

def buildgraph(nodes, edges):
    graph = {}

    for node in nodes:
        graph[node] = list()

    for u,v in edges:
        graph[u].append(v)

    return graph

def print_graph(graph):
    for node, edges in graph.items():
        print(node, end=': ')
        print(edges)

def topological_sort(graph):
    visited = set()
    order = deque()

    def _topological_sort(node):
        if node not in visited:
            visited.add(node)
            for neighbour in graph[node]:
                _topological_sort(neighbour)
            order.appendleft(node)

    for node in graph:
        _topological_sort(node)

    return order

if __name__ == "__main__":
    nodes = ['a','b','c','d','e','f']
    edges = [ ('a','d'), ('f','b'), ('b','d'), ('f','a'), ('d','c') ]

    graph = buildgraph(nodes, edges)
    print_graph(graph)
    print()
    print(topological_sort(graph))
