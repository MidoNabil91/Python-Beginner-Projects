suppliers = []
while True:
    print("\n===== Supplier Evaluation System =====")
    print("1. Add Supplier Evaluation")
    print("2. Show Suppliers")
    print("3. Show Top Supplier")
    print("4. Statistics")
    print("5. Search Supplier")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter supplier name: ")
        quality = float(input("Enter quality score (0-100): "))
        delivery = float(input("Enter delivery score (0-100): "))
        price = float(input("Enter price score (0-100): "))

        average_score = (quality + delivery + price) / 3
        if average_score >= 90:
            status = "Approved"
        elif average_score >= 80:
            status = "Conditional"
        else:
            status = "Rejected"

        suppliers.append({
            "name": name,
            "quality": quality,
            "delivery": delivery,
            "price": price,
            "average_score": average_score,
            "status": status,
        })
        print(f"Supplier {name} added with average score: {average_score:.2f} ({status})")

    elif choice == "2":
        if not suppliers:
            print("No suppliers found.")
        else:
            print("\n===== Supplier List =====")
            for i, supplier in enumerate(suppliers, start=1):
                print(f"{i}. {supplier['name']}")
                print(
                    f"Name: {supplier['name']}, Quality: {supplier['quality']}, "
                    f"Delivery: {supplier['delivery']}, Price: {supplier['price']}, "
                    f"Average Score: {supplier['average_score']:.2f}, Status: {supplier['status']}"
                )
    elif choice == "3":
        if not suppliers:
            print("No suppliers available.")
        else:
            top_supplier = max(suppliers, key=lambda supplier: supplier["average_score"])
            print(f"Name: {top_supplier['name']}")
            print(f"Score: {top_supplier['average_score']:.2f}")
            print(f"Status: {top_supplier['status']}")
          

    elif choice == "4":
        print("Statistics:")
        if suppliers:
            total_suppliers = len(suppliers)
            approved_suppliers = len([s for s in suppliers if s["status"] == "Approved"])
            conditional_suppliers = len([s for s in suppliers if s["status"] == "Conditional"])
            rejected_suppliers = len([s for s in suppliers if s["status"] == "Rejected"])

            print(f"Total Suppliers: {total_suppliers}")
            print(f"Approved: {approved_suppliers}")
            print(f"Conditional: {conditional_suppliers}")
            print(f"Rejected: {rejected_suppliers}")
        else:
            print("No suppliers found.")
    elif choice == "5":
        search_name = input("Enter supplier name to search: ")
        found_suppliers = [s for s in suppliers if s["name"].lower() == search_name.lower()]
        if found_suppliers:
            for supplier in found_suppliers:
                print(
                    f"Name: {supplier['name']}, "
                    f"quality: {supplier['quality']}, "
                    f"Delivery: {supplier['delivery']}, "
                    f"Price: {supplier['price']}, "
                    f"Average Score: {supplier['average_score']:.2f}, "
                    f"Status: {supplier['status']}"
                )
        else:
            print(f"No supplier found with name '{search_name}'.")
    elif choice == "6":
        print("goodbye!")
        break