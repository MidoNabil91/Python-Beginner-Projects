# ==========================================
# Number Guessing Game
# Created by Mohamed Nabil
# ==========================================

import random

print("=" * 50)
print("🎯 Number Guessing Game")
print("Try to guess the secret number!")
print("=" * 50)

while True:

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    # Track player attempts
    attempts = 1

    while attempts < 11:

        guess = int(input("Guess number 🎯 = "))

        if guess == secret_number:
            print("🎉 Congratulations! Correct answer.")
            print(f"You won after {attempts} attempts!")
            break

        elif guess > secret_number:
            print("💡 The target number is smaller than that!")

        else:
            print("💡 The target number is greater than this!")

        attempts += 1

    # Player used all attempts
    if attempts == 11:
        print(f"💀 Game Over! The number was {secret_number}")

    # Ask to play again
    play_again = input(
        "\nPlay Again? (y/n): "
    ).lower().strip()

    if play_again != "y":
        print("👋 Thanks for playing!")
        break