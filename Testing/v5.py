suppliers = [""]

supplier_count = 3

suppliers = [input("Enter Supplier Name: ") for i in range(supplier_count)]

print("Suppliers List:")

# اعرض الموردين هنا
for i, supplier in enumerate(suppliers):
    print(f" {i+1}: {supplier}")