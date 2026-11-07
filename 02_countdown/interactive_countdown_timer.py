# ==========================================
# Interactive Countdown Timer
# Created by Mohamed Nabil
# ==========================================

while True:

    number = int(input("Enter your number to count down: "))

    while number >= 0:

        print(f"Countdown: {number}")

        if number == 0:
            print("🎉 Time is up!")

        number -= 1

    user_choice = input(
        "\nDo you want another countdown? (y/n): "
    ).lower().strip()

    if user_choice == "n":
        print("\nThanks for using the Countdown Timer!")
        break