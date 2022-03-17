import time
from random import *

class TicTacToe:
    def __init__(self):
        self.board = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
        self.player = "X"
        self.game_still_running = True
        self.is_same_position = False
        self.winner = None

    def display_board(self):
        print(self.board[0] + " | " + self.board[1] + " | " + self.board[2] + '                ' + '1 | 2 | 3')
        print(self.board[3] + " | " + self.board[4] + " | " + self.board[5] + '                ' + '4 | 5 | 6')
        print(self.board[6] + " | " + self.board[7] + " | " + self.board[8] + '                ' + '7 | 8 | 9')
        print(f"{self.player}'s turn.")

    def change_player(self):
        if self.player == 'X':
            self.player = "O"
        elif self.player == "O":
            self.player = "X"

    def check_rows(self):
        if self.board[0] != '_':
            if self.board[0] == self.board[1] == self.board[2]:
                self.game_still_running = False
                self.winner = self.board[0]
                print(f"The winner is {self.winner}")

        if self.board[3] != '_':
            if self.board[3] == self.board[4] == self.board[5]:
                self.game_still_running = False
                self.winner = self.board[3]
                print(f"The winner is {self.winner}")

        if self.board[6] != '_':
            if self.board[6] == self.board[7] == self.board[8]:
                self.game_still_running = False
                self.winner = self.board[6]
                print(f"The winner is {self.winner}")

    def check_columns(self):
        if self.board[0] != '_':
            if self.board[0] == self.board[3] == self.board[6]:
                self.game_still_running = False
                self.winner = self.board[0]
                print(f"The winner is {self.winner}")

        if self.board[1] != '_':
            if self.board[1] == self.board[4] == self.board[7]:
                self.game_still_running = False
                self.winner = self.board[1]
                print(f"The winner is {self.winner}")

        if self.board[2] != '_':
            if self.board[2] == self.board[5] == self.board[8]:
                self.game_still_running = False
                self.winner = self.board[2]
                print(f"The winner is {self.winner}")

    def check_diagonals(self):
        if self.board[0] != '_':
            if self.board[0] == self.board[4] == self.board[8]:
                self.game_still_running = False
                self.winner = self.board[0]
                print(f"The winner is {self.winner}")

        if self.board[2] != '_':
            if self.board[2] == self.board[4] == self.board[6]:
                self.game_still_running = False
                self.winner = self.board[2]
                print(f"The winner is {self.winner}")

    def draw(self):
        if '_' not in self.board:
            self.game_still_running = False
            print('Draw')

    def check_winner(self):
        self.check_rows()
        self.check_columns()
        self.check_diagonals()

    def check_ai_winner(self, bo, le):
        return ((bo[6] == le and bo[7] == le and bo[8] == le) or  # across the top
                (bo[3] == le and bo[4] == le and bo[5] == le) or  # across the middle
                (bo[0] == le and bo[1] == le and bo[2] == le) or  # across the bottom
                (bo[6] == le and bo[3] == le and bo[0] == le) or  # down the left side
                (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the middle
                (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the right side
                (bo[6] == le and bo[4] == le and bo[2] == le) or  # diagonal
                (bo[8] == le and bo[4] == le and bo[0] == le))  # diagonal

    def computer_move(self):
        possible_moves = [x for x, let in enumerate(self.board) if let == '_']
        position = 0
        for i in ['O', 'X']:
            for x in possible_moves:
                boardcopy = self.board[:]
                boardcopy[x] = i
                if self.check_ai_winner(boardcopy, i):
                    position = i
                    return position
        return position

    def start(self):
        while not self.is_same_position:
            while self.game_still_running:
                self.display_board()
                if self.player == 'O':
                    time.sleep(1)
                    position = self.computer_move()
                    while self.board[position] == '_':
                        position = self.computer_move()
                        position = position + 1
                        position = str(position)
                else:
                    position = input('choose position from 1 - 9: ')
                number = []
                for i in range(1, 10):
                    number.append(str(i))
                while position not in number:
                    position = input("choose a position from 1 to 9: ")

                position = int(position)
                position = position - 1
                if self.board[position] == '_':
                    self.board[position] = self.player
                    self.change_player()
                    self.is_same_position = True
                self.check_winner()
                self.draw()


if __name__ == "__main__":
    game = TicTacToe()
    game.start()
