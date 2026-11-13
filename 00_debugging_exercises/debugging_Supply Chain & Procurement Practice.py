"""
Python Debugging Challenges - Supply Chain & Procurement Practice
Author: Mohammad Nabeel
Focus: Dictionaries, Loops, Conditionals, Accumulators, and Error Handling (.get)
"""

# ==============================================================================
# Challenge 1: Total Inventory Valuation
# Fixed: Added .items() to loop and used += accumulator instead of overwriting.
# ==============================================================================
stock_1 = {"Hydraulic Filter": 10, "Bussmann Fuse": 20, "Fuel Pump": 2}
prices_1 = {"Hydraulic Filter": 12, "Bussmann Fuse": 3, "Fuel Pump": 45}

total_value = 0
for item, qty in stock_1.items():
    total_value += qty * prices_1[item]

print(f"1. Total Inventory Value: {total_value} KWD")


# ==============================================================================
# Challenge 2: Low Stock Alert Report (< 10 units)
# Fixed: Changed <= to <, appended item name instead of qty, used len() for count.
# ==============================================================================
stock_2 = {
    "Hydraulic Filter": 15,
    "Bussmann Fuse": 4,
    "Fuel Pump": 2,
    "Oil Seal": 10,
    "Spark Plug": 8
}

low_items = []
for item, qty in stock_2.items():
    if qty < 10:
        low_items.append(item)

print(f"2. Low Stock Items: {low_items} | Count: {len(low_items)}")


# ==============================================================================
# Challenge 3: Updating Stock from Incoming Shipment
# Fixed: Used .items() in loop, checked membership directly in dict keys, used +=.
# ==============================================================================
current_stock = {"Hydraulic Filter": 10, "Bussmann Fuse": 25}
received_shipment = {"Hydraulic Filter": 5, "Oil Seal": 12}

for item, new_qty in received_shipment.items():
    if item in current_stock:
        current_stock[item] += new_qty
    else:
        current_stock[item] = new_qty

print(f"3. Updated Stock: {current_stock}")


# ==============================================================================
# Challenge 4: Applying 10% Vendor Discount on Items > 20 KWD
# Fixed: Changed < to >, fixed variable case sensitivity (Prices -> price).
# ==============================================================================
prices_4 = {"Hydraulic Filter": 25, "Bussmann Fuse": 5, "Fuel Pump": 50, "Oil Seal": 10}
final_bill = 0

for item, price in prices_4.items():
    if price > 20:
        final_bill += price * 0.90
    else:
        final_bill += price

print(f"4. Final Bill After Discount: {final_bill} KWD")


# ==============================================================================
# Challenge 5: Finding the Cheapest Spare Part
# Fixed: Initialized cheapest_price with float('inf') instead of 0.
# ==============================================================================
prices_5 = {"Hydraulic Filter": 25, "Bussmann Fuse": 5, "Fuel Pump": 50, "Oil Seal": 10}
cheapest_price = float("inf")
cheapest_item = ""

for item, price in prices_5.items():
    if price < cheapest_price:
        cheapest_price = price
        cheapest_item = item

print(f"5. Cheapest Item: {cheapest_item} ({cheapest_price} KWD)")


# ==============================================================================
# Challenge 6: Inventory Valuation with Missing Price Protection (.get)
# Fixed: Replaced prices[item] with prices.get(item, 0) to avoid KeyError, used +=.
# ==============================================================================
stock_6 = {"Hydraulic Filter": 10, "Bussmann Fuse": 20, "New Gasket": 5, "Oil Seal": 4}
prices_6 = {"Hydraulic Filter": 12, "Bussmann Fuse": 3, "Oil Seal": 8}

total_val_6 = 0
for item, qty in stock_6.items():
    price = prices_6.get(item, 0)
    if price == 0:
        print(f"   ⚠️ Missing price for: {item}")
    total_val_6 += qty * price

print(f"6. Safe Inventory Value: {total_val_6} KWD")


