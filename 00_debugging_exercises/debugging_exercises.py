# """
# ==================================================
# Python Debugging & Logic Fixing Exercises
# Author: Mohamed Nabil
# Description: Practice code reviews, bug fixing, variable scope, 
#              and flow control in Python.
# ==================================================
# """

# ================================================
# Challenge 1: Discount Function (Return vs Print)
# Bug: Missing return statement caused function to yield None.
# ================================================
print("--- Challenge 1: Discount Function ---")

# Fixed Code:
def apply_discount(price):
    if price >= 100:
        return price * 0.90  # Returns calculated value directly
    else:
        return price

total = apply_discount(150)
print(f"Total price after discount: ${total}\n")


# ================================================
# Challenge 2: Inventory Check (Assignment vs Comparison)
# Bug: Using '=' instead of '==' in conditional statement.
# ================================================
print("--- Challenge 2: Inventory Check ---")

# Fixed Code:
def check_stock(quantity):
    if quantity == 0:  # Fixed comparison operator
        return "Out of Stock!"
    elif quantity < 10:
        return "Low Stock! Reorder soon."
    else:
        return "Stock Level OK."

user_qty = 5
print(f"Stock Status for {user_qty} items: {check_stock(user_qty)}\n")


# ================================================
# Challenge 3: Attempts Loop (Infinite Loop & while-else)
# Bug: Missing counter increment and logic flow error.
# ================================================
print("--- Challenge 3: Password Attempts ---")

# Fixed Code using while-else:
attempts = 0
correct_pass = "admin123"

# Simulated loop test
while attempts < 3:
    password = "wrong_pass"  # Simulation of user input
    if password == correct_pass:
        print("Access Granted!")
        break
    else:
        print("Wrong password, try again.")
    attempts += 1  # Increment counter to prevent infinite loop
else:
    print("Account Locked!\n")


# ================================================
# Challenge 4: Procurement Order Cost (Unbound Local Variable)
# Bug: 'total' variable not assigned in the 'else' branch.
# ================================================
print("--- Challenge 4: Procurement Order Cost ---")

# Fixed Code:
def calculate_order_total(quantity, unit_price):
    subtotal = quantity * unit_price
    
    if subtotal > 1000:
        discount = subtotal * 0.05
        return subtotal - discount
    else:
        return subtotal  # Handled case where subtotal <= 1000

order1 = calculate_order_total(5, 100)
print(f"Order 1 Total: ${order1}\n")


# ================================================
# Challenge 5: Add Suppliers to List (Scope & Mutability)
# Bug: Return inside function was redundant for mutable list modifications.
# ================================================
print("--- Challenge 5: Suppliers List Scope ---")

suppliers = ["Eaton", "Hyva", "Bussmann"]

# Fixed Code:
def add_supplier(new_supplier):
    suppliers.append(new_supplier)  # Modifies global list directly in memory

add_supplier("Loctite")
print("Supplier added successfully!")
print("Updated Suppliers List:", suppliers, "\n")


# ================================================
# Challenge 6: Accumulative Stock Counter (Early Return in Loop)
# Bug: Return statement inside for-loop aborted loop on first iteration.
# ================================================
print("--- Challenge 6: Accumulative Stock Counter ---")

# Fixed Code:
def check_total_stock(stock_list):
    total = 0
    for item in stock_list:
        total += item  # Complete full loop iteration

    if total >= 100:
        return "Stock is Sufficient"
    else:
        return "Need Urgent Reorder"

warehouse_stocks = [30, 45, 40]
result = check_total_stock(warehouse_stocks)
print(f"Warehouse Stock Result: {result}\n")