### Guess the Number ###
import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0;
    while guess != random_number:
        guess = int(input(f'Guess the number I\'m thinking of from 1 and {x}: '))
        print(guess)
        if guess < random_number:
            print("Too low, guess again!")
        elif guess > random_number:
            print("Too high, guess again!")
    print(f"Congrats! The number was {random_number}")

def computer_guess(x):
    low = 1
    high = x
    value = ''
    while value != 'c':
        if low == high:
            guess = low
        else:
            guess = random.randint(low,high)
        value = input(f'I guessed {guess}! Is it too high(H), too low(L), or correct(C)?: ').lower()
        if value == 'h':
            high = guess - 1
        elif value == 'l':
            low = guess + 1
    print(f"Hooray! I guessed the number {guess} correctly!")

computer_guess(1000)