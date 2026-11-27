# ==============================================================================
# Debugging Exercises - Set 10: Object-Oriented Programming (OOP) (8 Challenges)
# Author: Mohamed Nabil (@MidoNabil91)
# Description: Practical OOP debugging challenges covering self binding,
#              instance vs class attributes, internal method calls, __repr__,
#              return vs print in methods, mutable default dictionaries,
#              encapsulation/validation guards, and JSON serialization.
# ==============================================================================
import json


# ------------------------------------------------------------------------------
# Challenge 1: Missing `self` in Method Definition (TypeError)
# ------------------------------------------------------------------------------
# ❌ Buggy Code:
# class PurchaseOrder:
#     def __init__(self, po_number, qty, unit_price):
#         self.po_number = po_number
#         self.qty = qty
#         self.unit_price = unit_price
#
#     def calculate_total():
#         return qty * unit_price

# ✅ Fixed Code (Pass `self` to access instance attributes):
class PurchaseOrder:
    def __init__(self, po_number, qty, unit_price):
        self.po_number = po_number
        self.qty = qty
        self.unit_price = unit_price

    def calculate_total(self):
        return self.qty * self.unit_price


# ------------------------------------------------------------------------------
# Challenge 2: Local Variable vs Instance Attribute in `__init__` (AttributeError)
# ------------------------------------------------------------------------------
# ❌ Buggy Code:
# class Supplier:
#     def __init__(self, name, category):
#         self.name = name
#         self.category = category
#         status = "Pending"  # Local variable lost after __init__ finishes!

# ✅ Fixed Code (Attach `status` to `self` so it persists on the instance):
class Supplier:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.status = "Pending"

    def approve_supplier(self):
        self.status = "Approved"
        return f"{self.name} is now {self.status}"


# ------------------------------------------------------------------------------
# Challenge 3: Calling Another Method Inside the Same Class (NameError)
# ------------------------------------------------------------------------------
# ❌ Buggy Code:
# class Shipment:
#     def __init__(self, goods_value, customs_rate=0.05):
#         self.goods_value = goods_value
#         self.customs_rate = customs_rate
#
#     def get_customs_fee(self):
#         return self.goods_value * self.customs_rate
#
#     def total_landed_cost(self):
#         fee = get_customs_fee()  # NameError: missing `self.`
#         return self.goods_value + fee

# ✅ Fixed Code (Call sibling methods using `self.method_name()`):
class Shipment:
    def __init__(self, goods_value, customs_rate=0.05):
        self.goods_value = goods_value
        self.customs_rate = customs_rate

    def get_customs_fee(self):
        return self.goods_value * self.customs_rate

    def total_landed_cost(self):
        fee = self.get_customs_fee()
        return self.goods_value + fee


# ------------------------------------------------------------------------------
# Challenge 4: Human-Readable Object Representation (`__repr__`)
# ------------------------------------------------------------------------------
# ❌ Buggy Code:
# class SparePart:
#     def __init__(self, name, stock):
#         self.name = name
#         self.stock = stock
# # Printing instance outputs memory address: <__main__.SparePart object at ...>

# ✅ Fixed Code (Implement `__repr__` for clear object formatting):
class SparePart:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

    def __repr__(self):
        return f"Part Name : {self.name!r} | stock = {self.stock!r}"


# ------------------------------------------------------------------------------
# Challenge 5: Printing Instead of Returning from a Method (TypeError)
# ------------------------------------------------------------------------------
# ❌ Buggy Code:
# class WarehouseItem:
#     def __init__(self, name, stock, price):
#         self.name = name
#         self.stock = stock
#         self.price = price
#
#     def issue_stock(self, qty):
#         if qty <= self.stock:
#             self.stock -= qty
#             print(self.stock)  # Returns None by default!

# ✅ Fixed Code (Return updated `self.stock` so callers can use the value):
class WarehouseItem:
    def __init__(self, name, stock, price):
        self.name = name
        self.stock = stock
        self.price = price

    def issue_stock(self, qty):
        if qty <= self.stock:
            self.stock -= qty
        return self.stock


# ------------------------------------------------------------------------------
# Challenge 6: Shared Mutable Class Dictionary Trap
# ------------------------------------------------------------------------------
# ❌ Buggy Code:
# class RFQ:
#     quotes = {}  # Shared across ALL RFQ instances!
#
#     def __init__(self, rfq_id):
#         self.rfq_id = rfq_id

# ✅ Fixed Code (Initialize `self.quotes = {}` inside `__init__` per instance):
class RFQ:
    def __init__(self, rfq_id):
        self.rfq_id = rfq_id
        self.quotes = {}

    def add_quote(self, vendor, price):
        self.quotes[vendor] = price


# ------------------------------------------------------------------------------
# Challenge 7: Encapsulation & Input Validation Guard on Price Updates
# ------------------------------------------------------------------------------
# ❌ Buggy Code:
# class Material:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def update_price(self, new_price):
#         self.price = new_price  # Allows zero or negative prices!

# ✅ Fixed Code (Use guard clause to reject prices <= 0):
class Material:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def update_price(self, new_price):
        if new_price <= 0:
            print(f"Price must be greater than 0; you entered {new_price}")
            return
        self.price = new_price


# ------------------------------------------------------------------------------
# Challenge 8: Object Serialization for JSON Persistence (`to_dict`)
# ------------------------------------------------------------------------------
# ❌ Buggy Code:
# class Vendor:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
# # json.dumps([v1]) raises TypeError: Object of type Vendor is not JSON serializable

# ✅ Fixed Code (Provide `to_dict()` method to convert instance to serializable dict):
class Vendor:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def to_dict(self):
        return {"name": self.name, "score": self.score}
