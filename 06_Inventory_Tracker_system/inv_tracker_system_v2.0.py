"""
==================================================
Project 6: Inventory Tracker System (v2.0)
Author: Mohamed Nabil
Description: Persistent procurement & warehouse control system featuring:
             - JSON Data Persistence (Auto-Load & Save)
             - Modular Function Architecture
             - Capacity Management & Reorder Alerts
             - Financial Valuation (KWD) & Occupancy Rate (%)
             - Timestamped Audit Trail History (Bin Card)
==================================================
"""

import json
from datetime import datetime

def load_invtracker(): # Load the File
    try:
        with open("inv_tracker.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"inventory": {}, "transactions": []}


def save_invtracker(invtracker): # Save Process
    with open("inv_tracker.json", "w", encoding="utf-8") as file:
        json.dump(invtracker, file, indent=4, ensure_ascii=False)


def add_material(data): # Main to Add Materials :
    material_code = input("Please Enter Material Code: ").strip().upper() # First of all the Code for each Material 
    if not material_code:
        print("❌ Material code cannot be empty!")
        return

    if material_code in data["inventory"]:
        print(f"⚠️ Material '{material_code}' already exists!")
        return
    
# 1. Name
    while True:
        name = input("Material Name: ").strip().title()
        if not name:
            print("⚠️ Name cannot be empty!")
            continue
        break

# 2. Category
    while True:
        category = input("Category Name (e.g., PPE, Tools): ").strip().upper()
        if not category:
            print("⚠️ Category cannot be empty!")
            continue
        break

# 3. Current Stock
    while True:
        try:
            stock = int(input("Please enter Current Stock: "))
            if stock < 0:
                print("⚠️ Stock can't be less than 0!")
                continue
            break
        except ValueError:
            print("⚠️ Invalid number! Enter a valid Number.")

    # 4. Max Capacity
    while True:
        try:
            max_capacity = int(input("Max Capacity for this item: "))
            if max_capacity <= 0 or max_capacity < stock:
                print(f"⚠️ Max Capacity must be > 0 and at least equal to Current Stock ({stock})!")
                continue
            break
        except ValueError:
            print("⚠️ Invalid Capacity! Enter a valid Number.")
        
# 5. Reorder Point
    while True:
        try:
            reorder_point = int(input("Enter Reorder Point: "))
            if reorder_point < 0 or reorder_point > max_capacity:
                print(f"⚠️ Reorder Point must be between 0 and Max Capacity ({max_capacity})!")
                continue
            break
        except ValueError:
            print("⚠️ Invalid Reorder Point! Enter a valid integer.")

# 6. Unit Price
    while True:
        try:
            unit_price = float(input("Unit Price (KWD): "))
            if unit_price <= 0:
                print("⚠️ Price must be greater than 0!")
                continue
            break
        except ValueError:
            print("⚠️ Invalid price! Enter a valid number.")
    
# 7. Adding .. Process
    data["inventory"][material_code] = {
        "name": name,
        "category": category,
        "stock": stock,
        "max_capacity": max_capacity,
        "reorder_point": reorder_point,
        "unit_price": unit_price
    }

    if stock > 0:
        data["transactions"].append({
            "type": "OPENING",
            "code": material_code,
            "qty": stock,
            "new_stock": stock,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M")
        })

    save_invtracker(data)
    print(f"✅ '{material_code}' added successfully!")
    return True

def receive_stock(data): # For in Material ,,
    material_code = input("Enter Material Code: ").strip().upper()
    if material_code not in data["inventory"]:
        print(f"⚠️ '{material_code}' not found in inventory!")
        return
    # to be sure if Qty before adding
    current_stock = data["inventory"][material_code]["stock"]
    max_capacity = data["inventory"][material_code]["max_capacity"]
    available_space = max_capacity - current_stock

    while True: 
        try:
            qty = int(input("Please enter Received Quantity: "))
            if qty <= 0:
                print("⚠️ Quantity must be greater than 0!")
                continue
            if (current_stock + qty) > max_capacity:
                print(f"⚠️ Exceeds max capacity ({max_capacity})! Available space: {available_space} pcs.")
                continue
            break
        except ValueError:
            print("⚠️ Invalid Quantity! Enter a valid number.")
            
    data["inventory"][material_code]["stock"] += qty
    
    new_stock = data["inventory"][material_code]["stock"]

    data["transactions"].append({
        "type": "IN",
        "code": material_code,
        "qty": qty,
        "new_stock": new_stock,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    })

    save_invtracker(data)
    print(f"✅ '{qty}' added successfully!")
    return True

def issue_stock(data): # For Out Material
    material_code = input("Enter Material Code: ").strip().upper()
    if material_code not in data["inventory"]:
        print(f"⚠️ '{material_code}' not found in inventory!")
        return

    current_stock = data["inventory"][material_code]["stock"]
    if current_stock == 0:
        print(f"⚠️ '{material_code}' is out of stock!")
        return

    while True:
        try:
            qty_issue = int(input(f"Enter Quantity to issue (Available: {current_stock}): "))
            if qty_issue <= 0:
                print("⚠️ Quantity must be greater than 0!")
                continue
            if qty_issue > current_stock:
                print(f"⚠️ Insufficient stock! Only {current_stock} pcs available.")
                continue
            break
        except ValueError:
            print("⚠️ Invalid Quantity! Enter a valid number.")

    # Subtract the quantity from the original dictionary
    data["inventory"][material_code]["stock"] -= qty_issue
    new_stock = data["inventory"][material_code]["stock"]

    # Recording disbursement transactions
    data["transactions"].append({
        "type": "OUT",
        "code": material_code,
        "qty": qty_issue,
        "new_stock": new_stock,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    })

    save_invtracker(data)
    print(f"✅ '{qty_issue}' pcs of '{material_code}' issued successfully! Remaining: {new_stock}")

    # Reorder Point Alert
    reorder_point = data["inventory"][material_code]["reorder_point"]
    if new_stock <= reorder_point:
        print(f"🚨 LOW STOCK ALERT: '{material_code}' reached reorder point ({new_stock} <= {reorder_point})!")

def reorder_report(data):
    if not data["inventory"]:
        print("📭 Inventory is empty!")
        return

    print("\n🚨 REORDER ALERT REPORT")
    print("=" * 55)
    found = False

    for code, info in data["inventory"].items():
        if info["stock"] <= info["reorder_point"]:
            print(f"⚠️ [{code}] {info['name']} | Stock: {info['stock']} (Reorder Point: {info['reorder_point']})")
            found = True

    if not found:
        print("✅ All items are above reorder point!")
    print("=" * 55)

def view_inventory(data):
    if not data["inventory"]:
        print("📭 Inventory is empty!")
        return

    print("\n📦 CURRENT INVENTORY & VALUATION REPORT")
    print("=" * 75)
    total_value = 0

    for code, info in data["inventory"].items():
        item_value = info["stock"] * info["unit_price"]
        total_value += item_value
        occupancy = (info["stock"] / info["max_capacity"]) * 100
        print(f"🔹 [{code}] {info['name']} ({info['category']}) | Stock: {info['stock']}/{info['max_capacity']} ({occupancy:.1f}%) | Value: {item_value:.3f} KWD")

    print("=" * 75)
    print(f"💰 TOTAL WAREHOUSE VALUATION: {total_value:.3f} KWD")
    print("=" * 75)

def view_transactions(data):
    if not data["transactions"]:
        print("📭 No transactions recorded yet!")
        return

    print("\n📜 WAREHOUSE TRANSACTION HISTORY (BIN CARD)")
    print("=" * 70)
    for tx in data["transactions"]:
        print(f"🕒 {tx['date']} | [{tx['type']:<7}] | Code: {tx['code']} | Qty: {tx['qty']} | Balance: {tx['new_stock']}")
    print("=" * 70)


def show_menu(): # Only Print Main Menu #
    """ Displays the list of options to the user. """
    print("\n" + "=" * 45)
    print("   📦 INVENTORY TRACKER SYSTEM (v2.0)")
    print("=" * 45)
    print("1. Add New Material")
    print("2. Receive Stock (IN)")
    print("3. Issue Stock (OUT)")
    print("4. View Inventory & Valuation Report")
    print("5. View Reorder Alert Report")
    print("6. View Transaction History")
    print("7. Exit")
    print("=" * 45)

def main():
    data = load_invtracker()
    while True:
        show_menu()

        choice = input("Choose (1-7): ").strip()
        if choice == "1":
            add_material(data)
        elif choice == "2":
            receive_stock(data)
        elif choice == "3":
            issue_stock(data)
        elif choice == "4":
            view_inventory(data)
        elif choice == "5":
            reorder_report(data)
        elif choice == "6":
            view_transactions(data)
        elif choice == "7":
            print("👋 Goodbye! All data is saved safely.")
            break
        else:
            print("❌ Invalid choice! Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()