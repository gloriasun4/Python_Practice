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

guess(10)
