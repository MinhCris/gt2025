def path_exists(start, end, graph):
    """
    Return True if a path exists in 'graph' from 'start' to 'end', else False.
    Uses a simple Depth-First Search (DFS) approach.
    """
    visited = set()
    stack = [start]

    while stack:
        current = stack.pop()
        if current == end:
            return True
        if current not in visited:
            visited.add(current)
            # Push all neighbors of 'current' onto the stack
            stack.extend(graph.get(current, []))

    return False


if __name__ == "__main__":
    
    graph = {
        1: [2],
        2: [1, 5],
        5: [2],
        3: [6],
        6: [3, 4, 7],
        4: [6, 7],
        7: [4, 6]
    }

    # Ask user for two node inputs
    start_node = int(input("Enter the starting node: "))
    end_node   = int(input("Enter the ending node: "))

    # Check if a path exists
    result = path_exists(start_node, end_node, graph)
    print(result)  # True if path exists, otherwise False
