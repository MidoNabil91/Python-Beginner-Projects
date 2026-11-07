supplier_count = int(input("How many suppliers? "))

suppliers = []

for i in range(supplier_count):

    supplier = input("Enter Supplier Name: ")

    price = float(input("Enter Supplier Price: "))
    delivery = float(input("Enter Supplier Delivery: "))
    quality = float(input("Enter Supplier Quality: "))
    service = float(input("Enter Supplier Service: "))

    suppliers.append([supplier, price, delivery, quality, service])

print("\nSUPPLIER RESULTS")
print("----------------")

for supplier in suppliers:

    print("Supplier:", supplier[0])

    print("Price:", supplier[1])
    print("Delivery:", supplier[2])
    print("Quality:", supplier[3])
    print("Service:", supplier[4])

    # Calculate overall score (example: simple average)
    overall_score = (supplier[1] + supplier[2] + supplier[3] + supplier[4]) / 4

    if overall_score >= 8:
        print("APPROVED SUPPLIER")

    elif overall_score >= 5:
        print("CONDITIONAL APPROVAL")

    else:
        print("REJECTED SUPPLIER")

print("----------------")
best_score = max(suppliers, key=lambda x: (x[1] + x[2] + x[3] + x[4]) / 4)
worst_score = min(suppliers, key=lambda x: (x[1] + x[2] + x[3] + x[4]) / 4)
print("Best Supplier:", best_score[0])
print("Best Score:", best_score[1])
print("Worst Supplier:", worst_score[0])
print("Worst Score:", worst_score[1])
print("----------------")
