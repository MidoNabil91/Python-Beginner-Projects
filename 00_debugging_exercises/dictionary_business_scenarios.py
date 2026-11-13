# ==================================================
# Dictionary Business Scenarios
# Author: Mohamed Nabil
# Description:
# Practical Dictionary Exercises Inspired by
# Procurement, Logistics, Fleet Management,
# Inventory Control, and Supplier Evaluation.
# ==================================================


# ==================================================
# Scenario 1 - Approved Suppliers Count
# ==================================================

suppliers = {
    "ABC": {"score": 88, "approved": True},
    "XYZ": {"score": 95, "approved": False},
    "MNO": {"score": 92, "approved": True}
}

count = 0

for supplier, info in suppliers.items():
    if info["approved"] == True:
        count += 1

print(f"Approved Suppliers : {count}")


# ==================================================
# Scenario 2 - Low Stock Report
# ==================================================

inventory = {
    "Valve": 50,
    "Pump": 5,
    "Bearing": 70,
    "Gasket": 2
}

low_stock = []

for item, qty in inventory.items():
    if qty < 10:
        low_stock.append(item)

print(low_stock)


# ==================================================
# Scenario 3 - Maintenance Vehicles Report
# ==================================================

fleet = {
    101: {"driver": "Ahmed", "km": 50000},
    102: {"driver": "Salem", "km": 120000},
    103: {"driver": "Khaled", "km": 85000},
    104: {"driver": "Ali", "km": 150000}
}

for fleet_id, info in fleet.items():
    if info["km"] > 100000:
        print(f"Vehicle {fleet_id} requires maintenance.")


# ==================================================
# Scenario 4 - Average RFQ Price
# ==================================================

quotes = {
    "Q-101": {"vendor": "ABC", "price": 1200},
    "Q-102": {"vendor": "XYZ", "price": 950},
    "Q-103": {"vendor": "MNO", "price": 1100}
}

total_quotes = 0

for quote_id, info in quotes.items():
    total_quotes += info["price"]

average_price = total_quotes / len(quotes)

print(f"Average RFQ Price = {average_price}")


# ==================================================
# Scenario 5 - Reorder Control
# ==================================================

inventory = {
    "Valve": {"stock": 50, "min_stock": 20},
    "Pump": {"stock": 8, "min_stock": 10},
    "Bearing": {"stock": 70, "min_stock": 30},
    "Gasket": {"stock": 2, "min_stock": 5}
}

for item, info in inventory.items():

    if info["stock"] < info["min_stock"]:
        print(
            f"⚠️ {item} needs reorder "
            f"(Stock: {info['stock']})"
        )


# ==================================================
# Scenario 6 - Fuel Monitoring
# ==================================================

fleet = {
    101: {"driver": "Ahmed", "fuel": 60},
    102: {"driver": "Salem", "fuel": 15},
    103: {"driver": "Khaled", "fuel": 40},
    104: {"driver": "Ali", "fuel": 10}
}

count = 0

for truck_id, info in fleet.items():

    if info["fuel"] < 20:

        print(
            f"Truck {truck_id} "
            f"requires refueling."
        )

        count += 1

print(f"Total Trucks Needing Fuel = {count}")


# ==================================================
# Scenario 7 - Approved Supplier List
# ==================================================

suppliers = {
    "ABC": {"score": 88, "approved": True},
    "XYZ": {"score": 95, "approved": False},
    "MNO": {"score": 92, "approved": True},
    "KGL": {"score": 97, "approved": True}
}

approved_suppliers = []

for supplier, info in suppliers.items():

    if info["approved"] == True:
        approved_suppliers.append(supplier)

print(approved_suppliers)


# ==================================================
# Scenario 8 - Total RFQ Value
# ==================================================

quotes = {
    "Q-101": {"vendor": "ABC", "price": 1200},
    "Q-102": {"vendor": "XYZ", "price": 950},
    "Q-103": {"vendor": "MNO", "price": 1100}
}

total_value = 0

for quote_id, info in quotes.items():
    total_value += info["price"]

print(f"Total RFQ Value = {total_value}")


