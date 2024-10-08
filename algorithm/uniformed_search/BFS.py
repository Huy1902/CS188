from queue import Queue

def bread_first_search(graph: dict, start: int) -> set[str]:
    """
    >>> input_G = { "A": ["B", "C", "D"], "B": ["A", "D", "E"],
    ... "C": ["A", "F"], "D": ["B", "D"], "E": ["B", "F"],
    ... "F": ["C", "E", "G"], "G": ["F"] }
    >>> output_G = list({'A', 'B', 'C', 'D', 'E', 'F', 'G'})
    >>> all(x in output_G for x in list(bread_first_search(input_G, "A")))
    True
    >>> all(x in output_G for x in list(bread_first_search(input_G, "G")))
    True
    """
    visited, queue = set(), Queue()
    visited.add(start)
    queue.put(start)
    while not queue.empty():
        vertex = queue.get()
        for adj in graph[vertex]:
            if adj not in visited:
                visited.add(adj)
                queue.put(adj)


    return visited

if __name__ == "__main__":
    G = {
        "A" : ["B", "C"],
        "B" : ["A", "D", "E"],
        "C" : ["A", "F"],
        "D" : ["B"],
        "E" : ["B", "F"],
        "F" : ["C", "E"]
    }
    print(bread_first_search(G, "A"))