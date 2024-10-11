import heapq
from algorithm.util.visualize import visualize_graph

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['I', 'J'],
    'F': ['K', 'M', 'E'],
    'G': ['L', 'M'],
    'H': [],
    'I': [],
    'J': [],
    'K': [],
    'L': [],
    'M': []
}

heuristic = {
    'A': 8, # Start state
    'B': 6,
    'C': 7,
    'D': 5,
    'E': 4,
    'F': 5,
    'G': 4,
    'H': 3,
    'I': 2,
    'J': 1,
    'K': 3,
    'L': 2,
    'M': 0 # Goal state
}

pos = {
    'A': (0, 0),
    'B': (-1, 1),
    'C': (1, 1),
    'D': (-1.5, 2),
    'E': (-0.5, 2),
    'F': (0.5, 2),
    'G': (1.5, 2),
    'H': (-2, 3),
    'I': (-1, 3),
    'J': (0, 3),
    'K': (1, 3),
    'L': (2, 3),
    'M': (3, 3)
}


def GreedySearch(graph: dict, start: int, goal: int, heuristic: dict) -> list[str]:
    frontier = []
    if start in heuristic.keys():
        heapq.heappush(frontier, (heuristic[start], [start]))
    visited = set()
    while frontier:
        path : list[str]
        _, path = heapq.heappop(frontier)
        current_state = path[-1]
        if current_state == goal:
            return path
        if current_state not in visited:
            visited.add(current_state)
            if current_state in graph.keys():
                for neighbor in graph[current_state]:
                    if neighbor not in visited:
                        heapq.heappush(frontier, (heuristic[neighbor], path + [neighbor]))
    return []

if __name__ == "__main__":
    path = GreedySearch(graph, 'A', 'M', heuristic)
    print(path)
    visualize_graph(graph, path, with_cost=False, pos=pos)