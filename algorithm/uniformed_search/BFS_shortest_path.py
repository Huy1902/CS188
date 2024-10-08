#Reference: GreekforGreek
import networkx as nx
import matplotlib.pyplot as plt


def visualize_graph(graph : dict, path : list):
    G = nx.DiGraph()

    # Adding nodes and edges to the graph
    for node, edges in graph.items():
        for neighbor in edges:
            G.add_edge(node, neighbor)

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

    plt.show()

from queue import Queue

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
            if not adj in visited:
                visited.add(vertex)
                queue.put(path + [adj])
    return []

demo_graph = {
    "A": ["B", "C", "E"],
    "B": ["A", "D", "E"],
    "C": ["A", "F", "G"],
    "D": ["B"],
    "E": ["A", "B", "D"],
    "F": ["C"],
    "G": ["C"],
}

if __name__ == "__main__":
    path = bread_first_search(demo_graph, "G", "D")
    visualize_graph(demo_graph, path)
