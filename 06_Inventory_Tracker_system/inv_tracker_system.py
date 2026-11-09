"""
==================================================
Project 6: Inventory Tracker Mini System (v1.0)
Author: Mohamed Nabil
Description: A simple procurement & inventory control system to manage 
             stock levels, reorder alerts, and transactions.
==================================================
"""

stock = 10

def add_stock(stock, qty):
    return stock + qty

def remove_stock(stock, qty):
    return stock - qty

def check_stock(stock):
    return stock

while True:
    print("\n" + "=" * 40)
    print("      📦 INVENTORY TRACKER SYSTEM")
    print("=" * 40)
    print("1. Add Stock")
    print("2. Remove Stock")
    print("3. Check Stock")
    print("4. Exit")
    print("=" * 40)

    user_input = int(input("Choose (1-4): "))

    if user_input == 1:
        qty = int(input("Enter quantity to add: "))
        stock = add_stock(stock, qty)
        print("✅ Stock Added Successfully!")
        print("Current Stock =", stock)

    elif user_input == 2:
        qty = int(input("Enter quantity to remove: "))
        if qty > stock:
            print("❌ Not enough stock available!")
        else:
            stock = remove_stock(stock, qty)
            print("✅ Stock Removed Successfully!")
            print("Current Stock =", stock)

    elif user_input == 3:
        print("📊 Current Stock =", check_stock(stock))

    elif user_input == 4:
        print("👋 Good Bye!")
        break

    else:
        print("❌ Invalid Choice! Please enter 1, 2, 3, or 4.")

    # Low Stock Warning check (runs only while inside active session)
    if stock <= 5:
        print("⚠️ Warning: Low Stock Level! Consider reordering soon.")