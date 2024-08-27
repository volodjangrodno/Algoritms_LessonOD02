class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []

        self.graph[u].append(v)

    def print_graph(self):
        # {0: [1, 2], 1: [0, 3], 2: [0], 3: [1]}
        for node in self.graph:
            print(node, "->", "->".join(map(str, self.graph[node])))


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

g.print_graph()
