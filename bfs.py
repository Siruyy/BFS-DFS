import tkinter as tk
from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, edges):
        self.graph[node] = edges

    def get_graph(self):
        return self.graph

    def bfs(self, start, callback):
        visited = {node: False for node in self.graph}
        queue = deque([start])
        visited[start] = True

        while queue:
            node = queue.popleft()
            callback(node, "yellow", "red")

            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
                    callback(neighbor, "blue", "blue")

class BFSApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BFS with GUI")

        self.canvas = tk.Canvas(root, width=400, height=300)
        self.canvas.pack()

        self.graph = Graph()
        self.graph.add_edge('A', ['B', 'C'])
        self.graph.add_edge('B', ['A', 'D', 'E'])
        self.graph.add_edge('C', ['A', 'F'])
        self.graph.add_edge('D', ['B'])
        self.graph.add_edge('E', ['B', 'F'])
        self.graph.add_edge('F', ['C', 'E'])

        self.start_button = tk.Button(root, text="Start BFS", command=self.start_bfs)
        self.start_button.pack()

    def start_bfs(self):
        self.clear_canvas()
        self.graph.bfs('A', self.visualize_bfs)

    def visualize_bfs(self, node, node_color, edge_color):
        x, y = self.get_node_position(node)
        radius = 20
        self.draw_edges(node, edge_color)
        self.draw_nodes(node, x, y, radius, node_color)
        self.root.update_idletasks()
        self.root.update()
        self.root.after(500)

    def clear_canvas(self):
        self.canvas.delete("all")

    def draw_nodes(self, node, x, y, radius, color):
        self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, outline=color, fill=color)
        self.canvas.create_text(x, y, text=node, fill="black")

    def draw_edges(self, node, color):
        graph_dict = self.graph.get_graph()
        x1, y1 = self.get_node_position(node)
        for neighbor in graph_dict[node]:
            x2, y2 = self.get_node_position(neighbor)
            self.canvas.create_line(x1, y1, x2, y2, fill=color)

    def get_node_position(self, node):
        positions = {'A': (100, 150), 'B': (200, 50), 'C': (300, 150), 'D': (200, 250), 'E': (100, 250), 'F': (300, 250)}
        return positions[node]

def main():
    root = tk.Tk()
    app = BFSApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()