import random
import time

MAX_LEVEL = 100
WORD_FILE = "words.txt"
CATEGORIES = ["Animals", "Fruits", "Countries", "Movies"]
CATEGORY_WORDS = {
    "Animals": ["dog", "cat", "lion", "tiger", "elephant"],
    "Fruits": ["apple", "banana", "orange", "mango", "pear"],
    "Countries": ["USA", "China", "Japan", "India", "England"],
    "Movies": ["Titanic", "Star Wars", "Harry Potter", "Jurassic Park", "Avengers"],
}
TIME_LIMIT = 30
POWER_UPS = ["Reveal Letter", "Extra Guess", "Remove Letter"]
SCORES = {"Easy": 10, "Medium": 50, "Hard": 100}

# Read words from file
with open(WORD_FILE, "r") as file:
    WORD_LIST = file.readlines()

# Ask the user how many levels they want to play and which category they want
print("Welcome to the word guessing game!")
num_levels = int(
    input(
        "How many levels do you want to play? Enter a number between 1 and {}: ".format(
            MAX_LEVEL
        )
    )
)
num_levels = min(num_levels, MAX_LEVEL)

print("Select a category:")
for i, category in enumerate(CATEGORIES):
    print("{}. {}".format(i + 1, category))
selected_category = int(input("Enter a number: "))
selected_category = max(1, min(selected_category, len(CATEGORIES)))
category_words = CATEGORY_WORDS[CATEGORIES[selected_category - 1]]

# Initialize game variables
current_level = 1
hidden_letters = []
guessed_letters = set()
word = ""
power_ups = []

# Start game loop
while current_level <= num_levels:
    # Generate new word for current level
    num_words = int(10 * (1 - current_level / MAX_LEVEL)) + 1
    if len(category_words) < num_words:
        num_words = len(category_words)
    word_subset = random.sample(category_words, num_words)
    word = random.choice(word_subset).strip()
    hidden_letters = ["_" for letter in word]
    guessed_letters = set()
    power_ups = random.choices(POWER_UPS, k=3)
    print("Level {}: Guess the word!".format(current_level))
    print(" ".join(hidden_letters))

    # Keep asking for guesses until the word is guessed or the user runs out of guesses
    guesses_left = len(word) + 3
    start_time = time.time()
    while guesses_left > 0 and time.time() - start_time <= TIME_LIMIT:
        print(
            "Guesses left: {}, Time left: {} seconds".format(
                guesses_left, TIME_LIMIT - int(time.time() - start_time)
            )
        )
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif len(guess) != 1:
            print("Please enter a single letter.")
        else:
            guessed_letters.add(guess)
            if guess in word:
                print("Correct!")
                for i in range(len(word)):
                    if word[i] == guess:
                        hidden_letters[i] = guess.upper()
                print(" ".join(hidden_letters))
                if "_" not in hidden_letters:
                    score = SCORES[input("Enter difficulty (Easy, Medium, Hard): ")]
                    print(
                        "Congratulations! You guessed the word and scored {} points.".format(
                            score
                        )
                    )
                    current_level += 1
                    break
            else:
                guesses_left -= 1
                print("Wrong. {} guesses left.".format(guesses_left))

            if power_ups:
                print("Power Ups: {}".format(", ".join(power_ups)))
                use_power_up = input("Use a power up? (Y/N) ").lower()
                if use_power_up == "y":
                    power_ups
                    selected_power_up = input(
                        "Select a power up ({}) or enter 'skip': ".format(
                            ", ".join(power_ups)
                        )
                    ).title()
                    if selected_power_up != "Skip" and selected_power_up in power_ups:
                        if selected_power_up == "Reveal Letter":
                            hidden_idx = [
                                i for i in range(len(word)) if hidden_letters[i] == "_"
                            ]
                            reveal_idx = random.choice(hidden_idx)
                            hidden_letters[reveal_idx] = word[reveal_idx].upper()
                            print(
                                "Letter revealed! {}".format(" ".join(hidden_letters))
                            )
                        elif selected_power_up == "Extra Guess":
                            guesses_left += 1
                            print(
                                "Extra guess added. {} guesses left.".format(
                                    guesses_left
                                )
                            )
                        elif selected_power_up == "Remove Letter":
                            all_idx = [i for i in range(len(word))]
                            remaining_idx = list(
                                set(all_idx)
                                - set(
                                    [
                                        j
                                        for j, letter in enumerate(hidden_letters)
                                        if letter != "_"
                                    ]
                                )
                            )
                            remove_idx = random.choice(remaining_idx)
                            hidden_letters[remove_idx] = " "
                            print("Letter removed! {}".format(" ".join(hidden_letters)))
                        power_ups.remove(selected_power_up)
            else:
                print("Time's up! The word was {}.".format(word.upper()))
                current_level += 1

# End of game
print("Game over! Thanks for playing.")
