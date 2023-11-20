import random

"""
print("\n~~~ WK4 Team Activity ~~~")
print("~~~ Guess my number ~~~\n")


magic_number = random.randint(1, 50)
counter = 0
keep_playing = "yes"

# Loop to ask is user wants to keep playing
while keep_playing == "yes":
    user_input = int(
        input("Guess the magic number: ")
    )  # Prompt user to guess the magic word

    while magic_number != user_input:
        counter += 1
        print(f"Your have guessed {counter} times")
        if user_input < magic_number:
            print("Go higher")
            print("_" * 30)  # Print break lines

        elif user_input > magic_number:
            print("Go lower")
            print("_" * 30)  # Print break lines

        else:
            print("You are right")
        user_input = int(input("Guess the magic number: "))
    keep_playing = input("Do you want to play again: ").lower()

# Statement comfirming player choice as 'Yes'
if keep_playing != "yes":
    print("Thank you")
"""
import random
import time


def play_game():
    magic_num = random.randint(1, 100)
    guesses = 0
    start_time = time.time()
    while True:
        try:
            guess = int(input("Guess the magic number between 1 and 100: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        guesses += 1

        if guess == magic_num:
            end_time = time.time()
            time_taken = end_time - start_time
            print(
                "Congratulations! You guessed the magic number in {} guesses and {} seconds.".format(
                    guesses, round(time_taken, 1)
                )
            )
            break
        elif guess > magic_num:
            print("Your guess is too high.")
        else:
            print("Your guess is too low.")

        if guesses == 10:
            print(
                "You have reached the maximum number of guesses. The magic number was {}.".format(
                    magic_num
                )
            )
            break

    if guesses <= 5:
        print("You are a genius!")
    elif guesses <= 10:
        print("You did a great job!")
    else:
        print("Better luck next time!")

    return guesses


def main():
    print("Welcome to the Magic Number game!")
    play_again = "y"
    while play_again.lower() == "y":
        print("Ready to guess? Let's go!")
        guesses = play_game()
        if guesses <= 5:
            print("You unlocked the platinum level!")
        elif guesses <= 10:
            print("You unlocked the gold level!")
        else:
            print("You unlocked the silver level!")

        play_again = input("Do you want to play again? (y/n): ")

    print("Thanks for playing. See you next time!")


if __name__ == "__main__":
    main()