# ==================================================
# Scenario 9 - Cheapest Approved Vendor
# ==================================================

vendors = {
    "ABC": {"price": 1000, "approved": True},
    "XYZ": {"price": 900, "approved": False},
    "MNO": {"price": 1200, "approved": True},
    "KGL": {"price": 950, "approved": True}
}

lowest_price = 1000000
lowest_vendor = ""

for vendor, info in vendors.items():

    if (
        info["approved"] == True
        and info["price"] < lowest_price
    ):

        lowest_price = info["price"]
        lowest_vendor = vendor

print(
    f"Cheapest Approved Vendor: "
    f"{lowest_vendor} ({lowest_price})"
)


# ==================================================
# Scenario 10 - Contract Status Report
# ==================================================

contracts = {
    "C-101": {"status": "Active"},
    "C-102": {"status": "Expired"},
    "C-103": {"status": "Active"},
    "C-104": {"status": "Expired"},
    "C-105": {"status": "Active"}
}

active_count = 0
expired_count = 0

for contract in contracts.values():

    if contract["status"] == "Active":
        active_count += 1

    elif contract["status"] == "Expired":
        expired_count += 1

print(f"Active Contracts = {active_count}")
print(f"Expired Contracts = {expired_count}")


# ==================================================
# Boss Fight 1 - Best Approved Supplier
# ==================================================

suppliers = {
    "ABC": {"score": 88, "approved": True},
    "XYZ": {"score": 95, "approved": False},
    "MNO": {"score": 92, "approved": True},
    "KGL": {"score": 97, "approved": True}
}

best_supplier = ""
best_score = 0

for supplier, info in suppliers.items():

    if (
        info["approved"] == True
        and info["score"] > best_score
    ):

        best_score = info["score"]
        best_supplier = supplier

print("=" * 40)
print(f"Best Approved Supplier = {best_supplier}")
print(f"Score = {best_score}")
print("=" * 40)


# ==================================================
# Boss Fight 2 - Salary Analysis
# ==================================================

employees = {
    1: {"name": "Ahmed", "salary": 500},
    2: {"name": "Salem", "salary": 700},
    3: {"name": "Ali", "salary": 600},
    4: {"name": "Khaled", "salary": 900},
    5: {"name": "Omar", "salary": 450}
}

highest_salary = 0
highest_employee = ""

lowest_salary = 100000
lowest_employee = ""

total_salary = 0

for employee_id, info in employees.items():

    total_salary += info["salary"]

    if info["salary"] > highest_salary:
        highest_salary = info["salary"]
        highest_employee = info["name"]

    if info["salary"] < lowest_salary:
        lowest_salary = info["salary"]
        lowest_employee = info["name"]

average_salary = total_salary / len(employees)

print("=" * 40)
print(f"Highest Salary = {highest_salary}")
print(f"Employee = {highest_employee}")
print("=" * 40)
print(f"Lowest Salary = {lowest_salary}")
print(f"Employee = {lowest_employee}")
print("=" * 40)
print(f"Average Salary = {average_salary}")
print("=" * 40)


# ==================================================
# RFQ Evaluation Challenge
# ==================================================

vendors = {
    "ABC": {"price": 1200, "delivery": 5, "approved": True},
    "XYZ": {"price": 900, "delivery": 15, "approved": True},
    "MNO": {"price": 1100, "delivery": 4, "approved": False},
    "KGL": {"price": 1000, "delivery": 6, "approved": True},
    "SSC": {"price": 1050, "delivery": 3, "approved": True}
}

lowest_price = 100000
best_vendor = ""
delivery_days = 0

for vendor, info in vendors.items():

    if (
        info["approved"] == True
        and info["delivery"] <= 7
        and info["price"] < lowest_price
    ):

        lowest_price = info["price"]
        best_vendor = vendor
        delivery_days = info["delivery"]

print("=" * 40)
print("RFQ EVALUATION RESULT")
print("=" * 40)
print(f"Best Vendor : {best_vendor}")
print(f"Price       : {lowest_price}")
print(f"Delivery    : {delivery_days} Days")
print("=" * 40)