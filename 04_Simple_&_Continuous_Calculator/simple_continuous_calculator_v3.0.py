# ==============================================================================
# Simple & Continuous Calculator (v3.0 - OOP Version)
# Author: Mohamed Nabil (@MidoNabil91)
# Description: Object-Oriented CLI calculator encapsulating arithmetic
#              operations, validation, and session history inside a Calculator class.
# ==============================================================================


class Calculator:
    def __init__(self):

        self.history = []
        self.operations = {
            "+": self.add,
            "-": self.subtract,
            "*": self.multiply,
            "/": self.division,
            "%": self.modulo,
            "**": self.power,
        }

    # --- (Methods) ---
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def division(self, num1, num2):
        return num1 / num2

    def modulo(self, num1, num2):
        return num1 % num2

    def power(self, num1, num2):
        return num1 ** num2

    # --- Valid ---
    def get_valid_float(self, prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("❌ Invalid input! Please enter a valid number.")

    def get_valid_operation(self):
        while True:
            process = input("Choose operation (+ , - , * , / , % , **): ").strip()
            if process in self.operations:
                return process
            print("❌ Invalid operation! Please choose from (+ , - , * , / , % , **).")

    # --- [Process and Record] ---
    def calculate(self, num1, process, num2):
        total = self.operations[process](num1, num2)
        record = f"{num1} {process} {num2} = {total}"
        self.history.append(record)
        return total, record

    # --- View History ---
    def show_history(self):
        print("\n📜 --- Calculation History ---")
        if not self.history:
            print("No calculations recorded yet.")
        else:
            for idx, item in enumerate(self.history, start=1):
                print(f"  {idx}. {item}")
        print("-" * 30)

    # --- App Working ---
    def run(self):
        print("=" * 50)
        print("🧮 Simple & Continuous Calculator (v3.0 - OOP)")
        print("=" * 50)

        while True:
            num1 = self.get_valid_float("\nEnter first number: ")

            while True:
                process = self.get_valid_operation()
                num2 = self.get_valid_float("Enter next number: ")

                if process in ("/", "%") and num2 == 0:
                    print("❌ Error: Division or modulo by zero is not allowed.")
                    continue

                total, record = self.calculate(num1, process, num2)
                print(f"👉 Result: {record}")
                print("=" * 50)

                while True:
                    choice = input(
                        f"Type 'y' to continue with {total}, 'n' for new calculation, "
                        "'h' for history, or 'q' to quit: "
                    ).lower().strip()

                    if choice == "h":
                        self.show_history()
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
                    self.show_history()
                    print("👋 Thanks for using Calculator!")
                    return


if __name__ == "__main__":
    calc = Calculator()  
    calc.run()           