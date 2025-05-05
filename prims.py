def prims_algorithm(graph, V):
    selected = [False] * V
    num_edges = 0
    selected[0] = True  # Start from vertex 0

    print("Edge \tWeight")
    while num_edges < V - 1:
        min_weight = float('inf')  # Use infinity instead of sys.maxsize
        x = 0  # source vertex
        y = 0  # destination vertex

        for i in range(V):
            if selected[i]:
                for j in range(V):
                    if not selected[j] and graph[i][j]:
                        if min_weight > graph[i][j]:
                            min_weight = graph[i][j]
                            x = i
                            y = j
        print(f"{x} - {y} \t{graph[x][y]}")
        selected[y] = True
        num_edges += 1

# Predefined adjacency matrix of graph (5 vertices)
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]
V = 5  # Number of vertices

prims_algorithm(graph, V)