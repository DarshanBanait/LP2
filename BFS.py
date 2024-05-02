from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        if u in self.adj_list:
            self.adj_list[u].append(v)
        else:
            self.adj_list[u] = [v]

        if v in self.adj_list:
            self.adj_list[v].append(u)
        else:
            self.adj_list[v] = [u]

    def bfs(self, start):
        visited = set()
        queue = deque([start])

        while queue:
            node = queue.popleft()
            if node not in visited:
                print(node)  # Process the current vertex (in this example, we'll print it)
                visited.add(node)
                for neighbor in self.adj_list.get(node, []):
                    if neighbor not in visited:
                        queue.append(neighbor)

def main():
    # Create an empty graph
    g = Graph()

    # Take input for the number of vertices
    num_vertices = int(input("Enter the number of vertices: "))

    # Take input for graph edges
    print("Enter edges (format: u v, where u and v are vertices):")
    for _ in range(num_vertices - 1):  # For a connected graph with num_vertices, there are num_vertices - 1 edges
        u, v = map(int, input().split())
        g.add_edge(u, v)

    # Prompt user for the starting vertex for BFS
    start_vertex = int(input("Enter the starting vertex for BFS: "))

    # Perform BFS starting from the specified vertex
    print("BFS traversal starting from vertex", start_vertex)
    g.bfs(start_vertex)

if __name__ == "__main__":
    main()