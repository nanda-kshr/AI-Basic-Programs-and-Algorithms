class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None
    
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        # Check row
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all(spot == letter for spot in row):
            return True
        
        # Check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all(spot == letter for spot in column):
            return True
        
        # Check diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all(spot == letter for spot in diagonal1):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all(spot == letter for spot in diagonal2):
                return True
        
        return False

def minimax(game, maximizing):
    # Base cases
    if game.current_winner == 'X':
        return 1, None  # score, move
    elif game.current_winner == 'O':
        return -1, None
    elif not game.empty_squares():
        return 0, None
    
    if maximizing:
        max_eval = float('-inf')
        best_move = None
        for move in game.available_moves():
            # Make a move
            game.make_move(move, 'X')
            # Recurse
            eval, _ = minimax(game, False)
            # Undo move
            game.board[move] = ' '
            game.current_winner = None
            
            if eval > max_eval:
                max_eval = eval
                best_move = move
        
        return max_eval, best_move
    
    else:
        min_eval = float('inf')
        best_move = None
        for move in game.available_moves():
            # Make a move
            game.make_move(move, 'O')
            # Recurse
            eval, _ = minimax(game, True)
            # Undo move
            game.board[move] = ' '
            game.current_winner = None
            
            if eval < min_eval:
                min_eval = eval
                best_move = move
        
        return min_eval, best_move

def play(game):
    game.print_board()
    
    while game.empty_squares():
        # X is human player
        human_move = int(input("Enter your move (0-8): "))
        if human_move not in game.available_moves():
            print("Invalid move!")
            continue
        
        game.make_move(human_move, 'X')
        game.print_board()
        
        if game.current_winner:
            print("X wins!")
            return
        
        if not game.empty_squares():
            print("It's a tie!")
            return
        
        # O is AI player with minimax
        _, ai_move = minimax(game, False)
        game.make_move(ai_move, 'O')
        
        print(f"AI makes move to {ai_move}")
        game.print_board()
        
        if game.current_winner:
            print("O wins!")
            return

if __name__ == "__main__":
    game = TicTacToe()
    play(game)