def calculate_discount(price):
    if price >= 100:
        return price * 0.1  # 10% discount
    else:
        return price * 0.05  # 5% discount

print("input price")
price = float(input("Enter Price: "))
discount = calculate_discount(price)
print("Discount on $", price, ":", discount)
print("Final Price after discount:", price - discount)


def po_approval(amount):
    if amount >= 10000:
        return "Management Approval"
    elif amount >= 5000:
        return "Department Approval"
    else:
        return "Auto Approved"


def enter_po_amount():
    amount = float(input("Enter PO Amount: "))
    approval_status = po_approval(amount)
    print("PO Approval Status:", approval_status)

enter_po_amount()