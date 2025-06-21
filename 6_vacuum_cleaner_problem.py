def print_environment(environment, vacuum_pos):
    result = ""
    for i in range(len(environment)):
        if i == vacuum_pos:
            result += "[V]" if environment[i] else "[V_clean]"
        else:
            result += "[dirty]" if environment[i] else "[clean]"
    print(result)

def vacuum_cleaner():
    environment = [1, 1]  # 1: dirty, 0: clean
    vacuum_pos = 0
    actions = []
    
    print("Initial state:")
    print_environment(environment, vacuum_pos)
    
    while True:
        # Check if current position is dirty
        if environment[vacuum_pos] == 1:
            environment[vacuum_pos] = 0
            actions.append(f"Clean square {vacuum_pos}")
            print(f"Cleaning square {vacuum_pos}")
            print_environment(environment, vacuum_pos)
        
        # Check if both squares are clean
        if environment == [0, 0]:
            break
        
        # Move to the other square
        if vacuum_pos == 0:
            vacuum_pos = 1
        else:
            vacuum_pos = 0
            
        actions.append(f"Move to square {vacuum_pos}")
        print(f"Moving to square {vacuum_pos}")
        print_environment(environment, vacuum_pos)
    
    print("\nActions taken:")
    for i, action in enumerate(actions):
        print(f"{i+1}. {action}")
    
    return actions

vacuum_cleaner()