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
        # Only need to check if square is an even number (0, 2, 4, 6, 8)
        # these are the only possible square to win a diagonal
        if square % 2 == 0:
            # Main diagonal
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all(spot == letter for spot in diagonal1):
                return True
            # Secondary diagonal
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all(spot == letter for spot in diagonal2):
                return True
        
        return False

def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board()
    
    letter = 'X'  # starting letter
    
    # iterate while the game has empty squares
    while game.empty_squares():
        # get the move from the appropriate player
        if letter == 'O':
            square = o_player(game)
        else:
            square = x_player(game)
        
        if game.make_move(square, letter):
            if print_game:
                print(f'{letter} makes a move to square {square}')
                game.print_board()
                print('')
            
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter
            
            letter = 'O' if letter == 'X' else 'X'
    
    if print_game:
        print('It\'s a tie!')

def get_human_move(game):
    valid_square = False
    val = None
    while not valid_square:
        square = input('Enter your move (0-8): ')
        try:
            val = int(square)
            if val not in game.available_moves():
                raise ValueError
            valid_square = True
        except ValueError:
            print('Invalid square. Try again.')
    
    return val

def get_computer_move(game):
    import random
    return random.choice(game.available_moves())

if __name__ == '__main__':
    x_player = get_human_move
    o_player = get_computer_move
    t = TicTacToe()
    play(t, x_player, o_player)