"""
==================================================
Debugging & Code Review Exercises - Set 3
Author: Mohamed Nabil
Description: Practice challenges focusing on:
             - Logical operators (and vs or)
             - Variable Scope & NameError debugging
             - Defensive Programming against ZeroDivisionError
             - Boundary Condition Validation (<= vs >=)
==================================================
"""

# ==================================================
# Challenge 1: PO Discount Eligibility (Logical Operators)
# Bug: Used 'and' instead of 'or', requiring both conditions instead of either.
# ==================================================

def check_discount(po_amount, is_approved):
    # FIXED: Changed 'and' to 'or' so either a high PO value OR approved status qualifies for a discount
    if po_amount > 1000 or is_approved:
        return "✅ Eligible for Discount"
    else:
        return "❌ Standard Price"

# Test Case: Non-approved supplier with high PO amount (1500 KWD)
print("--- Challenge 1 Output ---")
print(check_discount(1500, False))


# ==================================================
# Challenge 2: Discounted Unit Price Calculation (NameError Fix)
# Bug: Variable misnamed 'discount' instead of 'discount_amount'.
# ==================================================

def calculate_discounted_price(unit_price, discount_percent):
    discount_amount = unit_price * discount_percent / 100
    # FIXED: Refactored 'discount' to 'discount_amount'
    final_price = unit_price - discount_amount
    return final_price

print("\n--- Challenge 2 Output ---")
print(f"Discounted Price: {calculate_discounted_price(50.0, 10):.3f} KWD")


# ==================================================
# Challenge 3: Average Shipping Cost (ZeroDivisionError Handling)
# Bug: Executing division by shipments_count when count is 0.
# ==================================================

total_shipping_cost = 250.0
shipments_count = 0

print("\n--- Challenge 3 Output ---")
# FIXED: Guard condition prevents division by zero
if shipments_count > 0:
    avg_cost = total_shipping_cost / shipments_count
    print(f"Average shipping cost: {avg_cost:.3f} KWD")
else:
    print("⚠️ Warning: Shipments count cannot be zero (No shipments recorded yet).")


# ==================================================
# Challenge 4: Warehouse Capacity Check (Operator Logic Error)
# Bug: Used '>=' instead of '<=', incorrectly allowing over-capacity stock additions.
# ==================================================

current_stock = 90
added_qty = 20
max_cap = 100

print("\n--- Challenge 4 Output ---")
# FIXED: Changed '>=' to '<=' to validate available warehouse space
if current_stock + added_qty <= max_cap:
    print("✅ Stock added successfully!")
    current_stock += added_qty
else:
    print(f"❌ Cannot add {added_qty} pcs! Exceeds warehouse max capacity ({max_cap} pcs).")