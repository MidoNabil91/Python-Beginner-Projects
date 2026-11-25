"""
==================================================
Project 6: Inventory Tracker System (v3.0 - OOP)
Author: Mohamed Nabil (@MidoNabil91)
Description: Object-Oriented procurement & warehouse control system featuring:
             - Encapsulated InventoryTracker Class Architecture
             - JSON Data Persistence (Auto-Load & Save)
             - Capacity Management & Automated Reorder Alerts
             - Financial Valuation (KWD) & Occupancy Rate (%)
             - Timestamped Audit Trail History (Bin Card)
==================================================
"""
import json
from datetime import datetime


class InventoryTracker:
    """Manages warehouse inventory, stock movements, and audit logs."""

    def __init__(self, filename="inv_tracker.json"):
        self.filename = filename
        self.data = self.load_invtracker()

    # --- Persistence Methods ---
    def load_invtracker(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {"inventory": {}, "transactions": []}

    def save_invtracker(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(self.data, file, indent=4, ensure_ascii=False)

    # --- Core Inventory Operations ---
    def add_material(self):
        material_code = input("Please Enter Material Code: ").strip().upper()
        if not material_code:
            print("❌ Material code cannot be empty!")
            return

        if material_code in self.data["inventory"]:
            print(f"⚠️ Material '{material_code}' already exists!")
            return

        while True:
            name = input("Material Name: ").strip().title()
            if name:
                break
            print("⚠️ Name cannot be empty!")

        while True:
            category = input("Category Name (e.g., PPE, Tools): ").strip().upper()
            if category:
                break
            print("⚠️ Category cannot be empty!")

        while True:
            try:
                stock = int(input("Please enter Current Stock: "))
                if stock >= 0:
                    break
                print("⚠️ Stock can't be less than 0!")
            except ValueError:
                print("⚠️ Invalid number! Enter a valid integer.")

        while True:
            try:
                max_capacity = int(input("Max Capacity for this item: "))
                if max_capacity > 0 and max_capacity >= stock:
                    break
                print(f"⚠️ Max Capacity must be > 0 and at least equal to Current Stock ({stock})!")
            except ValueError:
                print("⚠️ Invalid Capacity! Enter a valid integer.")

        while True:
            try:
                reorder_point = int(input("Enter Reorder Point: "))
                if 0 <= reorder_point <= max_capacity:
                    break
                print(f"⚠️ Reorder Point must be between 0 and Max Capacity ({max_capacity})!")
            except ValueError:
                print("⚠️ Invalid Reorder Point! Enter a valid integer.")

        while True:
            try:
                unit_price = float(input("Unit Price (KWD): "))
                if unit_price > 0:
                    break
                print("⚠️ Price must be greater than 0!")
            except ValueError:
                print("⚠️ Invalid price! Enter a valid number.")

        self.data["inventory"][material_code] = {
            "name": name,
            "category": category,
            "stock": stock,
            "max_capacity": max_capacity,
            "reorder_point": reorder_point,
            "unit_price": unit_price,
        }

        if stock > 0:
            self.data["transactions"].append({
                "type": "OPENING",
                "code": material_code,
                "qty": stock,
                "new_stock": stock,
                "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            })

        self.save_invtracker()
        print(f"✅ '{material_code}' added successfully!")
        return True

    def receive_stock(self):
        material_code = input("Enter Material Code: ").strip().upper()
        if material_code not in self.data["inventory"]:
            print(f"⚠️ '{material_code}' not found in inventory!")
            return

        current_stock = self.data["inventory"][material_code]["stock"]
        max_capacity = self.data["inventory"][material_code]["max_capacity"]
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
                print("⚠️ Invalid Quantity! Enter a valid integer.")

        self.data["inventory"][material_code]["stock"] += qty
        new_stock = self.data["inventory"][material_code]["stock"]

        self.data["transactions"].append({
            "type": "IN",
            "code": material_code,
            "qty": qty,
            "new_stock": new_stock,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        })

        self.save_invtracker()
        print(f"✅ '{qty}' pcs added successfully! New balance: {new_stock}")
        return True

    def issue_stock(self):
        material_code = input("Enter Material Code: ").strip().upper()
        if material_code not in self.data["inventory"]:
            print(f"⚠️ '{material_code}' not found in inventory!")
            return

        current_stock = self.data["inventory"][material_code]["stock"]
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
                print("⚠️ Invalid Quantity! Enter a valid integer.")

        self.data["inventory"][material_code]["stock"] -= qty_issue
        new_stock = self.data["inventory"][material_code]["stock"]

        self.data["transactions"].append({
            "type": "OUT",
            "code": material_code,
            "qty": qty_issue,
            "new_stock": new_stock,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        })

        self.save_invtracker()
        print(f"✅ '{qty_issue}' pcs of '{material_code}' issued successfully! Remaining: {new_stock}")

        # Trigger low-stock warning if balance drops to or below reorder point
        reorder_point = self.data["inventory"][material_code]["reorder_point"]
        if new_stock <= reorder_point:
            print(f"🚨 LOW STOCK ALERT: '{material_code}' reached reorder point ({new_stock} <= {reorder_point})!")

    # --- Reporting Methods ---
    def reorder_report(self):
        if not self.data["inventory"]:
            print("📭 Inventory is empty!")
            return

        print("\n🚨 REORDER ALERT REPORT")
        print("=" * 55)
        found = False

        for code, info in self.data["inventory"].items():
            if info["stock"] <= info["reorder_point"]:
                print(f"⚠️ [{code}] {info['name']} | Stock: {info['stock']} (Reorder Point: {info['reorder_point']})")
                found = True

        if not found:
            print("✅ All items are above reorder point!")
        print("=" * 55)

    def view_inventory(self):
        if not self.data["inventory"]:
            print("📭 Inventory is empty!")
            return

        print("\n📦 CURRENT INVENTORY & VALUATION REPORT")
        print("=" * 75)
        total_value = 0

        for code, info in self.data["inventory"].items():
            item_value = info["stock"] * info["unit_price"]
            total_value += item_value
            occupancy = (info["stock"] / info["max_capacity"]) * 100
            print(
                f"🔹 [{code}] {info['name']} ({info['category']}) | "
                f"Stock: {info['stock']}/{info['max_capacity']} ({occupancy:.1f}%) | "
                f"Value: {item_value:.3f} KWD"
            )

        print("=" * 75)
        print(f"💰 TOTAL WAREHOUSE VALUATION: {total_value:.3f} KWD")
        print("=" * 75)

    def view_transactions(self):
        if not self.data["transactions"]:
            print("📭 No transactions recorded yet!")
            return

        print("\n📜 WAREHOUSE TRANSACTION HISTORY (BIN CARD)")
        print("=" * 70)
        for tx in self.data["transactions"]:
            print(
                f"🕒 {tx['date']} | [{tx['type']:<7}] | "
                f"Code: {tx['code']} | Qty: {tx['qty']} | Balance: {tx['new_stock']}"
            )
        print("=" * 70)

    # --- CLI Interface ---
    def show_menu(self):
        print("\n" + "=" * 45)
        print("   📦 INVENTORY TRACKER SYSTEM (v3.0 - OOP)")
        print("=" * 45)
        print("1. Add New Material")
        print("2. Receive Stock (IN)")
        print("3. Issue Stock (OUT)")
        print("4. View Inventory & Valuation Report")
        print("5. View Reorder Alert Report")
        print("6. View Transaction History")
        print("7. Exit")
        print("=" * 45)

    def main(self):
        while True:
            self.show_menu()
            choice = input("Choose (1-7): ").strip()
            if choice == "1":
                self.add_material()
            elif choice == "2":
                self.receive_stock()
            elif choice == "3":
                self.issue_stock()
            elif choice == "4":
                self.view_inventory()
            elif choice == "5":
                self.reorder_report()
            elif choice == "6":
                self.view_transactions()
            elif choice == "7":
                print("👋 Goodbye! All data is saved safely.")
                break
            else:
                print("❌ Invalid choice! Please enter a number from 1 to 7.")


if __name__ == "__main__":
    tracker = InventoryTracker()
    tracker.main()