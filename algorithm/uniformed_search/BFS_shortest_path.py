from algorithm.util.visualize import visualize_graph
from queue import Queue

# For graph have same cost at every edge ( regardless cost)
def bread_first_search(graph: dict, start: int, target:int) -> list[str]:
    visited, queue = set(), Queue()
    visited.add(start)
    queue.put([start])
    while not queue.empty():
        path = queue.get()
        vertex = path[-1]
        if vertex == target:
            return path
        for adj in graph[vertex]:
            if not adj[0] in visited:
                visited.add(vertex)
                queue.put(path + [adj[0]])
    return []

demo_graph = {
    "A": [("B", 1), ("C", 1), ("E", 1)],
    "B": [("A", 1), ("D", 1), ("E", 1)],
    "C": [("A", 1), ("F", 1), ("G", 1)],
    "D": [("B", 1)],
    "E": [("A", 1), ("B", 1), ("D", 1)],
    "F": [("C", 1)],
    "G": [("C", 1)],
}

if __name__ == "__main__":
    path = bread_first_search(demo_graph, "G", "F")
    visualize_graph(demo_graph, path)
