# Mastermind Game

Mastermind is a game where one player chooses a secret code, and the other player tries to guess it.

## Overview

- Player 1 inputs a secret code.
- Player 2 tries to guess the secret code.
- Player 2 receives feedback on how many numbers they got right and how many are in the correct location.
- The game ends either when Player 2 guesses the correct code or after 10 incorrect guesses.

## Features

- The secret code entered by Player 1 is not displayed on the screen, ensuring privacy.
- Provides feedback on the number of correct numbers and correct locations.
- Provides feedback on when Player 2's guess length does not match Player 1's secret length.

## How to Run

1. Ensure you have Python installed on your machine.
2. Save the provided code in a file named `mastermind.py`.
3. Navigate to the directory containing the file via the command line or terminal.
4. Run the script by entering `python mastermind.py`.
5. Follow the on-screen instructions to play.

## Game Rules

1. Player 1 will be prompted to enter a secret code. This will not be visible on the screen to keep it a secret.
2. Player 2 will have 10 attempts to guess the secret code.
3. After each guess, Player 2 will be provided feedback on:
   - The number of correct numbers.
   - The number of numbers in the correct location.
   - The game ends when either Player 2 guesses the code correctly or uses up all 10 attempts.
