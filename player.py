import math
import random


# constructor in Python

class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        # try, except format good for looping until valid value is passed
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8):')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again!')
        return val

    def genius_computer_player(player):
        def __init__(self, letter):
            super().__init__(letter)

        def get_move(self, game):
            if len(game.available_moves()) == 9:
                square = random.choice(game.available_moves())
            else:
                square = self.minimax(game, self.letter)
            return square

        def minimax(self, state, player):
            max_player = self.letter
            other_player = 'O' if player == 'X' else 'X'

            if state.current_winner == other_player:
                player_num = 1 if other_player == max_player else -1
                return {'position': None, 'score': player_num * (state.num_empty_square() + 1)}

            elif not state.empty_squares():
                return {'position': None, 'score': 0}


