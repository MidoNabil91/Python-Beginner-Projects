# ==============================================================================
# Debugging Exercises - Set 6: Inventory, Procurement & POS Logic (12 Challenges)
# Author: Mohamed Nabil
# Format: Each challenge shows the original buggy snippet followed by the
#         root-cause explanation and the fixed implementation.
# ==============================================================================
import json


# ------------------------------------------------------------------------------
# Challenge 1: Discount & Tax Calculator (Logic / Operator Precedence)
# ------------------------------------------------------------------------------
# ❌ Buggy Code:
# def calculate_final_bill(subtotal):
#     discount = 0.10
#     tax = 0.05
#     final_total = subtotal - subtotal * discount + subtotal * tax
#     return round(final_total, 3)

# ✅ Fixed Code (Apply discount first, then calculate 5% tax on the discounted price):
def calculate_final_bill(subtotal):
    discount = 0.10
    tax = 0.05
    discounted_price = subtotal - (subtotal * discount)
    final_total = discounted_price + (discounted_price * tax)
    return round(final_total, 3)


# ------------------------------------------------------------------------------
# Challenge 2: Check Item Availability (Dictionary Key / Membership Bug)
# ------------------------------------------------------------------------------
flower_stock = {
    "FLW-01": {"name": "Red Rose", "qty": 40, "price": 1.500},
    "FLW-02": {"name": "White Lily", "qty": 25, "price": 2.250}
}

# ❌ Buggy Code:
# def check_item(code):
#     if code in flower_stock.values():
#         return "Available"
#     return "Not Found"

# ✅ Fixed Code (Search in dictionary keys directly, not `.values()`):
def check_item(code):
    if code in flower_stock:
        return "Available"
    return "Not Found"


# ------------------------------------------------------------------------------
# Challenge 3: Cart Total Accumulator (Variable Reset Inside Loop)
# ------------------------------------------------------------------------------
cart = [
    {"item": "Red Rose", "qty": 5, "price": 1.500},
    {"item": "Gift Wrap", "qty": 1, "price": 0.750},
    {"item": "Vase", "qty": 1, "price": 4.000}
]

# ❌ Buggy Code:
# def get_cart_total(cart_items):
#     for entry in cart_items:
#         total = 0
#         total += entry["qty"] * entry["price"]
#     return total

# ✅ Fixed Code (Initialize `total = 0` outside the loop so it accumulates):
def get_cart_total(cart_items):
    total = 0
    for entry in cart_items:
        total += entry["qty"] * entry["price"]
    return total


# ------------------------------------------------------------------------------
# Challenge 4: Stock Deduction Guard (Boundary Condition Bug)
# ------------------------------------------------------------------------------
# ❌ Buggy Code:
# def sell_flower(current_stock, order_qty):
#     if order_qty < current_stock:
#         current_stock -= order_qty
#         return f"Sold! Remaining: {current_stock}"
#     else:
#         return "Insufficient stock!"

# ✅ Fixed Code (Use `<=` to allow selling when order quantity equals available stock):
def sell_flower(current_stock, order_qty):
    if order_qty <= current_stock:
        current_stock -= order_qty
        return f"Sold! Remaining: {current_stock}"
    else:
        return "Insufficient stock!"


# ------------------------------------------------------------------------------
# Challenge 5: Find Most Expensive Item (Comparison Operator Bug)
# ------------------------------------------------------------------------------
materials = {
    "MAT-1": {"name": "Valve", "price": 45.0},
    "MAT-2": {"name": "Filter", "price": 12.5},
    "MAT-3": {"name": "Pump", "price": 120.0}
}

# ❌ Buggy Code:
# def find_priciest(inv):
#     max_price = 0
#     priciest_name = ""
#     for code, details in inv.items():
#         if details["price"] < max_price:
#             max_price = details["price"]
#             priciest_name = details["name"]
#     return priciest_name, max_price

# ✅ Fixed Code (Use `>` instead of `<` to track the highest price):
def find_priciest(inv):
    max_price = 0
    priciest_name = ""
    for code, details in inv.items():
        if details["price"] > max_price:
            max_price = details["price"]
            priciest_name = details["name"]
    return priciest_name, max_price


# ------------------------------------------------------------------------------
# Challenge 6: Case-Insensitive Search (String Method Bug)
# ------------------------------------------------------------------------------
suppliers = ["Al-Ghanim Trading", "Kuwait Oil Supply", "Gulf Industrial"]

