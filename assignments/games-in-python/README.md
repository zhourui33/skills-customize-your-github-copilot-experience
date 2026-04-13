# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic word-guessing game using Python strings, loops, and user input. Students will practice string manipulation, conditionals, loops, and random selection.

## 📝 Tasks

### 🛠️	Set Up the Game

#### Description
Create the initial game setup by defining a list of words and randomly selecting one for the player to guess. Display the word as underscores and set the number of allowed incorrect attempts.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list
- Display the hidden word in `_ _ _` format
- Set and display the number of allowed incorrect guesses

### 🛠️	Implement the Guessing Logic

#### Description
Accept letter guesses from the player and update the game state accordingly. Reveal correctly guessed letters in the word and track incorrect guesses.

#### Requirements
Completed program should:

- Accept single-letter guesses from user input
- Reveal correctly guessed letters in their positions
- Track and display the number of incorrect guesses remaining
- Prevent duplicate guesses from being counted

### 🛠️	Handle Win and Lose Conditions

#### Description
End the game when the player has guessed the full word or has exhausted all attempts. Display an appropriate win or lose message.

#### Requirements
Completed program should:

- End the game when the word is fully guessed and display a win message
- End the game when attempts are exhausted and display a lose message with the correct word
- Prompt the player to play again
