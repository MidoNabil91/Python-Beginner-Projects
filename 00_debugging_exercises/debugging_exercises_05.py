# ==============================================================================
# Debugging & Code Review Practice — Set 7 (Warehouse & JSON Persistence)
# Description: 8 practical debugging challenges focused on inventory stock
#              validation, nested dictionary iteration, accumulator scope,
#              case-insensitive search, safe .get() lookups, and JSON handling.
# Developer: Mohamed Nabil
# ==============================================================================
import json


# ------------------------------------------------------------------------------
# Challenge 1: Stock Issue Logic (Comparison Operator Bug)
# Bug: Used '>' instead of '<', rejecting valid stock issues and allowing negatives.
# ------------------------------------------------------------------------------
def issue_material(inventory, mat_code, qty):
    if mat_code not in inventory:
        return "Material not found"

    if inventory[mat_code]["stock"] < qty:
        print("Insufficient stock!")
        return False

    inventory[mat_code]["stock"] -= qty
    return True


# ------------------------------------------------------------------------------
# Challenge 2: Reorder Alert Report (Nested Dictionary Iteration)
# Bug: Iterated over dictionary keys only instead of using .items() to access values.
# ------------------------------------------------------------------------------
def get_reorder_items(data):
    alerts = []
    for item, info in data.items():
        if info["stock"] <= info["min_stock"]:
            alerts.append(item)
    return alerts


# ------------------------------------------------------------------------------
# Challenge 3: Total Warehouse Valuation (Accumulator Scope Bug)
# Bug: 'total = 0' was initialized inside the loop, resetting on every iteration.
# ------------------------------------------------------------------------------
def calculate_total_value(inventory):
    total = 0
    for code, info in inventory.items():
        item_total = info["stock"] * info["price"]
        total += item_total
    return total


# ------------------------------------------------------------------------------
# Challenge 4: JSON File Persistence (File Open Mode & Parameter Matching)
# Bug: Opened file in read mode ("r") instead of write mode ("w") for json.dump().
# ------------------------------------------------------------------------------
def save_warehouse(data):
    with open("warehouse.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


# ------------------------------------------------------------------------------
# Challenge 5: Stock Receiving Validation (Boundary & Operator Bugs)
# Bug: Used 'qty < 0' (allowing 0) and '=+' instead of '+=' (overwriting stock).
# ------------------------------------------------------------------------------
def receive_material(inventory, mat_code, qty):
    if mat_code not in inventory:
        return "Material not found"

    if qty <= 0:
        print("Quantity must be greater than zero!")
        return False

    inventory[mat_code]["stock"] += qty
    return True


# ------------------------------------------------------------------------------
# Challenge 6: Case-Insensitive Material Search
# Bug: Normalized keyword to lowercase without normalizing item["name"].
# ------------------------------------------------------------------------------
def search_material(inventory, keyword):
    results = []
    keyword = keyword.strip().lower()
    for code, info in inventory.items():
        if keyword in info["name"].lower():
            results.append(code)
    return results


# ------------------------------------------------------------------------------
# Challenge 7: Safe JSON Loading on First Run
# Bug: Returned undefined variable 'data' in except block instead of empty dict {}.
# ------------------------------------------------------------------------------
def load_warehouse():
    try:
        with open("warehouse.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Starting with empty warehouse...")
        return {}


# ------------------------------------------------------------------------------
# Challenge 8: Category Filter with Safe Dictionary Lookup
# Bug: Direct key access info["category"] caused KeyError when key was missing.
# ------------------------------------------------------------------------------
def filter_by_category(inventory, target_category):
    matched = {}
    for code, info in inventory.items():
        if info.get("category", "").lower() == target_category.lower():
            matched[code] = info
    return matched


if __name__ == "__main__":
    sample_warehouse = {
        "MAT-101": {"name": "Safety Helmet", "category": "PPE", "stock": 10, "min_stock": 15, "price": 3.5},
        "MAT-102": {"name": "Welding Gloves", "category": "PPE", "stock": 50, "min_stock": 20, "price": 2.0},
        "MAT-103": {"name": "Safety Shoes", "stock": 5, "min_stock": 5, "price": 12.0},
    }

    print("Reorder Alerts:", get_reorder_items(sample_warehouse))
    print(f"Total Valuation: {calculate_total_value(sample_warehouse):.3f} KWD")
    print("Search 'safety':", search_material(sample_warehouse, "safety"))
    print("PPE Items:", list(filter_by_category(sample_warehouse, "ppe").keys()))