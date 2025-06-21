import heapq
from collections import deque
import copy

class PuzzleState:
    def __init__(self, board, moves=0, prev_state=None):
        self.board = board
        self.moves = moves
        self.prev_state = prev_state
        self.hash_val = hash(str(board))
        
    def __eq__(self, other):
        return self.board == other.board
    
    def __hash__(self):
        return self.hash_val
    
    def __lt__(self, other):
        return self.moves + self.get_manhattan_distance() < other.moves + other.get_manhattan_distance()
    
    def get_blank_pos(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return i, j
    
    def is_goal(self):
        goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        return self.board == goal
    
    def get_possible_moves(self):
        i, j = self.get_blank_pos()
        moves = []
        
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < 3 and 0 <= nj < 3:
                new_board = copy.deepcopy(self.board)
                new_board[i][j], new_board[ni][nj] = new_board[ni][nj], new_board[i][j]
                moves.append(PuzzleState(new_board, self.moves + 1, self))
        
        return moves
    
    def get_manhattan_distance(self):
        distance = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != 0:
                    val = self.board[i][j]
                    goal_i, goal_j = (val - 1) // 3, (val - 1) % 3
                    distance += abs(i - goal_i) + abs(j - goal_j)
        return distance

def solve_puzzle(initial_board):
    initial_state = PuzzleState(initial_board)
    
    if initial_state.is_goal():
        return [initial_state]
    
    open_set = []
    closed_set = set()
    
    heapq.heappush(open_set, initial_state)
    
    while open_set:
        current = heapq.heappop(open_set)
        
        if current.is_goal():
            path = []
            while current:
                path.append(current)
                current = current.prev_state
            return path[::-1]
        
        closed_set.add(current)
        
        for next_state in current.get_possible_moves():
            if next_state in closed_set:
                continue
                
            heapq.heappush(open_set, next_state)
    
    return None

initial_board = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

solution = solve_puzzle(initial_board)
if solution:
    for i, state in enumerate(solution):
        print(f"Step {i}:")
        for row in state.board:
            print(row)
        print()
else:
    print("No solution found.")