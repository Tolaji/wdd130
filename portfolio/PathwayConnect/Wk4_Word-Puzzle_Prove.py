"""The `import random` statement at the beginning of the code imports the `random` module in Python, which provides ability to select at random, words listed under the  'word_list' variable, this function can also be extended to randomly select words or phrases from a text file located on the same drive as this file.  

The code then prints a welcome message and then proceeds with a loop that allows the player to guess the secret word. The loop continues until the `check_win()` function returns `True`, which means that the player has correctly guessed the secret word at which the player is congratulated.

Within the loop, the player is prompted to enter a guess, which can be a single letter or the full word. The player's guess is then checked to see if it matches the secret word. If the guess is incorrect, the player is given a hint and the loop continues.

The loop also keeps track of the number of guesses the player has made and which letters have already been guessed. The `guessed_letters` variable is set that it keeps track of the letters the player has guessed so far.

Once the loop ends, the player is congratulated and the number of tries taken to guess the correct word is displayed.
"""


# The use of a set of words from a list of secret words
# Guess a full word or a single letter
# Represents the hints as '-' and as a number of letter in the word
# Error handling in case wrong characters are imputed
# Included line breaks for aesthetics


# Import the random function
import random

# Welcome the player
print("\n~~~ WORDS PUZZLE ~~~")
print("~~~ Prove ~~~\n")
print("Welcome to the Words guessing game! Can you guess the secret word?")
print("*" * 65)

# Set the list of secret words
word_list = [
    "joshua",
    "python",
    "programming",
    "computer",
    "algorithm",
    "database",
    "statistics",
    "analysis",
    "application",
    "network",
    "security",
    "web",
    "development",
    "machine",
    "learning",
    "interface",
    "scripting",
    "cloud",
    "virtual",
    "reality",
]

# Set the secret word
secret_word = random.choice(word_list)

# Set up variables for the game
guess_count = 0
guessed_letters = set()
hidden_word = ["_" for letter in secret_word]


def check_win():
    return "".join(hidden_word) == secret_word


# Loop until the player guesses the secret word
while not check_win():
    # Ask the player for a guess
    guess = input("Enter a letter or the full word: ").lower().strip()

    if not guess:
        print("Invalid guess, try again!")
        print("-" * 65)
        continue

    # Count the number of attempts at guessing wrongly
    guess_count += 1
    print(f"Your guess count is {guess_count}")

    # If the guess is a full word, set up the hidden_word list and check if it is correct
    if len(guess) > 1:
        if guess == secret_word:
            hidden_word = [letter.upper() for letter in secret_word]
            print("Congratulations! You guessed the secret word!")
            print(" ".join(hidden_word))
            print("-" * 65)
            break
        else:
            for i, letter in enumerate(secret_word):
                if letter in guess and i < len(guess):
                    hidden_word[i] = (
                        letter.upper() if letter == guess[i] else letter.lower()
                    )

            print("Your guess was not correct. Please try again.")
            print(" ".join(hidden_word))
            print("-" * 65)
            continue

    # Checks if guessed letter is a single letter and in lowercase
    elif len(guess) == 1 and guess.isalpha():
        # Check if the guess has already been made
        if guess in guessed_letters:
            print("You already guessed that letter, try again!")
            print("-" * 65)
            continue

        # Check if the guess is in the secret word
        if guess in secret_word:
            print("Great! You guessed a correct letter!")
            guessed_letters.add(guess)
            print("-" * 65)

            for i, letter in enumerate(secret_word):
                if letter == guess:
                    hidden_word[i] = letter.upper()

            print(" ".join(hidden_word))
            print("-" * 65)

            # Check if the player has guessed all the letters in the secret word
            if "_" not in hidden_word:
                print("Congratulations! You guessed it!")
                print("-" * 65)
                break

        # Informs player the guess isn't in the secret word, increases the guess count, and provides a hint
        else:
            print("Your guess was not correct. Please try again.")

            print("-" * 65)
            print()

            guess_count += 1

            # Provides a hint on the secret word
            hints = []
            for i, letter in enumerate(secret_word):
                if letter in guessed_letters:
                    hints.append(letter.lower())
                else:
                    hints.append("_")

            # If a letter is in the right position, add it to the hidden word in upper case
            # If a letter is in the wrong position, add it to the hints but not to the hidden word
            for i, letter in enumerate(secret_word):
                if letter == guess:
                    if i == guess.index(letter):
                        hidden_word[i] = letter.upper()
                    else:
                        hints[i] = letter

            print("Your hint is:", " ".join(hints))
            print(f"The secret word is {len(secret_word)} characters")
            print(
                "Sorry, the guessed word must have the same number of letters as the secret word."
            )
            print("-" * 83)

    else:
        print("Invalid guess, try again!")
        print("-" * 65)

# Congratulates the player for guessing the correct word and informs the number of tries taken
print(f"Congratulations! You guessed the secret word in {guess_count} tries.")
