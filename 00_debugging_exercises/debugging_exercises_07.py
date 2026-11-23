# ==============================================================================
# Debugging Exercises - Set 09: Practical Business Logic (10 Scenarios)
# Author: Mohamed Nabil (@MidoNabil91)
# Description: Real-world business debugging scenarios featuring the original
#              buggy code, root-cause explanation, and the corrected solution.
# ==============================================================================


# ------------------------------------------------------------------------------
# 1. Invoice Discount Calculation (Condition Ordering)
# ------------------------------------------------------------------------------
# BUGGY CODE:
# def apply_discount(total):
#     if total > 100:       # Catches 600 first and exits before checking > 500!
#         return total * 0.95
#     elif total > 500:
#         return total * 0.85
#     return total

# FIXED CODE:
def apply_discount(total):
    if total > 500:
        return total * 0.85
    elif total > 100:
        return total * 0.95
    return total


# ------------------------------------------------------------------------------
# 2. Inventory Stock Update (Input Type Casting)
# ------------------------------------------------------------------------------
# BUGGY CODE:
# def update_stock(current_stock, received_input):
#     return current_stock + received_input  # TypeError: int + str

# FIXED CODE:
def update_stock(current_stock, received_input):
    received_qty = int(received_input)
    return current_stock + received_qty


# ------------------------------------------------------------------------------
# 3. Order Cart Total (Accumulator Initialization Outside Loop)
# ------------------------------------------------------------------------------
# BUGGY CODE:
# for order in orders:
#     grand_total = 0  # Resets to 0 on every iteration!
#     grand_total += order["qty"] * order["price"]

# FIXED CODE:
def calculate_cart_total(orders):
    grand_total = 0
    for order in orders:
        grand_total += order["qty"] * order["price"]
    return grand_total


# ------------------------------------------------------------------------------
# 4. Inventory Item Search (String Normalization)
# ------------------------------------------------------------------------------
# BUGGY CODE:
# search_code = input("Enter item code: ")  # Fails on " flw-101 "
# if search_code in inventory_codes: ...

# FIXED CODE:
def find_item_code(codes_list, raw_search):
    clean_code = raw_search.strip().upper()
    return clean_code in codes_list


# ------------------------------------------------------------------------------
# 5. Supplier Average Price (Empty List Division Guard)
# ------------------------------------------------------------------------------
# BUGGY CODE:
# def calculate_average_price(prices):
#     return sum(prices) / len(prices)  # ZeroDivisionError when prices = []

# FIXED CODE:
def calculate_average_price(prices):
    if not prices:
        return "Nothing To Calculate!"
    return sum(prices) / len(prices)


# ------------------------------------------------------------------------------
# 6. Dictionary Safe Lookup (Missing Key Handling)
# ------------------------------------------------------------------------------
# BUGGY CODE:
# prices = {"Rose": 2.5, "Tulip": 3.0}
# print(prices["Lily"])  # Raises KeyError

# FIXED CODE:
def get_item_price(prices_dict, item_name):
    return prices_dict.get(item_name, 0)


# ------------------------------------------------------------------------------
# 7. Removing Out-of-Stock Items (Mutating List While Iterating)
# ------------------------------------------------------------------------------
# BUGGY CODE:
# for qty in stock:
#     if qty == 0:
#         stock.remove(qty)  # Skips consecutive zeros due to index shifting

# FIXED CODE:
def remove_zero_stock(stock_list):
    return [qty for qty in stock_list if qty != 0]


# ------------------------------------------------------------------------------
# 8. Invoice Tax & Shipping Total (Operator Precedence)
# ------------------------------------------------------------------------------
# BUGGY CODE:
# total = price + shipping * tax_rate  # Multiplies shipping by tax_rate first!

# FIXED CODE:
def calculate_final_invoice(price, shipping, tax_rate=0.15):
    tax_amount = price * tax_rate
    return price + tax_amount + shipping


# ------------------------------------------------------------------------------
# 9. Creating New Invoice List (Mutable Default Argument Trap)
# ------------------------------------------------------------------------------
# BUGGY CODE:
# def add_item(item, invoice=[]):  # Shares the same list across function calls!
#     invoice.append(item)
#     return invoice

# FIXED CODE:
def add_item(item, invoice=None):
    if invoice is None:
        invoice = []
    invoice.append(item)
    return invoice


# ------------------------------------------------------------------------------
# 10. Phone Number Validation (Logical AND vs OR)
# ------------------------------------------------------------------------------
# BUGGY CODE:
# if len(phone) == 8 or phone.isdigit():  # Passes even if length != 8!

# FIXED CODE:
def is_valid_kuwait_phone(phone):
    return len(phone) == 8 and phone.isdigit()
