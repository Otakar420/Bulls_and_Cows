# Bulls and Cows

## Running the Game
- Open PowerShell in the game directory.
- Make sure Python is installed — the game has been tested with Python version 3.12.1.
- Then, execute the program using the following command:
```
python '.\bulls_&_cows.py'
```

## Introduction

- Bulls and cows, also known as cows and bulls or pigs and bulls, is a classic code-breaking game, often played with paper and pencil for two or more players.
- This open-source version, 4digits, uses the symbols "Bulls" for the correct digits in the right place and "Cows" for the correct digits in the wrong place.

## Origin

- Bulls and cows predates the commercially sold board game Mastermind, and its word version predates the popular word game Wordle.
- A variant called MOO was widely available for computers running mainframe, Unix, and Multics operating systems.

## Rules

- Plays with four digits, but variations with any number of digits are possible.
- The program generates a secret four-digit number with unique digits, which players then guess.
- In each round, players guess their opponent's number and receive feedback in the form of "bulls" (correct digits in the correct place) and "cows" (correct digits in the wrong place).

_Example:_

```
Secret number: 4271  
Opponent's guess: 1234  
Answer: 1 bulls and 2 cows. (Bulls are "2", cows are "4" and "1".)
```

## Game Complexity

- It has been proven that it is possible to break any number in seven moves.
- The average minimum game length is approximately 5.21 moves.