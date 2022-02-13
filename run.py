from slides import tornado_display
from words import easy_words, hard_words
import random
import os
import time


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
        self.feedback = 0
        self.won = False


def run_game(words):

    cur_game = Tornado(words)

    main_display(cur_game)
    print(cur_game.cur_word)

    while cur_game.remaining_guesses > 0:
        guess = input("\nEnter your guess - letter or word: ").upper()
        if len(guess) == 1:
            check_letter(cur_game, guess)
        elif len(guess) > 1:
            check_word(cur_game, guess)
        time.sleep(2)
        clear_screen(cur_game)
        main_display(cur_game)


def check_letter(cur_game, guess):
    if guess in cur_game.guessed_letters and guess.isalpha():
        cur_game.feedback = 1
        clear_screen(cur_game)
        user_feedback(cur_game, guess)
    elif guess not in cur_game.cur_word and guess.isalpha():
        cur_game.feedback = 2
        cur_game.remaining_guesses -= 1
        cur_game.guessed_letters.append(guess)
        user_feedback(cur_game, guess)
    elif guess in cur_game.cur_word:
        cur_game.feedback = 3
        cur_game.guessed_letters.append(guess)
        word_ltrs = list(cur_game.hidden_word)
        indices = [i for i, ltr in enumerate(cur_game.cur_word) if ltr == guess]
        for index in indices:
            word_ltrs[index] = guess
        cur_game.hidden_word = "".join(word_ltrs)
        user_feedback(cur_game, guess)
    else:
        user_feedback(cur_game, guess)


def check_word(cur_game, guess):
    if guess == cur_game.cur_word:
        win_game(cur_game, guess)
    else:
        cur_game.remaining_guesses -= 1
        update_display(cur_game)


def user_feedback(cur_game, guess):
    if cur_game.feedback == 1:
        update_display(cur_game)
        print(f"\nYou already guessed {guess}!")
    elif cur_game.feedback == 2:
        update_display(cur_game)
        print(f"\n{guess} is not in the word!")
    elif cur_game.feedback == 3:
        update_display(cur_game)
        print(f"\nWell done! {guess} is in the word!")
    else:
        update_display(cur_game)
        print(f"\nYour guess needs to be either a word or letter. Try again..")


def main_display(cur_game):
    update_display(cur_game)
    print(f"\nAlready guessed: {','.join(cur_game.guessed_letters)}")
    print(f"\nRemaining guesses: {cur_game.remaining_guesses}")


def update_display(cur_game):
    print(tornado_display(cur_game.remaining_guesses))
    print(cur_game.hidden_word)


def clear_screen(cur_game):
    os.system("clear")


def win_game(cur_game, guess): 
    print('YOU WON!')


def play_again(cur_game):
    print("Test")

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

    while True:

        difficulty = input(
            "\nChoose your difficulty - enter 'Easy' or 'Hard': ").upper()
        if difficulty == 'EASY':
            os.system("clear")
            run_game(easy_words)
        elif difficulty == 'HARD':
            os.system("clear")
            run_game(hard_words)
        else:
            print("\nInvalid response - Please try again:") 


main()
