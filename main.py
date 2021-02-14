### Rock Paper Scissors ###
import random


def play():
    user = input('What\'s your choice? "r" for rock, "p" for paper, "s" for scissors? \n')
    computer = random.choice(["r", "p", "s"])
    if user == computer:
        return print('It\'s a tie!')
    if winner(user, computer):
        return print('You won!')
    return print('You lost!')


# p for player, c for computer
def winner(p, c):
    if (p == 'r' and c == 's') or (p == 's' and c == 'p') or (p == 'p' and c == 'r'):
        return True


play()
