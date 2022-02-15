# Tornado Game

## Overview

As the game is played in the terminal/CLI I decided the target audience would be technology/computer enthusiasts 
(as they will have to have at least some knowledge of this to play the game in the first place) who enjoy guessing games, and computer games in general. I then came up with an alternative theme/imagery to give the game extra interest.

## Goals

### Organisation Aims

-   Create a variation on the traditional hangman game using a different theme & imagery
-   Make the the game easy to play and rules unambigious
-   Allow the user to chose the difficulty of the words used in the game


### User Stories

- I want the game to be intuative to understand and play
- I want to be able to continue playing or finish the game when I choose
- I want the game to be visually appealing
- I want to know the word after losing
- I want to be able to choose the difficulty of the game

## Game Development

My overall plan for the game was to create a hangman type game with it's own style. Due to the nature of it being played in the terminal this made me think about using a retro, arcade type of aesthetic for the game. I searched for ASCII art and came up with the idea of using a tornado approaching a house, getting closer everytime the user guesses incorrectly. Implementing all this would enable the game to meet all user stories.

### Game Planning

Due to the nature of the game being command line the first step in the planning phase wasn't to wireframe but rather to create a flow chart that would enable me to implement the logic for the game into my python code and take it from there:

![flowchart](./assets/images/flowchart.png)

## Functionality

The 'home' page for the game features a retro computer style font displaying the name of the game, then the rules for the game are displayed which make use of a typing effect so that they appear to be typed out to the user (adding to the retro game aesthetic). These are followed by the question asking the user which difficulty they would like to play. These 3 features meet all 3 of the organisation aims and the 1st, 2nd, 3rd & 5th user stories.

![tornadohome](./assets/images/tornado_home.png)

Once the game starts the user sees the main display for the game which is the tornado at it's furthest point from the house, the empty reveal word, the amount of remaining guesses which is then followed by the input which makes use of the typing effect to prompt the user to guess a letter or word. This meets the 1st and 3rd user stories.

![gameplay](./assets/images/gameplay.png)

The game will then display relevant feedback to the user depending on their guess, as follows:

Correct letter:

![correctletter](./assets/images/correctletter.png)

Incorrect letter:

![incorrectletter](./assets/images/incorrectletter.png)

Invalid input:

![invalidinput](./assets/images/invalidinput.png)

Incorrect word:

![incorrectword](./assets/images/incorrectword.png)

These features meet the first user story.

The game will then result in either win or lose game, at which point the user is informed what the correct word was if
they lost which is followed by asking if the user wants to play again - if they choose yes they are taken to the choose difficulty page and if they choose no they are displayed the quit game page. This meets the 2nd, 3rd, 4th & 5th user stories.

Win game:

![wingame](./assets/images/wingame.png)

Lose game:

![losegame](./assets/images/losegame.png)

Play again:

![playagain](./assets/images/playagain.png)

Quit game:

![quitgame](./assets/images/quitgame.png)

## Testing

As the game runs in the terminal (or via the Heroku app) there was no need to test on multiple devices/browsers
as it will run the same on all of them. Testing was done on my MacBook Air and the process references all the features mentioned in the previous functionality section. The process was as follows:

- Test that the 'home page' displays the logo and rules and difficulty input (with typing effects) properly
- Test that the user input for difficulty responds as expected; hard = hard words, easy = easy words, quit = quit game
- Test that the game displays as expected once starting; reveal word is empty, remaining guesses = 5, already guess is empty and the tornado image is at it's intended starting position
- Test that both word and letter input validation works so that anything which isn't alphabetical will give the user invalid input feedback
- Test that correct letter guesses result in correct letter feedback & the letter displaying in reveal word and guessed letters
- Test that incorrect letter guesses result in incorrect letter feedback, remaining guesses decreases by 1, the tornado image moves closer to the house and the letter is added to guessed letters
- Test that correct word guesses result in win game feedback being displayed to the user and that the play again option is displayed
- Test that incorrect word guesses result in incorrect word feedback, remaining guesses decreases by 1 and the tornado image moves closer to the house
- Test that when the user reaches 0 guesses the tornado hits the house and the game ends, the user is told what the correct word was and is asked if they want to play again
- Test that if the user choses to play again they are taken to the play again page and that the chose difficult input works as expected
- Test that if the user choses not to play again they are taken to the thanks for playing page
- Test that the quit game function works at any point in the game and that the user is displayed the thanks for playing page


