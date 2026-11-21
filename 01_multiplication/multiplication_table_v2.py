# ==============================================================================
# Interactive Multiplication Table Generator (v2.0)
# Author: Mohamed Nabil (@MidoNabil91)
# Description: Dual-mode CLI multiplication trainer featuring customizable
#              table generation (Learn Mode), randomized quizzes (Quiz Mode),
#              mistake tracking, and defensive input validation.
# ==============================================================================

import random


def get_valid_int(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")


def generate_table(number, limit=10):
    print(f"\n--- Multiplication Table for {number} (1 to {limit}) ---")
    for i in range(1, limit + 1):
        result = i * number
        print(f"{i} x {number} = {result}")
    print("-" * 40)


def start_quiz(number, questions_count=5):
    score = 0
    mistakes = []

    print(f"\n🧠 Starting Quiz for Table {number} ({questions_count} Questions)!")
    for q in range(1, questions_count + 1):
        multiplier = random.randint(1, 10)
        correct_answer = multiplier * number
        user_answer = get_valid_int(f"Q{q}: What is {multiplier} x {number}? ")

        if user_answer == correct_answer:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is {correct_answer}")
            mistakes.append(f"{multiplier} x {number} = {correct_answer} (Your answer: {user_answer})")

    print(f"\n🎯 Final Score: {score}/{questions_count}")
    if mistakes:
        print("📌 Review your mistakes:")
        for m in mistakes:
            print(f"  - {m}")


def main_lines():
    print("\n--- Multiplication Table Menu (v2.0) ---")
    print("=" * 50)
    print("1. Learn Mode (Generate Table)")
    print("2. Quiz Mode (Test Yourself)")
    print("3. Exit")
    print("=" * 50)


def main():
    while True:
        main_lines()
        user_choice = get_valid_int("Please choose an option (1-3): ")

        if user_choice == 1:
            number = get_valid_int("Enter table number: ")
            limit = get_valid_int("Enter max limit (e.g., 10 or 12): ")
            generate_table(number, limit)

        elif user_choice == 2:
            number = get_valid_int("Enter table number for the quiz: ")
            start_quiz(number, questions_count=5)

        elif user_choice == 3:
            print("\n👋 Thank you for using the Multiplication Table Generator!")
            break

        else:
            print("❌ Invalid choice! Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()