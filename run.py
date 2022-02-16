import random
import os
import time
import sys
from slides import tornado_display
from words import easy_words, hard_words


class Tornado:
    """
    Class used to store the information required to play the game
    with the use of instance variables
    """
    def __init__(self, words):
        self.cur_word = random.choice(words).upper()
        self.reveal_word = "_" * len(self.cur_word)
        self.rem_guess = 5
        self.guessed_letters = []
        self.feedback = 0
        self.won = False


def run_game(words):
    """
    Starts the game with the default display and with the chosen word
    difficulty, and runs the while loop which keeps the game running
    until the user has won or lost
    """
    cur_game = Tornado(words)
    main_display(cur_game)

    while cur_game.rem_guess > 0 or cur_game.won is False:
        guess = t_input("\nEnter your guess - letter or word: ").upper()
        validate(cur_game, guess)
        if cur_game.won is True or cur_game.rem_guess == 0:
            win_game(cur_game, guess)
            break
        time.sleep(1.5)
        clear_screen()
        main_display(cur_game)


def validate(cur_game, guess):
    """
    Validates the users input and then calls the correct function
    for a single letter or word guess
    """
    if guess.isalpha():
        if len(guess) == 1:
            check_letter(cur_game, guess)
        else:
            check_word(cur_game, guess)
    else:
        update_display(cur_game)
        t_print("\nYour guess needs to be a word or letter. Try again..")


def check_letter(cur_game, guess):
    """
    Checks the users guess of an individual letter then updates the reveal
    word variable and gives relevant feedback
    """
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
    else:
        cur_game.feedback = 2
        cur_game.rem_guess -= 1
        cur_game.guessed_letters.append(guess)
        user_feedback(cur_game, guess)


def check_word(cur_game, guess):
    """
    Checks users guess of a full word and then either ends the game if
    correct or continues the game with relevant feedback - also allows
    the user to quit game
    """
    if guess == 'QUIT':
        quit_game()
    elif guess == cur_game.cur_word:
        cur_game.won = True
    else:
        cur_game.feedback = 4
        cur_game.rem_guess -= 1
        user_feedback(cur_game, guess)


def update_reveal_word(cur_game, guess):
    """
    Checks the users individual letter guesses against the current word
    and then joins them to the reveal word if they are correct
    This code is credited in the README
    """
    word_ltrs = list(cur_game.reveal_word)
    indices = [i for i, ltr in enumerate(cur_game.cur_word) if ltr == guess]
    for index in indices:
        word_ltrs[index] = guess
    cur_game.reveal_word = "".join(word_ltrs)


def user_feedback(cur_game, guess):
    """
    Chooses the relevant feedback to be displayed to the user after
    their most recent guess
    """
    if cur_game.feedback == 1:
        update_display(cur_game)
        t_print(f"\nYou already guessed {guess}!")
    elif cur_game.feedback == 2:
        update_display(cur_game)
        t_print(f"\n{guess} is not in the word!")
    elif cur_game.feedback == 3:
        update_display(cur_game)
        t_print(f"\nWell done! {guess} is in the word!")
    elif cur_game.feedback == 4:
        update_display(cur_game)
        t_print(f"\n {guess} is not the word!")
    else:
        update_display(cur_game)


def main_display(cur_game):
    """
    Displays the current state of the game with necessary information
    for the user to continue playing
    """
    update_display(cur_game)
    print(f"\nAlready guessed: {','.join(cur_game.guessed_letters)}")
    print(f"\nRemaining guesses: {cur_game.rem_guess}")


def update_display(cur_game):
    """
    Prints the tornado image and the current state of the reveal word
    """
    print(tornado_display(cur_game.rem_guess))
    print(cur_game.reveal_word)


def clear_screen():
    """
    Clears the terminal to allow for the updated display of the game
    """
    os.system("clear")


def win_game(cur_game, guess):
    """
    Checks whether the user has won the game or not and displays relevant
    feedback, then asks if they want to play again
    """
    if cur_game.won is True:
        clear_screen()
        print(tornado_display(cur_game.rem_guess))
        print(f"{cur_game.cur_word} is correct!")
        print(f"Well done, You saved the household!")
    else:
        clear_screen()
        print(tornado_display(cur_game.rem_guess))
        print("The house is destroyed! You lose.")
        print(f"\n The word was {cur_game.cur_word}")

    play_again()


def play_again():
    """
    Enables the user to choose if they want to play another game
    """
    again = t_input(
            "\n Would you like to play again? - enter 'N' or 'Y': ").upper()
    if again == 'N':
        quit_game()
    elif again == 'Y':
        os.system("clear")
        logo()
        choose_difficulty()
    elif again == 'QUIT':
        quit_game()
    else:
        t_print("\n Invalid response - Please try again: \n")


def choose_difficulty():
    """
    Enables the user to chose the difficulty of the game
    """
    difficulty = t_input(
        "Choose your difficulty - enter 'Easy' or 'Hard': ").upper()
    if difficulty == 'EASY':
        os.system("clear")
        run_game(easy_words)
    elif difficulty == 'HARD':
        os.system("clear")
        run_game(hard_words)
    elif difficulty == 'QUIT':
        quit_game()
    else:
        t_print("\n Invalid response - Please try again: \n")


def quit_game():
    """
    Enables the user to end the game at any point they wish and displays
    leaving message and logo
    """
    clear_screen()
    logo()
    t_print("\n Thanks for playing - until next time!")
    time.sleep(1)
    quit()


def logo():
    """
    Displays the main logo for the game
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


def t_print(text):
    """
    This allows print text to be displayed with typing effect
    This code is credited in the README
    """
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.035)


def t_input(text):
    """
    This allows input text to be displayed with typing effect
    This code is credited in the README
    """
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.035)
    value = input()
    return value


def main():
    """
    Displays the landing page to the user and explains the rules of the
    game, and then lets them choose their difficulty or to quit the game
    """
    logo()

    t_print(""" Welcome to Tornado,
 do you think you have what it takes to save the household?""")
    time.sleep(0.3)
    print("\n")
    t_print(" The rules are very simple: \n")
    time.sleep(0.3)
    t_print(
        "\n- A word is chosen & you must guess the word by inputting letters")
    time.sleep(0.3)
    t_print(
        "\n- If correct, the letter will appear & you can make a new guess")
    time.sleep(0.3)
    t_print("\n- If your guess is incorrect you will lose a life")
    time.sleep(0.3)
    t_print("\n- You have 5 lives")
    time.sleep(0.3)
    t_print("\n- At 0 lives the tornado will destroy the household & you lose")
    time.sleep(0.3)
    t_print("\n- If you wish to quit at any point, enter 'Quit'")
    time.sleep(0.3)
    print("\n")

    choose_difficulty()


main()
