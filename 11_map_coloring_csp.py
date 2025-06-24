def is_safe(graph, colors, v, c):
    for i in range(len(graph)):
        if graph[v][i] == 1 and colors[i] == c:
            return False
    return True

def graph_coloring_util(graph, m, colors, v):
    # If all vertices are assigned colors
    if v == len(graph):
        return True
    
    # Try different colors for vertex v
    for c in range(1, m + 1):
        if is_safe(graph, colors, v, c):
            colors[v] = c
            
            # Recur to assign colors to the rest
            if graph_coloring_util(graph, m, colors, v + 1):
                return True
            
            # If assigning color c doesn't lead to a solution
            colors[v] = 0
    
    # If no color can be assigned
    return False

def graph_coloring(graph, m):
    colors = [0] * len(graph)
    
    if not graph_coloring_util(graph, m, colors, 0):
        print("Solution does not exist")
        return None
    
    return colors

# Example graph represented as adjacency matrix
graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

# Number of colors
m = 3

colors = graph_coloring(graph, m)

if colors:
    print("Graph can be colored using at most", m, "colors")
    print("Color assignment:")
    for v, c in enumerate(colors):
        print(f"Vertex {v}: Color {c}")