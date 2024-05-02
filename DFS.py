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

    def dfs_recursive(self, start, visited=None):
        if visited is None:
            visited = set()

        visited.add(start)
        print(start)  # Process the current vertex (in this example, we'll print it)

        for neighbor in self.adj_list.get(start, []):
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited)

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

    # Prompt user for the starting vertex for DFS
    start_vertex = int(input("Enter the starting vertex for DFS: "))

    # Perform DFS starting from the specified vertex
    print("DFS traversal starting from vertex", start_vertex)
    g.dfs_recursive(start_vertex)

if __name__ == "__main__":
    main()