# ❌ Buggy Code:
# def search_supplier(query):
#     results = []
#     for sup in suppliers:
#         if query.lower() in sup:
#             results.append(sup)
#     return results

# ✅ Fixed Code (Convert both sides to `.lower()` during comparison):
def search_supplier(query):
    results = []
    for sup in suppliers:
        if query.lower() in sup.lower():
            results.append(sup)
    return results


# ------------------------------------------------------------------------------
# Challenge 7: Bulk Reorder Status Updater (Dictionary Iteration Bug)
# ------------------------------------------------------------------------------
warehouse = {
    "A1": {"stock": 5, "min": 10},
    "A2": {"stock": 20, "min": 10}
}

# ❌ Buggy Code:
# def tag_inventory_status(data):
#     for item in data:
#         if item["stock"] <= item["min"]:
#             item["status"] = "LOW"
#         else:
#             item["status"] = "OK"
#     return data

# ✅ Fixed Code (Loop over `data.values()` to access each item's dictionary):
def tag_inventory_status(data):
    for item in data.values():
        if item["stock"] <= item["min"]:
            item["status"] = "LOW"
        else:
            item["status"] = "OK"
    return data


# ------------------------------------------------------------------------------
# Challenge 8: Receipt Number Generator (String & Integer Type Bug)
# ------------------------------------------------------------------------------
# ❌ Buggy Code:
# def generate_invoice_id(last_number):
#     next_num = last_number + 1
#     return "INV-" + next_num.zfill(5)

# ✅ Fixed Code (Cast `next_num` to `str` before calling `.zfill(5)`):
def generate_invoice_id(last_number):
    next_num = last_number + 1
    s = str(next_num)
    return "INV-" + s.zfill(5)


# ------------------------------------------------------------------------------
# Challenge 9: Average Lead Time Calculator (ZeroDivisionError Guard)
# ------------------------------------------------------------------------------
# ❌ Buggy Code:
# def average_lead_time(days_list):
#     total_days = sum(days_list)
#     avg = total_days / len(days_list)
#     if not days_list:
#         return 0.0
#     return round(avg, 1)

# ✅ Fixed Code (Check if list is empty BEFORE dividing):
def average_lead_time(days_list):
    if not days_list:
        return 0.0
    total_days = sum(days_list)
    avg = total_days / len(days_list)
    return round(avg, 1)


# ------------------------------------------------------------------------------
# Challenge 10: Safe Price Input Parser (Exception Type Bug)
# ------------------------------------------------------------------------------
# ❌ Buggy Code:
# def parse_unit_price(raw_input):
#     try:
#         price = float(raw_input)
#         if price <= 0:
#             return None
#         return price
#     except KeyError:
#         return None

# ✅ Fixed Code (Catch `ValueError` instead of `KeyError` on invalid float conversion):
def parse_unit_price(raw_input):
    try:
        price = float(raw_input)
        if price <= 0:
            return None
        return price
    except ValueError:
        return None


# ------------------------------------------------------------------------------
# Challenge 11: Daily Sales Filter by Payment Method (Logical Operator Bug)
# ------------------------------------------------------------------------------
invoices = [
    {"id": 1, "method": "KNET", "amount": 15.0},
    {"id": 2, "method": "CASH", "amount": 8.5},
    {"id": 3, "method": "LINK", "amount": 22.0}
]

# ❌ Buggy Code:
# def filter_instant_payments(tx_list):
#     valid = []
#     for tx in tx_list:
#         if tx["method"] == "KNET" and tx["method"] == "CASH":
#             valid.append(tx)
#     return valid

# ✅ Fixed Code (Use `or` so either KNET or CASH transactions are matched):
def filter_instant_payments(tx_list):
    valid = []
    for tx in tx_list:
        if tx["method"] == "KNET" or tx["method"] == "CASH":
            valid.append(tx)
    return valid


# ------------------------------------------------------------------------------
# Challenge 12: JSON Loader Default Structure (Data Type Mismatch Bug)
# ------------------------------------------------------------------------------
# ❌ Buggy Code:
# def load_pos_data(filename="non_existent_pos.json"):
#     try:
#         with open(filename, "r", encoding="utf-8") as f:
#             return json.load(f)
#     except FileNotFoundError:
#         return []

# ✅ Fixed Code (Return the expected dictionary schema on first run):
def load_pos_data(filename="non_existent_pos.json"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"products": {}, "sales": []}