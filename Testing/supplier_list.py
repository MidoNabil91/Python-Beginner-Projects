suppliers = []

for i in range(5):
    supplier = input("Enter Supplier Name: ")
    suppliers.append(supplier)

print("\nSUPPLIER LIST")

for supplier in suppliers:
    print("-", supplier)

print("Total Suppliers:", len(suppliers))