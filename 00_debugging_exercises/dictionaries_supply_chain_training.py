"""
Python Dictionaries Training: Supply Chain, Procurement & Inventory Management
Description: Practical exercises progressing from basic dictionary CRUD operations
to nested dictionary iteration, conditional updates, min/max comparisons, and data filtering.
"""

# ==============================================================================
# 1. Basic CRUD: Modifying & Adding Keys
# ==============================================================================
print("--- 1. Basic CRUD Operations ---")
part = {
    "code": "HYV-204",
    "name": "Hydraulic Filter",
    "stock": 12
}

part["stock"] = 15          # Update existing key
part["location"] = "Ahmadi" # Add new key
print("Updated Part:", part)


# ==============================================================================
# 2. Safe Retrieval with .get() & Deletion with del
# ==============================================================================
print("\n--- 2. Safe Retrieval & Deletion ---")
print("Price Check:", part.get("price", "Not Priced"))
del part["location"]
print("After Deleting Location:", part)


# ==============================================================================
# 3. Looping through a Dictionary with .items()
# ==============================================================================
print("\n--- 3. Warehouse Stock Report ---")
warehouse = {
    "Ahmadi": 50,
    "Shuwaikh": 120,
    "Shuaiba": 30
}

for branch, stock in warehouse.items():
    print(f"{branch} has {stock} items")


# ==============================================================================
# 4. Conditional Filtering & Updating inside a Loop
# ==============================================================================
print("\n--- 4. Low Stock Alerts & Auto-Replenishment ---")
for branch, stock in warehouse.items():
    if stock < 60:
        print(f"⚠️ Reorder needed in {branch} (Current: {stock})")
        warehouse[branch] += 50  # Replenish stock by 50 units

print("Replenished Warehouse:", warehouse)


# ==============================================================================
# 5. Nested Dictionaries: Conditional Stock Update
# ==============================================================================
print("\n--- 5. Nested Warehouse Threshold Check ---")
nested_warehouse = {
    "Ahmadi": {"stock": 50, "min_limit": 60},
    "Shuwaikh": {"stock": 120, "min_limit": 100},
    "Shuaiba": {"stock": 30, "min_limit": 40}
}

for branch, info in nested_warehouse.items():
    if info["stock"] < info["min_limit"]:
        info["stock"] += 50

print("Updated Nested Warehouse:", nested_warehouse)


# ==============================================================================
# 6. Aggregation (Accumulator Pattern): Fleet Maintenance Costs
# ==============================================================================
print("\n--- 6. Fleet Maintenance Cost Report ---")
cars_service = {
    "CAR-1": {"model": "Toyota Hilux", "parts_cost": 80, "labor_cost": 20},
    "CAR-2": {"model": "Nissan Patrol", "parts_cost": 150, "labor_cost": 50},
    "CAR-3": {"model": "Ford F-150", "parts_cost": 120, "labor_cost": 30}
}

total_fleet_cost = 0

for car, info in cars_service.items():
    total_car = info["parts_cost"] + info["labor_cost"]
    total_fleet_cost += total_car
    print(f"{info['model']}: {total_car} KD")

print(f"Total Fleet Cost: {total_fleet_cost} KD")


# ==============================================================================
# 7. Import Shipments Valuation & High-Value Alerts
# ==============================================================================
print("\n--- 7. Import Shipments & Customs Valuation ---")
shipments = {
    "SHP-101": {"supplier": "Siemens", "goods_value": 2000, "customs_fee": 150},
    "SHP-102": {"supplier": "Hyva", "goods_value": 800, "customs_fee": 60},
    "SHP-103": {"supplier": "Eaton", "goods_value": 1500, "customs_fee": 120}
}

total_import_cost = 0

for code, info in shipments.items():
    ship_per_one = info["goods_value"] + info["customs_fee"]
    total_import_cost += ship_per_one
    print(f"{info['supplier']}: {ship_per_one} KD")
    if ship_per_one >= 1500:
        print("⚠️ High Value Shipment - Needs Manager Approval")

