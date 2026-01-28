import random
def number_guessing_game():
    """A simple number guessing game where the player tries to guess a random number."""

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print()

    # Generate a random number between 1 and 100
    secret_number = 6
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        try:
            # Get player's guess
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
            attempts += 1

            # Check the guess
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100!")
                continue

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"\n🎉 Congratulations! You guessed it in {attempts} attempts!")
                print(f"The number was {secret_number}!")
                return

            print()

        except ValueError:
            print("Invalid input! Please enter a valid number.")
            print()

    # If player runs out of attempts
    print(f"\n😔 Game Over! You've used all {max_attempts} attempts.")
    print(f"The secret number was {secret_number}. Better luck next time!")


def main():
    """Main function to run the game with replay option."""
    while True:
        number_guessing_game()

        # Ask if player wants to play again
        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if play_again not in ['yes', 'y']:
            print("Thanks for playing! Goodbye!")
            break
        print("\n" + "=" * 50 + "\n")

main()