from collections import deque

def is_valid_state(state):
    ml, cl, mr, cr = state
    
    # Check if counts are valid
    if ml < 0 or cl < 0 or mr < 0 or cr < 0:
        return False
    
    # Check if missionaries outnumbered by cannibals
    if (ml > 0 and ml < cl) or (mr > 0 and mr < cr):
        return False
    
    return True

def missionaries_cannibals():
    # Initial state: (missionaries_left, cannibals_left, missionaries_right, cannibals_right, boat_position)
    initial_state = (3, 3, 0, 0, 'left')
    goal_state = (0, 0, 3, 3, 'right')
    
    visited = set()
    queue = deque([(initial_state, [])])
    
    while queue:
        state, path = queue.popleft()
        ml, cl, mr, cr, boat = state
        
        if (ml, cl, mr, cr, boat) == goal_state:
            return path + [state]
        
        if (ml, cl, mr, cr, boat) in visited:
            continue
            
        visited.add((ml, cl, mr, cr, boat))
        
        # Possible moves: (m, c) represents missionaries and cannibals to move
        moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
        
        for m, c in moves:
            if boat == 'left':
                new_state = (ml - m, cl - c, mr + m, cr + c, 'right')
            else:
                new_state = (ml + m, cl + c, mr - m, cr - c, 'left')
            
            new_ml, new_cl, new_mr, new_cr, new_boat = new_state
            
            if is_valid_state((new_ml, new_cl, new_mr, new_cr)):
                queue.append((new_state, path + [state]))
    
    return None

solution = missionaries_cannibals()

if solution:
    print("Solution found:")
    for i, state in enumerate(solution):
        ml, cl, mr, cr, boat = state
        print(f"Step {i}:")
        print(f"Left bank: {ml} missionaries, {cl} cannibals")
        print(f"Right bank: {mr} missionaries, {cr} cannibals")
        print(f"Boat is on the {boat} side\n")
else:
    print("No solution found.")