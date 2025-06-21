import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position  # (x, y)
        self.parent = parent
        
        self.g = 0  # Distance from start
        self.h = 0  # Heuristic (distance to goal)
        self.f = 0  # Total cost (g + h)
    
    def __eq__(self, other):
        return self.position == other.position
    
    def __lt__(self, other):
        return self.f < other.f

def astar(maze, start, end):
    # Create start and end nodes
    start_node = Node(start)
    end_node = Node(end)
    
    # Initialize open and closed lists
    open_list = []
    closed_list = []
    
    # Add the start node to the open list
    heapq.heappush(open_list, (start_node.f, id(start_node), start_node))
    
    # Loop until the end is found
    while open_list:
        # Get the current node with the lowest f value
        current_f, _, current_node = heapq.heappop(open_list)
        
        # Add to closed list
        closed_list.append(current_node)
        
        # Check if goal is reached
        if current_node.position == end_node.position:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Return reversed path
        
        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # Adjacent squares (up, down, left, right)
            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
            
            # Check if within bounds
            if (node_position[0] < 0 or node_position[0] >= len(maze) or 
                node_position[1] < 0 or node_position[1] >= len(maze[0])):
                continue
            
            # Check if walkable
            if maze[node_position[0]][node_position[1]] != 0:
                continue
            
            # Create new node
            new_node = Node(node_position, current_node)
            
            # Append to children
            children.append(new_node)
        
        # Loop through children
        for child in children:
            # Check if child is in closed list
            if any(child.position == closed_child.position for closed_child in closed_list):
                continue
            
            # Calculate f, g, and h values
            child.g = current_node.g + 1
            # Heuristic - Manhattan distance
            child.h = abs(child.position[0] - end_node.position[0]) + abs(child.position[1] - end_node.position[1])
            child.f = child.g + child.h
            
            # Check if child is already in open list with a lower g value
            if any(child.position == open_node.position and child.g > open_node.g 
                   for _, _, open_node in open_list):
                continue
            
            # Add the child to the open list
            heapq.heappush(open_list, (child.f, id(child), child))
    
    return None  # No path found

# Example usage
maze = [
    [0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0]
]

start = (0, 0)
end = (4, 5)

path = astar(maze, start, end)
if path:
    print(f"Path found: {path}")
    
    # Print the maze with the path
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if (i, j) in path:
                print("P", end=" ")
            else:
                print(maze[i][j], end=" ")
        print()
else:
    print("No path found")