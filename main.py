### Hangman ###
import random
from words import words
import string


def get_valid_word(words):
    computer_word = random.choice(words)
    while '-' in computer_word or ' ' in computer_word:
        computer_word = random.choice(words)
    return computer_word.upper()

def play():
    word = get_valid_word(words)
    # creates a set of letters in word
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6

    while len(word_letters) > 0 and lives > 0:

        print("You have", lives, "lives left.\nYou have already used these letters: ", " ".join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_input = input('Guess a letter: ').upper()
        if user_input in alphabet - used_letters:
            used_letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)
            else:
                lives-=1
                print("Letter is not in the word")

        elif user_input in used_letters:
            print("You have already used that letter. Please try again!")

        else:
            print("Invalid letter. Please try again!")
    if lives == 0:
        print("Sorry! Game over. The word was ", word)
    else:
        print("Congrats! You won!")

play()




