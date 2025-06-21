from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def dfs_util(self, vertex, visited, result):
        visited[vertex] = True
        result.append(vertex)
        
        for neighbor in self.graph[vertex]:
            if not visited[neighbor]:
                self.dfs_util(neighbor, visited, result)
    
    def dfs(self, start):
        visited = [False] * (max(self.graph) + 1 if self.graph else 1)
        result = []
        
        self.dfs_util(start, visited, result)
        return result

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("DFS starting from vertex 2:")
print(g.dfs(2))