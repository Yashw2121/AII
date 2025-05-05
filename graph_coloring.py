graph = [
[1,2],
[0,2,3],
[0,1,3],
[1,2,4],
[3]
]

Vert = len(graph)
#print(v)

def graph_coloring(graph,Vert):
	result = [-1] * Vert
	#print("Result : ",result)
	result[0] = 0
	available = [False] * Vert
	#print("available : ",available)
	
	for u in range(1,Vert):
		for v in graph[u]:
			if result[v] != -1:
				available[result[v]] = True
				
		for color in range(0,Vert):
			if not available[color]:
				break
		
		result[u] = color
		
		for v in graph[u]:
			if result[v] != -1:
				available[result[v]] = False
		
		#print("available : ",available)
		#print("Result : ",result)
	
	for u in range(0,Vert):
		
		print(f"Vertex {u} --> Color {result[u]}")

graph_coloring(graph,Vert)	