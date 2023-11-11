class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def is_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True

        return False

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def make_move(self, row, col):
        # Make a move by updating the board with the current player's symbol
        if 0 <= row < 3 and 0 <= col < 3:
            if self.board[row][col] == ' ':
                self.board[row][col] = self.current_player
                return True
            else:
                print("This cell is already occupied. Please try again.")
                return False
        else:
            print("Incorrect coordinates. Please try again.")
            return False

    def game_over(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True


if __name__ == "__main__":
    game = TicTacToe()

    while not game.is_winner() and not game.game_over():
        game.print_board()
        row = int(input("Enter the row number (0, 1, 2): "))
        col = int(input("Enter the column number (0, 1, 2): "))

        if game.make_move(row, col):
            game.switch_player()

    game.print_board()

    if game.is_winner():
        print(f"Player {game.current_player} wins!")
    else:
        print("It's a draw!")
