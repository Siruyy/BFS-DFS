class Node:
    def __init__(self, name):
        self.name = name
        self.outgoing_edges = [] 
        self.incoming_edges = []
        self.processed = False
        self.cumulative_incoming_weight = 0
        self.overall_score = 0

class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_edge(self, source, target, weight=1):
        if source not in self.nodes:
            self.nodes[source] = Node(source)
        if target not in self.nodes:
            self.nodes[target] = Node(target)

        edge = Edge(self.nodes[source], self.nodes[target], weight)
        self.nodes[source].outgoing_edges.append(edge)
        self.nodes[target].incoming_edges.append(edge)

    def dfs_util(self, node, depth, visited):
        visited[node.name] = True
        node.processed = True

        for edge in node.incoming_edges:
            if not visited[edge.source.name]:
                self.dfs_util(edge.source, depth + 1, visited)
            node.cumulative_incoming_weight += edge.weight

        node.overall_score = node.cumulative_incoming_weight + depth

    def dfs(self, start):
        visited = {node: False for node in self.nodes.values()}
        self.dfs_util(self.nodes[start], 0, visited)
        highest_score_node = max(self.nodes.values(), key=lambda node: node.overall_score).name
        for node in self.nodes.values():
            print(f"Processing node {node.name} at depth {node.overall_score}, "
                  f"Number of Neighbors: {len(node.outgoing_edges)}")
        print(f"Node with the highest overall score: {highest_score_node}")

    def find_optimal_path(self, start, end):
        visited = {node.name: False for node in self.nodes.values()}
        path = []
        self.find_optimal_path_util(self.nodes[start], self.nodes[end], visited, path)
        return path

    def find_optimal_path_util(self, current_node, target_node, visited, path):
        visited[current_node.name] = True
        path.append(current_node.name)

        if current_node == target_node:
            return

        next_edge = max(current_node.outgoing_edges, key=lambda edge: edge.weight)
        next_node = next_edge.target

        if not visited[next_node.name]:
            self.find_optimal_path_util(next_node, target_node, visited, path)

    def print_optimal_path(self, start, end):
        path = self.find_optimal_path(start, end)
        print(f"Optimal Path from {start} to {end}: {' -> '.join(path)}")

g = Graph()
g.add_edge('A', 'B', 3)
g.add_edge('A', 'C', 2)
g.add_edge('B', 'D', 1)
g.add_edge('C', 'D', 2)
g.add_edge('D', 'E', 5)

print("DFS Traversal with Custom Processing:")
g.dfs('A')

print()
g.print_optimal_path('A', 'E')
