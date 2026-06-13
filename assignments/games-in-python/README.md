
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a command-line Hangman game that reinforces string manipulation, loops, and conditional logic by having students implement game flow and state tracking.

## 📝 Tasks

### 🛠️ Hangman Game

#### Description
Create a playable Hangman game where the program selects a secret word and the player guesses letters until they either reveal the word or run out of allowed incorrect attempts.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list.
- Display the current word progress using underscores for unknown letters (e.g. `_ _ _ _`).
- Accept single-letter guesses and update the displayed progress.
- Track and display the number of remaining incorrect attempts.
- Avoid deducting attempts for letters that have already been guessed.
- End the game with a win message when the word is fully revealed, or a loss message that reveals the correct word when attempts run out.

#### Example gameplay
```
Secret word: "code"
Display: _ _ _ _
Player guesses: c
Display: c _ _ _
Player guesses: o
Display: c o _ _
```

Follow the project assignment template and keep the README sections intact.
