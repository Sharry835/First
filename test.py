import random


def number_guessing_game():
    # Set the range and maximum attempts
    lower_bound = 1
    upper_bound = 100
    secret_number = random.randint(lower_bound, upper_bound)
    max_attempts = 7
    attempts = 0

    print("=== Welcome to the Number Guessing Game! ===")
    print(
        f"I'm thinking of a number between {lower_bound} and {upper_bound}."
    )
    print(f"You have {max_attempts} attempts to guess it.\n")

    while attempts < max_attempts:
        user_input = input(
            f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "
        ).strip()

        # Validate that the input is a valid integer
        if not user_input.lstrip("-").isdigit():
            print("Invalid input! Please enter a valid whole number.\n")
            continue

        guess = int(user_input)
        attempts += 1

        if guess < secret_number:
            print("Too low! Try a higher number.\n")
        elif guess > secret_number:
            print("Too high! Try a lower number.\n")
        else:
            print(
                f"🎉 Congratulations! You guessed the number {secret_number} correctly in {attempts} attempt(s)!"
            )
            return

    print(f"Game over! The secret number was {secret_number}. Better luck next time!")


if __name__ == "__main__":
    number_guessing_game()
