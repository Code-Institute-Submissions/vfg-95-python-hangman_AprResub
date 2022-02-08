from slides import tornado_display
from words import easy_words, hard_words
import os, random

def run_game():
  word = random.choice(easy_words).upper()
  hidden_word = "_" * len(word)
  remaining_guesses = 5
  guessed_letters = []

  print(tornado_display(remaining_guesses))
  print(hidden_word)
  print(f"\nAlready guessed: {guessed_letters}")
  print(f"\nRemaining guesses: {remaining_guesses}")

  while remaining_guesses > 0:
    guess = input("\nEnter your guess - letter or word: ").upper()
    if len(guess) == 1:
      if guess not in word:
        remaining_guesses -= 1
        guessed_letters.append(guess)
      else:
        word_ltrs = list(hidden_word)
        indices = [i for i, ltr in enumerate(word) if ltr == guess]
        for index in indices:
          word_ltrs[index] = guess
        hidden_word = "".join(word_ltrs)
      os.system("clear")
      print(tornado_display(remaining_guesses))
      print(hidden_word)
      print(f"\nAlready guessed: {guessed_letters}")
      print(f"\nRemaining guesses: {remaining_guesses}")

run_game()


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

  print('Welcome to Tornado, do you think you have what it takes to save the household?')
  print("\nThe rules are very simple:",
    "\n- A word is chosen and you must guess the word by inputting letters",
    "\n- If you guess correct, the letter will appear and you can make a new guess",
    "\n- If your guess is incorrect you will lose a life",
    "\n- You have 5 lives. At 0 the tornado will wipe out the household and it's game over")
  play = input("Press p to play: ")
  if play == 'p':
    os.system("clear") 
    run_game()


#main()