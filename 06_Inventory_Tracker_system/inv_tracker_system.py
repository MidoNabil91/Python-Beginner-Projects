"""
==================================================
Project 6: Inventory Tracker Mini System (v1.4)
Author: Mohamed Nabil
Description: Procurement & inventory control system featuring:
             - Capacity Management & Reorder Alerts
             - Financial Valuation (KWD)
             - Warehouse Occupancy Rate (%)
             - Cumulative Movement Metrics (+In / -Out)
             - Session Audit Trail History Log
==================================================
"""

stock = 10                  # Initial stock quantity.
max_capacity = 500          # Maximum warehouse capacity.
unit_price_val = 15.0       
reorder_point = 5          
total_add = 0               
total_removed = 0           

# String-based log to store session transactions
history_log = "--- SESSION TRANSACTION LOG ---\n"


def add_stock(stock, qty): 
    return stock + qty


def remove_stock(stock, qty): 
    return stock - qty


def calculate_inventory_value(stock, price):  
    return stock * price


def occupied_inv(stock, max_capacity):
    return (stock / max_capacity) * 100


while True:
    print("\n" + "=" * 40)
    print("      📦 INVENTORY TRACKER SYSTEM (v1.4)")
    print("=" * 40)
    print("1. Add Stock")
    print("2. Remove Stock")
    print("3. Check Stock Status")
    print("4. Check Inventory Valuation Report")
    print("5. View Transaction History")
    print("6. View Movement Report")
    print("7. Exit")
    print("=" * 40)

    user_input = int(input("Choose (1-7): "))

    if user_input == 1:
        qty = int(input("Enter quantity to add: "))
        if qty <= 0:
            print("❌ Quantity must be greater than zero.")
            continue
        elif (stock + qty) > max_capacity:
            available_space = max_capacity - stock
            print(f"❌ Cannot add {qty} pcs! Max capacity is {max_capacity}.")
            print(f"💡 Space available: {available_space} pcs.")
        else:
            stock = add_stock(stock, qty)
            occupied = occupied_inv(stock, max_capacity)
            total_add += qty
            print("✅ Stock Added Successfully!")
            print(f"Current Stock = {stock} / {max_capacity} Pieces")
            print(f"📈 Warehouse Usage: {occupied:.2f}%")

            # Record in history log
            history_log += f"➕ Added: {qty} pcs | New Stock: {stock} pcs\n"

    elif user_input == 2:
        qty = int(input("Enter quantity to remove: "))

        if qty <= 0:
            print("❌ Quantity must be greater than zero.")
            continue
        elif qty > stock:
            print("❌ Not enough stock available!")
        else:
            stock = remove_stock(stock, qty)
            occupied = occupied_inv(stock, max_capacity)
            total_removed -= qty
            print("✅ Stock Removed Successfully!")
            print(f"Current Stock = {stock} Pieces")
            print(f"📉 Warehouse Usage: {occupied:.2f}%")

            # Record in history log
            history_log += f"➖ Removed: {qty} pcs | New Stock: {stock} pcs\n"

    elif user_input == 3:
        occupied = occupied_inv(stock, max_capacity)
        print(f"📊 Current Stock Status: {stock} / {max_capacity} Pieces ({occupied:.2f}% Usage)")

    elif user_input == 4:
        inv_value = calculate_inventory_value(stock, unit_price_val)
        print("\n" + "=" * 40)
        print("💵 INVENTORY VALUE REPORT")
        print("=" * 40)
        print(f"📦 Stock Quantity : {stock} Pieces")
        print(f"💵 Unit Price     : {unit_price_val:.3f} KWD")
        print(f"💰 Inventory Value: {inv_value:.3f} KWD")
        print("=" * 40)

    elif user_input == 5:
        print("\n" + "=" * 40)
        print(history_log)
        print("=" * 40)

    elif user_input == 6:
        print("\n" + "=" * 40)
        print("📦 STOCK MOVEMENT REPORT")
        print("=" * 40)
        print(f"⬆️ Stock Added   : +{total_add}")
        print(f"⬇️ Stock Removed : {total_removed}")
        print(f"📦 Current Stock  : {stock}")
        print("=" * 40)

    elif user_input == 7:
        print("👋 Good Bye!")
        break

    else:
        print("❌ Invalid Choice! Please enter a number from 1 to 7.")

    # Low Stock Warning check
    if stock <= reorder_point:
        print(f"⚠️ Warning: Low Stock Level! Stock is <= {reorder_point}.")