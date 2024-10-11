import heapq

from setuptools.msvc import SystemInfo

from algorithm.util.visualize import visualize_graph


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
            if current_state in graph.keys():
                for neighbor, cost in graph[current_state]:
                    total_cost = current_cost + cost
                    if neighbor not in visited:
                        heapq.heappush(frontier, (total_cost, path + [neighbor]))

    # If the goal is not reachable, return []
    return []

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
