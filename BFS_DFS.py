'''
         Graph :    

        0
       / \
      1   2
     /     \
    4       3
           / \
          6   5  
'''

graph = {
    '0': ['1', '2'],
    '1': ['0', '4'],
    '2': ['0', '3'],
    '4': ['1'],
    '3': ['2', '6', '5'],
    '6': ['3'],
    '5': ['3']
}

def bfs(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)

    print("\nFollowing is the Breadth-First Search:")
    while queue:
        node = queue.pop(0)
        print(node, end=" ")
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    print()

def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
        print("\nFollowing is the Depth-First Search:")

    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(graph, neighbour, visited)

# Run DFS and BFS
dfs(graph, '0')
print()
bfs(graph, '0')
