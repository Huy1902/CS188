def depth_first_search(graph : dict, start : int) -> set[str]:
    """
    >>> input_G = { "A": ["B", "C", "D"], "B": ["A", "D", "E"],
    ... "C": ["A", "F"], "D": ["B", "D"], "E": ["B", "F"],
    ... "F": ["C", "E", "G"], "G": ["F"] }
    >>> output_G = list({'A', 'B', 'C', 'D', 'E', 'F', 'G'})
    >>> all(x in output_G for x in list(depth_first_search(input_G, "A")))
    True
    >>> all(x in output_G for x in list(depth_first_search(input_G, "G")))
    True
    """
    visited, stack = set(), [start]
    visited.add(start)
    while stack:
        vertex = stack.pop()
        visited.add(vertex)
        for adj in graph[vertex]:
            if adj not in visited:
                stack.append(adj)

    return visited

G = {
    "A" : ["B", "C"],
    "B" : ["A", "D", "E"],
    "C" : ["A", "F"],
    "D" : ["B"],
    "E" : ["B", "F"],
    "F" : ["C", "E"]
}

if __name__ == "__main__":

    print(depth_first_search(G, "A"))