# ==============================================================================
# Challenge 7: Counting Deliveries per Vendor (COUNTIF Logic)
# Fixed: Swapped if/else logic (increment += 1 if exists, initialize = 1 if new).
# ==============================================================================
deliveries = ["KGL", "Al-Ghanim", "KGL", "Agility", "KGL", "Al-Ghanim"]
vendor_counts = {}

for vendor in deliveries:
    if vendor in vendor_counts:
        vendor_counts[vendor] += 1
    else:
        vendor_counts[vendor] = 1

print(f"7. Vendor Delivery Counts: {vendor_counts}")


# ==============================================================================
# Challenge 8: Grouping Expenses by Department (SUMIF Logic)
# Fixed: Swapped if/else logic (accumulate += amount if exists, set = amount if new).
# ==============================================================================
invoices = [
    ("Maintenance", 150),
    ("Operations", 300),
    ("Maintenance", 200),
    ("HSE", 100),
    ("Operations", 50)
]

dept_totals = {}
for dept, amount in invoices:
    if dept in dept_totals:
        dept_totals[dept] += amount
    else:
        dept_totals[dept] = amount

print(f"8. Department Totals: {dept_totals}")


# ==============================================================================
# Challenge 9: Reorder Point Alert Report
# Fixed: Changed () tuple to [] list, fixed dict typo, changed > to <=.
# ==============================================================================
stock_9 = {"Hydraulic Filter": 8, "Bussmann Fuse": 30, "Fuel Pump": 2, "Oil Seal": 15}
reorder_level = {"Hydraulic Filter": 10, "Bussmann Fuse": 20, "Fuel Pump": 5, "Oil Seal": 15}

items_to_order = []
for item, qty in stock_9.items():
    if qty <= reorder_level[item]:
        items_to_order.append(item)

print(f"9. Items to Reorder: {items_to_order}")


# ==============================================================================
# Challenge 10: Generating Purchase Order Quantities up to Max Stock
# Fixed: Initialized {} dict instead of [], added .items(), calculated target - qty.
# ==============================================================================
stock_10 = {"Hydraulic Filter": 8, "Bussmann Fuse": 30, "Fuel Pump": 2, "Oil Seal": 15}
max_stock = {"Hydraulic Filter": 20, "Bussmann Fuse": 30, "Fuel Pump": 10, "Oil Seal": 25}

purchase_order = {}
for item, qty in stock_10.items():
    target = max_stock[item]
    if qty < target:
        purchase_order[item] = target - qty

print(f"10. Final Purchase Order: {purchase_order}")
# ==============================================================================
## 🔍 Key Bugs Identified & Resolved
# | # | Scenario | Bugs Fixed |
# |---|---|---|
# | **01** | **Inventory Valuation** | Added missing `.items()` for dictionary unpacking; replaced `=` with `+=` accumulator. |
# | **02** | **Low Stock Alerts** | Changed `<=` to `<` for strict threshold; appended `item` name instead of `qty`; used `len()`. |
# | **03** | **Shipment Stock Update** | Checked key membership directly (`if item in dict`) instead of `.items()`; used `+=` to add stock. |
# | **04** | **Vendor Bulk Discount** | Reversed comparison (`<` to `>`) for items above 20 KWD; fixed `NameError` case sensitivity. |
# | **05** | **Cheapest Item Finder** | Replaced `0` initial value with `float('inf')` so price comparisons evaluate properly. |
# | **06** | **Safe Valuation (`.get`)** | Replaced direct indexing `prices[item]` with `prices.get(item, 0)` to prevent `KeyError`. |
# | **07** | **Vendor Delivery Count** | Fixed inverted `if/else` logic for `COUNTIF`-style dictionary frequency counting. |
# | **08** | **Department Spend (`SUMIF`)** | Fixed inverted `if/else` logic so existing department totals accumulate via `+=`. |
# | **09** | **Reorder Point Report** | Changed immutable tuple `()` to list `[]` to support `.append()`; fixed dict name typo and `<=` check. |
# | **10** | **Auto Purchase Order** | Changed `[]` to `{}` dictionary; fixed subtraction order (`target - qty`) for positive order quantities. |