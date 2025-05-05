# Simple Kruskal's Algorithm

# Function to find parent of a node
def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

# Function to union two sets
def union(parent, u, v):
    root_u = find(parent, u)
    root_v = find(parent, v)
    parent[root_v] = root_u

# Define graph as list of edges: (weight, node1, node2)
edges = [
    (1, 'A', 'B'),
    (3, 'A', 'C'),
    (2, 'B', 'C'),
    (4, 'B', 'D'),
    (5, 'C', 'D')
]

# Extract unique nodes
nodes = set()
for edge in edges:
    nodes.add(edge[1])
    nodes.add(edge[2])

# Initialize parent for each node
parent = {node: node for node in nodes}

# Sort edges by weight
edges.sort()

# Kruskal’s Algorithm
mst = []
total_cost = 0

for weight, u, v in edges:
    if find(parent, u) != find(parent, v):
        union(parent, u, v)
        mst.append((u, v, weight))
        total_cost += weight

# Print Minimum Spanning Tree
print("Edges in the Minimum Spanning Tree:")
for u, v, weight in mst:
    print(f"{u} - {v} : {weight}")

print("Total Cost of MST:", total_cost)