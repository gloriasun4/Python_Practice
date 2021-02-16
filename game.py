class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_Winner = None

    def print_board(self):