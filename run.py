from slides import tornado_display
from words import easy_words, hard_words
import random
import os
import time
import sys


class Tornado:
    """
    Class used to store the information required to play the game
    by allowing functions to access and use the instance atttibutes
    """
    def __init__(self, words):
        self.cur_words = words
        self.cur_word = random.choice(words).upper()
        self.reveal_word = "_" * len(self.cur_word)
        self.rem_guess = 5
        self.guessed_letters = []
        self.feedback = 0
        self.won = False


def run_game(words):
    """
    docstring
    """
    cur_game = Tornado(words)
    main_display(cur_game)
    print(cur_game.cur_word)  #dont forget to delete

    while cur_game.rem_guess > 0:
        guess = input("\nEnter your guess - letter or word: ").upper()
        if len(guess) == 1:
            check_letter(cur_game, guess)
            time.sleep(2)
            clear_screen(cur_game)
            main_display(cur_game)
        elif len(guess) > 1:
            check_word(cur_game, guess)
    else:
        win_game(cur_game, guess)


def check_letter(cur_game, guess):
    """
    docstring
    """
    if guess in cur_game.guessed_letters and guess.isalpha():
        cur_game.feedback = 1
        clear_screen(cur_game)
        user_feedback(cur_game, guess)
    elif guess not in cur_game.cur_word and guess.isalpha():
        cur_game.feedback = 2
        cur_game.rem_guess -= 1
        cur_game.guessed_letters.append(guess)
        user_feedback(cur_game, guess)
    elif guess in cur_game.cur_word:
        cur_game.feedback = 3
        cur_game.guessed_letters.append(guess)
        update_reveal_word(cur_game, guess)
        user_feedback(cur_game, guess)
    else:
        user_feedback(cur_game, guess)


def check_word(cur_game, guess):
    """
    docstring
    """
    if guess == 'QUIT':
        quit()
    elif guess == cur_game.cur_word:
        cur_game.won = True
        win_game(cur_game, guess)
    else:
        cur_game.feedback = 4
        cur_game.rem_guess -= 1
        user_feedback(cur_game, guess)


def update_reveal_word(cur_game, guess):
    """
    docstring
    """
    word_ltrs = list(cur_game.reveal_word)
    indices = [i for i, ltr in enumerate(cur_game.cur_word) if ltr == guess]
    for index in indices:
        word_ltrs[index] = guess
    cur_game.reveal_word = "".join(word_ltrs)        


def user_feedback(cur_game, guess):
    """
    docstring
    """
    if cur_game.feedback == 1:
        update_display(cur_game)
        print(f"\nYou already guessed {guess}!")
    elif cur_game.feedback == 2:
        update_display(cur_game)
        print(f"\n{guess} is not in the word!")
    elif cur_game.feedback == 3:
        update_display(cur_game)
        print(f"\nWell done! {guess} is in the word!")
    elif cur_game.feedback == 4:
        update_display(cur_game)
        print(f"\n {guess} is not the word!")
    else:
        update_display(cur_game)
        print(f"\nYour guess needs to be either a word or letter. Try again..")


def main_display(cur_game):
    """
    docstring
    """
    update_display(cur_game)
    print(f"\nAlready guessed: {','.join(cur_game.guessed_letters)}")
    print(f"\nRemaining guesses: {cur_game.rem_guess}")


def update_display(cur_game):
    """
    docstring
    """
    print(tornado_display(cur_game.rem_guess))
    print(cur_game.reveal_word)


def clear_screen(cur_game):
    """
    docstring
    """
    os.system("clear")


def win_game(cur_game, guess):
    """
    docstring
    """
    clear_screen(cur_game) 
    print(tornado_display(cur_game.rem_guess))
    print(f"{guess} is correct! Well done, You saved the household!")


def main():
    """
    docstring
    """
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

    while True:

        difficulty = input(
            "\nChoose your difficulty - enter 'Easy' or 'Hard': ").upper()
        if difficulty == 'EASY':
            os.system("clear")
            run_game(easy_words)
        elif difficulty == 'HARD':
            os.system("clear")
            run_game(hard_words)
        elif difficulty == 'QUIT':
            quit()
        else:
            print("\nInvalid response - Please try again:") 


main()
