import random
import os
import time
import sys
from slides import tornado_display
from words import easy_words, hard_words


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

    while cur_game.rem_guess > 0 or cur_game.won is False:
        guess = typing_input("\nEnter your guess - letter or word: ").upper()
        if len(guess) == 1:
            check_letter(cur_game, guess)
            if cur_game.won is True or cur_game.rem_guess == 0:
                win_game(cur_game, guess)
                break
            time.sleep(1)
            clear_screen()
            main_display(cur_game)
        elif len(guess) > 1:
            check_word(cur_game, guess)
            if cur_game.won is True or cur_game.rem_guess == 0:
                win_game(cur_game, guess)
                break


def check_letter(cur_game, guess):
    """
    docstring
    """
    if guess.isalpha():
        if guess in cur_game.guessed_letters:
            cur_game.feedback = 1
            clear_screen()
            user_feedback(cur_game, guess)
        elif guess in cur_game.cur_word:
            cur_game.feedback = 3
            cur_game.guessed_letters.append(guess)
            update_reveal_word(cur_game, guess)
            user_feedback(cur_game, guess)
            if cur_game.reveal_word == cur_game.cur_word:
                cur_game.won = True
                win_game(cur_game, guess)
        else:
            cur_game.feedback = 2
            cur_game.rem_guess -= 1
            cur_game.guessed_letters.append(guess)
            user_feedback(cur_game, guess)
    else:
        update_display(cur_game)
        print("\nYour guess needs to be either a word or letter. Try again..")


def check_word(cur_game, guess):
    """
    docstring
    """
    if guess == 'QUIT':
        quit_game()
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


def clear_screen():
    """
    docstring
    """
    os.system("clear")


def win_game(cur_game, guess):
    """
    docstring
    """
    if cur_game.won is True:
        clear_screen()
        print(tornado_display(cur_game.rem_guess))
        print(f"{guess} is correct! Well done, You saved the household!")
    else:
        clear_screen()
        print(tornado_display(cur_game.rem_guess))
        print("The house is destroyed! You lose.")

    play_again()


def play_again():
    again = typing_input(
            "\n Would you like to play again? - enter 'N' or 'Y': ").upper()
    if again == 'N':
        quit_game()
    elif again == 'Y':
        os.system("clear")
        choose_difficulty()
    elif again == 'QUIT':
        quit_game()
    else:
        print("\n Invalid response - Please try again: \n")


def choose_difficulty():
    difficulty = typing_input(
        " Choose your difficulty - enter 'Easy' or 'Hard': ").upper()
    if difficulty == 'EASY':
        os.system("clear")
        run_game(easy_words)
    elif difficulty == 'HARD':
        os.system("clear")
        run_game(hard_words)
    elif difficulty == 'QUIT':
        quit_game()
    else:
        print("\n Invalid response - Please try again: \n")


def quit_game():
    clear_screen()
    logo()
    typing_print("\n Thanks for playing - until next time!")
    time.sleep(1)
    quit()


def logo():
    print("""
         _______  _______  ______    __    _  _______  ______   _______
        |       ||       ||    _ |  |  |  | ||   _   ||      | |       |
        |_     _||   _   ||   | ||  |   |_| ||  |_|  ||  _    ||   _   |
          |   |  |  | |  ||   |_||_ |       ||       || | |   ||  | |  |
          |   |  |  |_|  ||    __  ||  _    ||       || |_|   ||  |_|  |
          |   |  |       ||   |  | || | |   ||   _   ||       ||       |
          |___|  |_______||___|  |_||_|  |__||__| |__||______| |_______|
        """)


def typing_print(text):
    """
    This allows text to be displayed with typing effect
    """
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.035)


def typing_input(text):
    """
    This allows input text to be displayed with typing effect
    """
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.035)
    value = input()
    return value


def main():
    """
    docstring
    """
    logo()

    typing_print(""" Welcome to Tornado,
 do you think you have what it takes to save the household?""")
    time.sleep(0.3)
    print("\n")
    typing_print(" The rules are very simple: \n")
    time.sleep(0.3)
    typing_print("\n- A word is chosen and you must guess the word by inputting letters")
    time.sleep(0.3)
    typing_print("\n- If you guess correct, the letter will appear and you can make a new guess")
    time.sleep(0.3)
    typing_print("\n- If your guess is incorrect you will lose a life")
    time.sleep(0.3)
    typing_print("\n- You have 5 lives. At 0 the tornado will wipe out the household and you lose")
    time.sleep(0.3)
    typing_print("\n- If you wish to quit at any point, enter 'Quit'")
    time.sleep(0.3)
    print("\n")

    choose_difficulty()


main()
