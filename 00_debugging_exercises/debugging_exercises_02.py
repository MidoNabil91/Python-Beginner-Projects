# """
# ==================================================
# Python Debugging & Logic Fixing Exercises
# Author: Mohamed Nabil
# Description: Practice code reviews, bug fixing, variable scope, 
#              and flow control in Python.
# ==================================================
# """
# ================================================
# Challenge 1 - Login Attempts
# Bug: The attempts variable never changes.
# ================================================
username = "admin"
password = 1234

attempts = 1

while attempts <= 3:
    user = input("Username: ")
    pwd = int(input("Password: "))

    if user == username and pwd == password:
        print("Login Success")
        break

    print("Wrong Credentials")

print("Account Locked")

# was missing, causing an infinite loop when incorrect credentials are entered.
# Also, "Account Locked" should only appear after all attempts are used.

# ====================================================
# Challenge 1 - Login Attempts ### Correct Answer ###
# ====================================================

username = "admin"
password = 1234

attempts = 1

while attempts <= 3:
    user = input("Username: ")
    pwd = int(input("Password: "))

    if user == username and pwd == password:
        print("Login Success")
        break # break prevents the else block from running.
    else:
        print("Wrong Credentials")

    attempts += 1 # Counters must be updated inside loops.

else: # while...else is useful when the loop finishes naturally.
    print("Account Locked")
# ================================================
# Challenge 2 - Employee Bonus
# Bug: When salary is less than or equal to 1000: bonus is never created.
#           This causes: NameError
# ================================================
salary = 500

if salary > 1000:
    bonus = salary * 0.10

print("Bonus:", bonus)
# ================================================
# Challenge 2 - Employee Bonus ### Correct Answer ###
# ================================================
salary = 500
bonus = 0 # Variables should be initialized before use.

if salary > 1000:
    bonus = salary * 0.10

print("Bonus:", bonus)
#Always consider what happens when a condition is False.
# ================================================
# Challenge 3 - Procurement Approval Logic
# Bug: The approval hierarchy is incorrect.
# Bug: A higher approval level should be checked first.
# ================================================
amount = 2500

if amount >= 5000:
    print("Manager Approval")

elif amount >= 10000:
    print("Director Approval")

else:
    print("Auto Approved")

# ================================================
# Challenge 3 - Procurement Approval Logic ## correct answer ##
# ================================================
amount = 2500

if amount >= 10000:
    print("Director Approval")

elif amount >= 5000:
    print("Manager Approval")

else:
    print("Auto Approved")
# Order matters in if and elif.
# Business logic is just as important as syntax.
# ================================================
# Challenge 4 - Average Calculator
# Bug: Operator precedence causes Python to calculate: 70 / 3
# Bug: The result is not the true average.
# ================================================
def calculate_average(a, b, c):
    average = a + b + c / 3
    return average

result = calculate_average(90, 80, 70)

print(result)
# ================================================
# Challenge 4 - Average Calculator ## correct answer ##
# ================================================
def calculate_average(a, b, c):
    return (a + b + c) / 3

result = calculate_average(90, 80, 70)

print(result)
# Always use parentheses when calculating averages: (a + b + c) / 3 not a + b + c / 3
# ================================================
# Challenge 5 - Inventory Counter
# Bug: The loop prints: 11 time.
# Bug: then Out Of Stock
# ================================================
stock = 10

while stock >= 0:
    print("Current Stock:", stock)
    stock -= 1

print("Out Of Stock")
# ================================================
# Challenge 5 - Inventory Counter ## correct answer ##
# ================================================
stock = 10

while stock > 0:
    print("Current Stock:", stock)
    stock -= 1

print("Out Of Stock")

# stops before zero.
# Always understand the business requirement before changing the code.

# Key Takeaways
# ✅ Variables must be initialized.
# ✅ Loops need proper counters.
# ✅ Parentheses matter in calculations.
# ✅ Condition order affects program logic.
# ✅ Debugging is not only about fixing errors, it's about understanding the program flow.