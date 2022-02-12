from slides import tornado_display
from words import easy_words, hard_words
import random
import os


class Tornado:
    """
    Class used to store the information required to play the game
    by allowing functions to access and use the instance atttibutes
    """
    def __init__(self, words):
        self.cur_words = words
        self.cur_word = random.choice(words).upper()
        self.hidden_word = "_" * len(self.cur_word)
        self.remaining_guesses = 5
        self.guessed_letters = []


def run_game(words):

    cur_game = Tornado(words)

    update_display(cur_game)

    while cur_game.remaining_guesses > 0:
        guess = input("\nEnter your guess - letter or word: ").upper()
        if len(guess) == 1:
            check_letter(cur_game, guess)
            clear_screen(cur_game)
            update_display(cur_game)
        

def check_letter(cur_game, guess):
    if guess not in cur_game.cur_word:
        cur_game.remaining_guesses -= 1
        cur_game.guessed_letters.append(guess)
    else:
        word_ltrs = list(cur_game.hidden_word)
        indices = [i for i, ltr in enumerate(cur_game.cur_word) if ltr == guess]
        for index in indices:
            word_ltrs[index] = guess
        cur_game.hidden_word = "".join(word_ltrs)


def update_display(cur_game):
    print(tornado_display(cur_game.remaining_guesses))
    print(cur_game.hidden_word)
    print(f"\nAlready guessed: {','.join(cur_game.guessed_letters)}")
    print(f"\nRemaining guesses: {cur_game.remaining_guesses}")


def clear_screen(cur_game):
    os.system("clear")


def main():
    print("""
         _______  _______  ______    __    _  _______  ______   _______
        |       ||       ||    _ |  |  |  | ||   _   ||      | |       |
        |_     _||   _   ||   | ||  |   |_| ||  |_|  ||  _    ||   _   |
          |   |  |  | |  ||   |_||_ |       ||       || | |   ||  | |  |
          |   |  |  |_|  ||    __  ||  _    ||       || |_|   ||  |_|  |
          |   |  |       ||   |  | || | |   ||   _   ||       ||       |
          |___|  |_______||___|  |_||_|  |__||__| |__||______| |_______|
        """)

    print(""" Welcome to Tornado,
     do you think you have what it takes to save the household?""")
    print("""\nThe rules are very simple:
    \nA word is chosen and you must guess the word by inputting letters
    \nIf you guess correct, the letter will appear and you can make a new guess
    \nIf your guess is incorrect you will lose a life"
    \nYou have 5 lives. At 0 the tornado will wipe out the household""")
    difficulty = input(
        "Choose your difficulty - enter 'Easy' or 'Hard': ").upper()
    if difficulty == 'EASY':
        os.system("clear")
        run_game(easy_words)
    elif difficulty == 'HARD':
        os.system("clear")
        run_game(hard_words)


main()
