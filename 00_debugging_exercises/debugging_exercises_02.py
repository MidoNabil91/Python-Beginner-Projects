# """
# ==================================================
# Python Debugging & Logic Fixing Exercises
# Author: Mohamed Nabil
# Description: Practice code reviews, bug fixing, variable scope, 
#              and flow control in Python.
# ==================================================
# """
# ================================================
# Challenge 1: Login Attempts Counter
# Bug: Missing loop counter update causing infinite loop, and unconditional locked message outside the loop.
# ================================================
print("--- Challenge 1: Login Attempts ---")

# Fixed Code:
username = "admin"
password = 1234
attempts = 1

while attempts <= 3:
    user = input("Username: ")
    pwd = int(input("Password: "))

    if user == username and pwd == password:
        print("Login Success")
        break
    else:
        print("Wrong Credentials")

    attempts += 1  # Increment counter to prevent infinite loop
else:
    print("Account Locked")  # Only runs if loop completes all 3 attempts naturally

print()
# ================================================
# Challenge 2: Employee Bonus Calculation
# Bug: Variable 'bonus' is only initialized inside the 'if' condition, causing NameError when salary <= 1000.
# ================================================
print("--- Challenge 2: Employee Bonus ---")

# Fixed Code:
salary = 500
bonus = 0  # Initialize variable with default value to prevent NameError

if salary > 1000:
    bonus = salary * 0.10

print(f"Salary: ${salary} | Bonus: ${bonus}\n")
#Always consider what happens when a condition is False.
# # ================================================
# Challenge 3: Procurement Approval Logic
# Bug: Incorrect conditional hierarchy where
# lower threshold (>= 5000) was checked
# before higher threshold (>= 10000),
# causing larger amounts to bypass Director Approval.
# ================================================
print("--- Challenge 3: Procurement Approval Logic ---")

# Fixed Code:
amount = 12000

if amount >= 10000:  # Highest threshold must be evaluated first
    print("Approval Level Required: Director Approval")
elif amount >= 5000:
    print("Approval Level Required: Manager Approval")
else:
    print("Approval Level Required: Auto Approved")

print()

# Order matters in if and elif.
# Business logic is just as important as syntax.
# ================================================
# Challenge 4: Average Calculator
# Bug: Missing parentheses caused operator precedence issue,
# calculating 'a + b + (c / 3)' instead of the true average.
# ================================================
print("--- Challenge 4: Average Calculator ---")

# Fixed Code:
def calculate_average(a, b, c):
    return (a + b + c) / 3  # Parentheses enforce correct order of addition before division

result = calculate_average(90, 80, 70)
print(f"Calculated Average: {result}\n")
# Always use parentheses when calculating averages: (a + b + c) / 3 not a + b + c / 3
# ================================================
# Challenge 5: Inventory Counter
# Bug: Boundary condition logic error using '>=' printed 'Current Stock: 0' before 'Out Of Stock', incorrectly stating stock was available when 0 remained.
# ================================================
print("--- Challenge 5: Inventory Counter ---")

# Fixed Code:
stock = 10

while stock > 0:  # Loop stops strictly when stock reaches 0
    print("Current Stock:", stock)
    stock -= 1

print("Out Of Stock!\n")
# stops before zero.
# Always understand the business requirement before changing the code.
# ================================================
# Challenge 6: Function Return Value
# Bug: Missing 'return' statement inside the function, causing it to return 'None' by default and triggering a TypeError on addition.
# ================================================
print("--- Challenge 6: Calculate Total with Return ---")

# Fixed Code:
def calculate_total(price, qty):
    return price * qty  # Added return statement to send the calculated value back

result = calculate_total(100, 5)
print(f"Total with Addition: ${result + 50}\n")



# Key Takeaways
# ✅ Variables must be initialized.
# ✅ Loops need proper counters.
# ✅ Parentheses matter in calculations.
# ✅ Condition order affects program logic.
# ✅ Debugging is not only about fixing errors, it's about understanding the program flow.