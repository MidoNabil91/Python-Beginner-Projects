# ==========================================
# Simple & Continuous Calculator
# Created by Mohamed Nabil
# ==========================================

import sys

print("=" * 50)
print("🧮 Calculator Project")
print("=" * 50)

while True:
    num1 = float(input("Enter first Number = "))
    
    while True:
        process = input("Choose operation (+ , - , * , / , % , **): ").strip()
        num2 = float(input("Enter next Number = "))

        if process == "+":
            total = num1 + num2
        elif process == "-":
            total = num1 - num2
        elif process == "*":
            total = num1 * num2
        elif process == "/":
            if num2 == 0:
                print("❌ Error: Division by zero is not allowed.")
                continue
            total = num1 / num2
        elif process == "%":
            if num2 == 0:
                print("❌ Error: Modulo by zero is not allowed.")
                continue
            total = num1 % num2
        elif process == "**":
            total = num1 ** num2
        else:
            print("❌ Invalid operation! Please try again.")
            continue

        print(f"👉 Result: {num1} {process} {num2} = {total}")
        print("=" * 50)

        # The option to continue with the existing total
        choice = input(f"Type 'y' to continue calculating with {total}, 'n' for new calculation, or 'q' to quit: ").lower().strip()

        if choice == 'y':
            num1 = total  # The old output as num1 for the next process
        elif choice == 'n':
            print("=" * 50)
            break  # Exiting the inner loop to start with a new number
        else:
            print("👋 Thanks for using Calculator!")
            sys.exit()  # Terminate the entire program