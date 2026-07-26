# Hangman (Text-Based)

A simple text-based Hangman game written in Python. The program picks a random word, and the player tries to guess it letter by letter before running out of attempts.

## How to Play

1. Run the script.
2. A random word is chosen from a predefined list.
3. Guess one letter at a time.
4. Correct letters are revealed in their position(s) in the word.
5. Incorrect letters cost you one of your 6 attempts.
6. Guess the full word before you run out of attempts to win!

## Requirements

- Python 3

## Running the Game

```bash
python hangman.py
```

## Example

```
You have 6 attempts left.
Guess a letter: p
_ _ _ _ _ _
You have 6 attempts left.
Guess a letter: o
```

## Project Structure

- `hangman.py` — the full game logic in a single file.

## Concepts Used

- Lists and string manipulation
- The `random` module (`random.choice()`)
- `while` and `for` loops
- Conditional statements
- `input()` / `print()` and f-strings
- Booleans for tracking game state

## Possible Improvements

- Refactor the code into functions for better readability
- Add an ASCII drawing of the hangman that updates with each wrong guess
- Let the player choose difficulty (number of attempts, word length, etc.)
- Add support for accented characters# codealpha_task2
