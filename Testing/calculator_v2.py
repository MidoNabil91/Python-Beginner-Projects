supplier = input("Enter Supplier Name: ")

item = input("Enter Item Name: ")

quantity = int(input("Enter Quantity: "))

price = float(input("Enter Unit Price: "))

total = quantity * price

print("-------------------")
print("PURCHASE SUMMARY")
print("-------------------")
print("Supplier:", supplier)
print("Item:", item)
print("Quantity:", quantity)
print("Unit Price:", price)
print("Total Cost:", total)