print(f"Total Import Cost = {total_import_cost} KD")


# ==============================================================================
# 8. Vendor Quotes Discounting & Savings Calculation
# ==============================================================================
print("\n--- 8. Vendor Quotes Discount & Delivery Analysis ---")
quotes = {
    "Q-10": {"vendor": "Al-Ghanim", "price": 1000, "delivery_days": 5},
    "Q-20": {"vendor": "KGL", "price": 1200, "delivery_days": 2},
    "Q-30": {"vendor": "Agility", "price": 800, "delivery_days": 10}
}

total_after_discount = 0
total_before = 0

for quote, info in quotes.items():
    total_before += info["price"]
    info["price"] = info["price"] * 0.9
    total_after_discount += info["price"]
    print(f"{info['vendor']} : {info['price']} KWD")
    if info["delivery_days"] <= 5:
        print("⚡ Fast Delivery")
    else:
        print("Normal Delivery")

print("=" * 50)
print(f"Total After Discount = {total_after_discount} KWD")
print(f"Savings (Before vs After) = {total_before - total_after_discount} KWD")
print("=" * 50)


# ==============================================================================
# 9. Finding Max/Min: Highest Rated Vendor
# ==============================================================================
print("\n--- 9. Top Rated Vendor Selection ---")
vendors_rating = {
    "V-1": {"name": "Al-Ghanim", "score": 88},
    "V-2": {"name": "KGL", "score": 95},
    "V-3": {"name": "Agility", "score": 82}
}

highest_score = 0
best_vendor = ""

for qot, info in vendors_rating.items():
    if info["score"] > highest_score:
        highest_score = info["score"]
        best_vendor = info["name"]

print(f"🏆 Winner: {best_vendor} with Score {highest_score}")


# ==============================================================================
# 10. Conditional Min/Max: Best Quote within Delivery SLA & Certified Contractors
# ==============================================================================
print("\n--- 10. Conditional Bid & Contractor Selection ---")
quotes_sla = {
    "Q-10": {"vendor": "Al-Ghanim", "price": 900.0, "delivery_days": 5},
    "Q-20": {"vendor": "KGL", "price": 1080.0, "delivery_days": 2},
    "Q-30": {"vendor": "Agility", "price": 720.0, "delivery_days": 10},
    "Q-40": {"vendor": "Boodai", "price": 850.0, "delivery_days": 4}
}

lowest_price = 999999
best_sla_vendor = ""
best_days = 0

for qot, info in quotes_sla.items():
    if info["delivery_days"] <= 5 and info["price"] < lowest_price:
        lowest_price = info["price"]
        best_sla_vendor = info["vendor"]
        best_days = info["delivery_days"]

print(f"🏆 SLA Winner: {best_sla_vendor} ({best_days} days) at {lowest_price} KWD")

contractors = {
    "C-1": {"name": "Al-Mulla", "score": 95, "certified": False},
    "C-2": {"name": "Kharafi", "score": 88, "certified": True},
    "C-3": {"name": "Galfar", "score": 92, "certified": True},
    "C-4": {"name": "NBTC", "score": 80, "certified": False}
}

highest_cert_score = 0
best_comp = ""

for qout, info in contractors.items():
    if info["score"] > highest_cert_score and info["certified"] == True:
        highest_cert_score = info["score"]
        best_comp = info["name"]

print(f"🏆 Best Certified Contractor: {best_comp} (Score: {highest_cert_score})")


# ==============================================================================
# 11. Filtering Data into a List: Uncertified Contractors
# ==============================================================================
print("\n--- 11. Compliance Follow-up List ---")
un_certified = []

for con, info in contractors.items():
    if info["certified"] == False:
        un_certified.append(info["name"])

print("Contractors Needing Renewal:", un_certified)
print(f"Total to renew: {len(un_certified)}")