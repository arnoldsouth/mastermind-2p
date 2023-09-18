import getpass


def get_feedback(secret, guess):
    # Initialize counter for the correct number in the correct location (correct_location).
    correct_location = 0
    # Initialize counter for the correct number regardless of its location (correct_number).
    correct_number = 0

    # Create two lists to keep track of which numbers from the secret and guess have been matched. This ensures we don't double-count numbers if there's duplicates.
    matched_secret = [False] * len(secret)
    matched_guess = [False] * len(guess)

    # For numbers in the correct position:
    # Check each position in the secret against the corresponding position in the guess.
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            # The number in position i of the guess is correct. Increment the count of correct_location.
            correct_location += 1
            # Increment the count of overall correct numbers.
            correct_number += 1
            # Mark these positions as matched.
            matched_secret[i] = True
            matched_guess[i] = True

    # For numbers not in the correct position:
    # Check each number in the secret against each number in the guess.
    for i in range(len(secret)):
        for j in range(len(guess)):
            if (
                not matched_secret[i]
                and not matched_guess[j]
                and secret[i] == guess[j]
            ):
                # The number from the secret exists in the guess but at a different position.
                correct_number += 1
                # Mark these numbers as matched.
                matched_secret[i] = True
                matched_guess[j] = True
                # Once a match is found for this secret[i], break out of loop and move to the next one
                break

    # Return the counts of correct numbers and their correct locations.
    return correct_location, correct_number


def mastermind():
    # Display game name
    print("Mastermind Game")

    # Instructs Player 1 to input secret code (to be guessed by Player 2).
    # print("\nPlayer 1, enter secret code:")
    # Assign variable (secret) to Player 1's input as a list and stripped of whitespaces.
    # secret = list(input().strip())

    # Uses getpass module so Player 1 secret input isn't displayed
    secret = list(getpass.getpass("\nPlayer 1, enter secret code:").strip())
    secret_length = len(secret)
    print("*" * secret_length)
    print(f"Secret code is {secret_length} digit(s).")

    # Initialize counter to keep track of the number of guesses made by Player 2.
    num_guesses = 0
    # Assign variable (MAX_GUESSES) to maximum number of guesses Player 2 can make.
    MAX_GUESSES = 10

    # While number of guesses is less than 10, continue prompting Player 2 for guesses until out of attempts.
    while num_guesses < MAX_GUESSES:
        # Prompts Player 2 to enter guess and provides current guess attempt count.
        print(f"\nPlayer 2, enter guess ({num_guesses + 1}/{MAX_GUESSES}):")

        # Assign variable (guess) to Player 2's guess as a list and stripped of whitespaces.
        guess = list(input().strip())
        # Increment the number of guess attempts once guess is made.
        num_guesses += 1

        # Check if the guess is of the correct length as secret. Attempt is incremented for incorrect guess length.
        if len(guess) != len(secret):
            print(f"Your guess should be {len(secret)} digit(s).")

            # If incorrect guess length was Player 2's last guess (10/10), end the game and reveal the secret.
            if num_guesses == MAX_GUESSES:
                print(
                    f"Game over. Player 2 has used all attempts. The correct code was {(''.join(secret))}."
                )
                return
            # If the guess is not of the correct length, prompt for another guess.
            continue

        # Get returned feedback based on the current guess and assign them variables (correct_loc, correct_num).
        correct_loc, correct_num = get_feedback(secret, guess)

        # For Player 2's correct guess: check feedback's correct_loc count value against secret's length (the correct_loc count matches the length of secret code).
        if correct_loc == len(secret):
            print(
                f"Yay Player 2! You guessed the secret code in {num_guesses} attempt(s)."
            )
            break
        else:
            # If the guess was incorrect, provide feedback.
            print(
                f"{correct_num} correct number(s) and {correct_loc} correct location(s)."
            )

        # If Player 2 has used up all their guesses, end the game and reveal the secret.
        if num_guesses == MAX_GUESSES:
            print(
                f"Game over. Player 2 has used all attempts. The correct code was {(''.join(secret))}."
            )


# Start the game if this script is executed directly.
if __name__ == "__main__":
    mastermind()
