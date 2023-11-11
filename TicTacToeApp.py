import pygame
import sys


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


# Pygame initialization
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 300
VIOLET = (148, 87, 235)
DARK_GREEN = (0, 110, 0)
LINE_WIDTH = 15
CELL_SIZE = WIDTH // 3

# Create TicTacToe object
game = TicTacToe()

# Pygame window setup
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")


def draw_board():
    for i in range(1, 3):
        pygame.draw.line(window, DARK_GREEN, (CELL_SIZE * i, 0), (CELL_SIZE * i, HEIGHT), LINE_WIDTH)
        pygame.draw.line(window, DARK_GREEN, (0, CELL_SIZE * i), (WIDTH, CELL_SIZE * i), LINE_WIDTH)


def draw_symbols():
    font = pygame.font.Font(None, 100)

    for i in range(3):
        for j in range(3):
            symbol = game.board[i][j]
            if symbol != ' ':
                text = font.render(symbol, True, DARK_GREEN)
                text_rect = text.get_rect(center=(CELL_SIZE * j + CELL_SIZE // 2, CELL_SIZE * i + CELL_SIZE // 2))
                window.blit(text, text_rect)


# Main game loop
while not game.is_winner() and not game.game_over():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos()
            clicked_row = mouseY // CELL_SIZE
            clicked_col = mouseX // CELL_SIZE

            if game.make_move(clicked_row, clicked_col):
                game.switch_player()

    window.fill(VIOLET)
    draw_board()
    draw_symbols()
    pygame.display.flip()

# Display the final state of the board
game.print_board()

# Display the result of the game
if game.is_winner():
    print(f"Player {game.current_player} wins!")
else:
    print("It's a draw!")

pygame.quit()
