Graph_nodes = {
    'A': [('B', 1), ('C', 2)],
    'B': [('D', 3)],
    'C': [('E', 5)],
    'D': [('F', 2)],
    'E': [('G', 3)],
    'F': [('H', 1)],
    'G': [('H', 2)],
    'H': []
}

def get_neighbours(v):
    return Graph_nodes.get(v, [])

def h(n):
    H_val = {
        'A': 5,
        'B': 6,
        'C': 4,
        'D': 3,
        'E': 5,
        'F': 1,
        'G': 0,
        'H': 0
    }
    return H_val[n]

def aStar(start_node, end_node):
    open_list = set([start_node])
    closed_list = set()
    g = {start_node: 0}
    parents = {start_node: start_node}

    while open_list:
        n = None
        for v in open_list:
            if n is None or g[v] + h(v) < g[n] + h(n):
                n = v

        if n == end_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print("Path Found:", path)
            return path

        for (m, weight) in get_neighbours(n):
            if m not in open_list and m not in closed_list:
                open_list.add(m)
                g[m] = g[n] + weight
                parents[m] = n
            else:
                if g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n
                    if m in closed_list:
                        closed_list.remove(m)
                        open_list.add(m)

        open_list.remove(n)
        closed_list.add(n)

    print("Path Does Not Exist!")
    return None

aStar('A', 'H')
