def water_jug_problem(jug1_cap, jug2_cap, target):
    visited = set()
    queue = [(0, 0, [])]
    
    while queue:
        jug1, jug2, path = queue.pop(0)
        
        if jug1 == target or jug2 == target:
            return path + [(jug1, jug2)]
        
        if (jug1, jug2) in visited:
            continue
            
        visited.add((jug1, jug2))
        
        queue.append((jug1_cap, jug2, path + [(jug1, jug2, "Fill jug1")]))
        queue.append((jug1, jug2_cap, path + [(jug1, jug2, "Fill jug2")]))
        queue.append((0, jug2, path + [(jug1, jug2, "Empty jug1")]))
        queue.append((jug1, 0, path + [(jug1, jug2, "Empty jug2")]))
        
        pour_amount = min(jug1, jug2_cap - jug2)
        queue.append((jug1 - pour_amount, jug2 + pour_amount, path + [(jug1, jug2, "Pour jug1 to jug2")]))
        
        pour_amount = min(jug2, jug1_cap - jug1)
        queue.append((jug1 + pour_amount, jug2 - pour_amount, path + [(jug1, jug2, "Pour jug2 to jug1")]))
    
    return None

jug1_capacity = 4
jug2_capacity = 3
target_amount = 2

solution = water_jug_problem(jug1_capacity, jug2_capacity, target_amount)

if solution:
    print(f"Solution to get {target_amount} liters:")
    for step in solution:
        if len(step) > 2:
            jug1, jug2, action = step
            print(f"{action}: Jug1={jug1}, Jug2={jug2}")
        else:
            jug1, jug2 = step
            print(f"Final state: Jug1={jug1}, Jug2={jug2}")
else:
    print("No solution exists.")