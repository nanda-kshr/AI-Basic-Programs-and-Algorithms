import itertools
import sys

def tsp(graph, s):
    n = len(graph)
    
    # Store all vertices except the starting one
    vertices = []
    for i in range(n):
        if i != s:
            vertices.append(i)
    
    # Store minimum weight Hamiltonian Cycle
    min_path = sys.maxsize
    min_path_order = []
    
    # Generate all permutations of vertices
    permutations = itertools.permutations(vertices)
    
    for perm in permutations:
        current_path_weight = 0
        
        # Calculate weight of current path
        k = s
        current_path = [s]
        
        for j in perm:
            current_path_weight += graph[k][j]
            k = j
            current_path.append(j)
        
        current_path_weight += graph[k][s]
        current_path.append(s)
        
        # Update minimum
        if current_path_weight < min_path:
            min_path = current_path_weight
            min_path_order = current_path
    
    return min_path, min_path_order

# Example graph represented as adjacency matrix
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Starting vertex
s = 0

min_weight, min_path = tsp(graph, s)

print("The shortest path:", ' -> '.join(map(str, min_path)))
print("The minimum weight of the path:", min_weight)