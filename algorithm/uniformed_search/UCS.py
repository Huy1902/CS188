import heapq
import networkx as nx
import matplotlib.pyplot as plt


def uniform_cost_search(graph : dict, start : int, goal : int) -> list[str]:
    # Priority queue to store the frontier nodes, initialized with the start node
    frontier = [(0, [start])]
    # Dictionary to store the cost of the shortest path to each node
    visited = set()

    while frontier:
        # Pop the node with the lowest cost from the priority queue
        current_cost, path = heapq.heappop(frontier)
        current_state = path[-1]

        # When current_state is visited here, it means this path is
        # minimum path to go to current_state
        if not current_state in visited:
            # If we reached the goal, return the total cost and the path
            visited.add(current_state)
            if current_state == goal:
                return path

            # Explore the neighbors
            for neighbor, cost in graph[current_state]:
                total_cost = current_cost + cost
                if neighbor not in visited:
                    heapq.heappush(frontier, (total_cost, path + [neighbor]))

    # If the goal is not reachable, return []
    return []


def reconstruct_path(visited, start, goal):
    # Reconstruct the path from start to goal by following the visited nodes
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = visited[current][1]  # Get the parent node
    path.reverse()
    return path


def visualize_graph(graph : dict, path : list):
    G = nx.DiGraph()

    # Adding nodes and edges to the graph
    for node, edges in graph.items():
        for neighbor, cost in edges:
            G.add_edge(node, neighbor, weight=cost)

    pos = nx.spring_layout(G)  # Positioning the nodes

    # Drawing the graph
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=15, font_weight='bold',
            edge_color='gray')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=12)

    if path:
        # Highlight the path in red
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2.5)

    plt.title("Uniform Cost Search Path Visualization")
    plt.show()


# Example graph represented as an adjacency list
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 1), ('E', 3)],
    'C': [('F', 5)],
    'D': [('G', 2)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

# Example usage of the UCS function
start_node = 'A'
goal_node = 'G'
path = uniform_cost_search(graph, start_node, goal_node)
visualize_graph(graph, path)
