# ==============================================================================
# Simple & Continuous Calculator (v2.0)
# Author: Mohamed Nabil (@MidoNabil91)
# Description: Modular CLI calculator supporting continuous chained operations,
#              dictionary-mapped arithmetic functions, zero-division protection,
#              defensive numeric validation, and session calculation history.
# ==============================================================================


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


def modulo(num1, num2):
    return num1 % num2


def power(num1, num2):
    return num1 ** num2


OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": division,
    "%": modulo,
    "**": power,
}


def get_valid_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")


def get_valid_operation():
    while True:
        process = input("Choose operation (+ , - , * , / , % , **): ").strip()
        if process in OPERATIONS:
            return process
        print("❌ Invalid operation! Please choose from (+ , - , * , / , % , **).")


def show_history(history):
    print("\n📜 --- Calculation History ---")
    if not history:
        print("No calculations recorded yet.")
    else:
        for idx, item in enumerate(history, start=1):
            print(f"  {idx}. {item}")
    print("-" * 30)


def main():
    print("=" * 50)
    print("🧮 Simple & Continuous Calculator (v2.0)")
    print("=" * 50)

    history = []

    while True:
        num1 = get_valid_float("\nEnter first number: ")

        while True:
            process = get_valid_operation()
            num2 = get_valid_float("Enter next number: ")

            if process in ("/", "%") and num2 == 0:
                print("❌ Error: Division or modulo by zero is not allowed.")
                continue

            total = OPERATIONS[process](num1, num2)
            record = f"{num1} {process} {num2} = {total}"
            history.append(record)

            print(f"👉 Result: {record}")
            print("=" * 50)

            while True:
                choice = input(
                    f"Type 'y' to continue with {total}, 'n' for new calculation, "
                    "'h' for history, or 'q' to quit: "
                ).lower().strip()

                if choice == "h":
                    show_history(history)
                elif choice in ("y", "n", "q"):
                    break
                else:
                    print("❌ Invalid choice! Please enter 'y', 'n', 'h', or 'q'.")

            if choice == "y":
                num1 = total
            elif choice == "n":
                print("=" * 50)
                break
            elif choice == "q":
                show_history(history)
                print("👋 Thanks for using Calculator!")
                return


if __name__ == "__main__":
    main()