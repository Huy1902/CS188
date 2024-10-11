#Reference: GreekforGreek
import networkx as nx
import matplotlib.pyplot as plt

def create_graph_with_cost(graph : dict) -> nx.DiGraph:
    G = nx.DiGraph()
    # Adding nodes and edges to the graph
    for node, edges in graph.items():
        for neighbor, cost in edges:
            G.add_edge(node, neighbor, weight=cost)
    return G

def create_grpah_with_no_cost(graph : dict) -> nx.DiGraph:
    G = nx.DiGraph()
    # Adding nodes and edges to the graph
    for node, edges in graph.items():
        for neighbor in edges:
            G.add_edge(node, neighbor)
    return G

def visualize_graph(graph : dict, path : list, with_cost : bool = True, pos : dict = None):
    if with_cost:
        G = create_graph_with_cost(graph)
    else:
        G = create_grpah_with_no_cost(graph)

    if pos is None:
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

    plt.title("Path Visualization")
    plt.show()