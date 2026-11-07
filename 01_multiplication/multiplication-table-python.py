# ==========================================
# Interactive Multiplication Table Generator
# Created by Mohamed Nabel
# ==========================================

# First multiplication table
number = int(input("Enter a number: "))

for i in range(1, 11):
    result = i * number
    print(f"{i} x {number} = {result}")

print("-" * 30)

# Generate additional tables
while True:

    number = int(input("Enter a new number (0 to exit): "))

    # Exit condition
    if number == 0:
        print("\nThank you for using the Multiplication Table Generator!")
        break

    print(f"\nMultiplication Table for {number}")
    print("-" * 30)

    for i in range(1, 11):
        result = i * number
        print(f"{i} x {number} = {result}")

    print("-" * 30)