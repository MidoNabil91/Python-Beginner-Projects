# """
# ==================================================
# Python Debugging & Logic Challenges - Set 2
# Author: Mohamed Nabil
# Description: Practice code reviews, error handling, default parameters, 
#              and vendor selection logic in Python.
# ==================================================
# """

# ================================================
# Challenge 1: Safety Stock Reorder Threshold
# Bug: Used '<' instead of '<=' which missed exact safety stock limits.
# ================================================
print("--- Challenge 1: Safety Stock Status ---")

# Fixed Code:
def check_reorder_status(current_stock, safety_stock):
    if current_stock <= safety_stock:  # Handle boundary condition
        return "Reorder Immediately"
    else:
        return "Stock Level Safe"

print("Reorder Status (20 vs 20):", check_reorder_status(20, 20), "\n")


# ================================================
# Challenge 2: Dynamic Budget Allocation (Scope & Returns)
# Bug: UnboundLocalError due to updating global variable inside local scope.
# ================================================
print("--- Challenge 2: Dynamic Budget Allocation ---")

remaining_budget = 50000

# Fixed Code (Pure Function approach):
def deduct_po_cost(current_budget, po_amount):
    return current_budget - po_amount

remaining_budget = deduct_po_cost(remaining_budget, 12000)
print(f"PO Processed. New Budget: ${remaining_budget}\n")


# ================================================
# Challenge 3: Vendor Selection Logic (Logical Operators)
# Bug: Used 'or' operator instead of 'and', allowing uncertified vendors.
# ================================================
print("--- Challenge 3: Vendor Eligibility ---")

# Fixed Code:
def is_vendor_eligible(is_certified, price, max_budget):
    if is_certified and price <= max_budget:  # Both conditions must be met
        return "Vendor Approved"
    else:
        return "Vendor Rejected"

print("Vendor Status:", is_vendor_eligible(False, 800, 1000), "\n")


# ================================================
# Challenge 4: Unit Price Conversion (Default Argument Order)
# Bug: SyntaxError caused by default parameter coming before positional parameters.
# ================================================
print("--- Challenge 4: Unit Price Calculation ---")

# Fixed Code:
def calculate_material_cost(unit_price, quantity, currency="USD"):
    total = unit_price * quantity
    return f"{total} {currency}"

print("Calculated Cost:", calculate_material_cost(150, 10), "\n")


# ================================================
# Challenge 5: Average RFQ Quote Calculator (ZeroDivisionError)
# Bug: Division by zero when passing an empty list of supplier quotes.
# ================================================
print("--- Challenge 5: Average RFQ Quote ---")

# Fixed Code:
def calculate_average_quote(quotes_list):
    if not quotes_list:  # Check if list is empty to prevent zero division
        return None
        
    total_sum = 0
    for quote in quotes_list:
        total_sum += quote
    
    return total_sum / len(quotes_list)

supplier_quotes = []
average = calculate_average_quote(supplier_quotes)

if average is None:
    print("No quotes available to calculate an average.")
else:
    print(f"Average Quote: ${average}")