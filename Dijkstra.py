import heapq

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, u, v, weight):
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []

        self.adjacency_list[u].append((v, weight))
        self.adjacency_list[v].append((u, weight))

    def dijkstra_mst(self, source):
        min_heap = []  # Priority queue to store vertices based on their minimum distance
        heapq.heappush(min_heap, (0, source))  # Push the source vertex with distance 0
        mst_cost = 0  # Total cost of the MST
        mst_edges = []  # List to store MST edges

        # Dictionary to keep track of minimum distance to each vertex
        min_distance = {vertex: float('inf') for vertex in self.adjacency_list}
        min_distance[source] = 0

        # Set to track visited vertices
        visited = set()

        while min_heap:
            current_distance, current_vertex = heapq.heappop(min_heap)

            if current_vertex in visited:
                continue

            # Mark the current vertex as visited
            visited.add(current_vertex)
            mst_cost += current_distance

            if current_vertex != source:
                mst_edges.append((min_distance[current_vertex], current_vertex))

            # Explore neighbors of the current vertex
            for neighbor, weight in self.adjacency_list[current_vertex]:
                if neighbor not in visited and weight < min_distance[neighbor]:
                    min_distance[neighbor] = weight
                    heapq.heappush(min_heap, (weight, neighbor))

        return mst_cost, mst_edges

def get_input_edges():
    edges = []
    while True:
        print("Enter an edge (format: u v weight) or enter 'done' to finish:")
        user_input = input().strip()
        if user_input.lower() == 'done':
            break
        try:
            u, v, weight = user_input.split()
            weight = int(weight)
            edges.append((u, v, weight))
        except ValueError:
            print("Invalid input format. Please try again.")
    return edges

def main():
    # Create a new graph instance
    graph = Graph()

    # Prompt the user to enter edges and weights
    edges = get_input_edges()

    # Add edges to the graph
    for u, v, weight in edges:
        graph.add_edge(u, v, weight)

    # Specify the source vertex for MST
    source_vertex = input("Enter the source vertex for MST: ").strip()

    # Find the Minimal Spanning Tree (MST) using Dijkstra's algorithm
    if source_vertex in graph.adjacency_list:
        mst_cost, mst_edges = graph.dijkstra_mst(source_vertex)

        # Display the Minimal Spanning Tree (MST) cost and edges
        print("Minimal Spanning Tree (MST) Cost:", mst_cost)
        print("Minimal Spanning Tree (MST) Edges:")
        for cost, edge in mst_edges:
            print(edge)
    else:
        print("Invalid source vertex. Please enter a valid vertex.")

if __name__ == "__main__":
    main()
