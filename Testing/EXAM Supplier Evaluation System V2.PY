suppliers = []

def calculate_average(quality, delivery, price):
    return (quality + delivery + price) / 3

def calculate_status(average_score):
    if average_score >= 90:
        return "Approved"
    elif average_score >= 80:
        return "Conditional"
    else:
        return "Rejected"

def add_supplier():
    name = input("Enter supplier name: ")
    if any(supplier["name"].lower() == name.lower() for supplier in suppliers):
        print(f"Supplier {name} already exists.")
        return
    try:
                quality = float(input("Enter new quality score (0-100): "))
                delivery = float(input("Enter new delivery score (0-100): "))
                price = float(input("Enter new price score (0-100): "))
    except ValueError:
                print("Scores must be numeric values between 0 and 100.")
                return
    if quality < 0 or quality > 100 or delivery < 0 or delivery > 100 or price < 0 or price > 100:
        print("Scores must be between 0 and 100.")
        return
    average_score = calculate_average(quality, delivery, price)
    status = calculate_status(average_score)

    suppliers.append({
        "name": name,
        "quality": quality,
        "delivery": delivery,
        "price": price,
        "average_score": average_score,
        "status": status,
    })
    print(f"Supplier {name} added with average score: {average_score:.2f} ({status})")

def show_suppliers():
    if not suppliers:
        print("No suppliers found.")
    else:
        print("\n===== Supplier List =====")
        for i, supplier in enumerate(suppliers, start=1):
            print("==============================")
            print(f"{i}. {supplier['name']}")
            print(f"Name: {supplier['name']}")
            print(f"Quality: {supplier['quality']}, ")
            print(f"Delivery: {supplier['delivery']}, ")
            print(f"Price: {supplier['price']}, ")
            print(f"Average Score: {supplier['average_score']:.2f}, ")
            print(f"Status: {supplier['status']}")
            print("==============================")
            
def search_supplier():
    search_name = input("Enter supplier name to search: ")
    found_suppliers = [s for s in suppliers if search_name.lower() in s["name"].lower()]

    if found_suppliers:
        for supplier in found_suppliers:
            print(
                f"Name: {supplier['name']}, "
                f"Quality: {supplier['quality']}, "
                f"Delivery: {supplier['delivery']}, "
                f"Price: {supplier['price']}, "
                f"Average Score: {supplier['average_score']:.2f}, "
                f"Status: {supplier['status']}"
            )
    else:
        print(f"No suppliers found with name containing '{search_name}'.")
def delete_supplier():
    delete_name = input("Enter supplier name to delete: ")
    found_suppliers = [s for s in suppliers if delete_name.lower() in s["name"].lower()]

    if found_suppliers:
        for supplier in found_suppliers:
            suppliers.remove(supplier)
            print(f"Supplier {supplier['name']} deleted.")
    else:
        print(f"No suppliers found with name containing '{delete_name}'.")

def show_top_supplier():
    if not suppliers:
        print("No suppliers available.")
    else:
        top_supplier = max(suppliers, key=lambda supplier: supplier["average_score"])
        print(f"Name: {top_supplier['name']}")
        print(f"Score: {top_supplier['average_score']:.2f}")
        print(f"Status: {top_supplier['status']}")

def show_statistics():
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
        print(f"Average Score of All Suppliers: {sum(s['average_score'] for s in suppliers) / total_suppliers:.2f}")
    else:
        print("No suppliers available.")

def Update_supplier():
    update_name = input("Enter supplier name to update: ")
    found_suppliers = [s for s in suppliers if update_name.lower() in s["name"].lower()]

    if found_suppliers:
        for supplier in found_suppliers:
            print(f"Updating supplier: {supplier['name']}")
            try:
                quality = float(input("Enter new quality score (0-100): "))
                delivery = float(input("Enter new delivery score (0-100): "))
                price = float(input("Enter new price score (0-100): "))
            except ValueError:
                print("Scores must be numeric values between 0 and 100.")
                return

            if any(score < 0 or score > 100 for score in (quality, delivery, price)):
                print("Scores must be between 0 and 100.")
                return

            average_score = (quality + delivery + price) / 3
            status = calculate_status(average_score)

            supplier.update({
                "quality": quality,
                "delivery": delivery,
                "price": price,
                "average_score": average_score,
                "status": status,
            })
            print(f"Supplier {supplier['name']} updated with average score: {average_score:.2f} ({status})")
    else:
        print(f"No suppliers found with name containing '{update_name}'.")

while True:
    print("\n===== Supplier Evaluation System =====")
    print("1. Add Supplier Evaluation")
    print("2. Show Suppliers")
    print("3. Show Top Supplier")
    print("4. Statistics")
    print("5. Search Supplier")
    print("6. Update Supplier")
    print("7. Delete Supplier")
    print("8. Exit")

    choice = input("Choose an option: ")
    if choice == "1":
        add_supplier()
    elif choice == "2":
        show_suppliers()
    elif choice == "3":
        show_top_supplier()
    elif choice == "4":
        show_statistics()
    elif choice == "5":
        search_supplier()
    elif choice == "6":
        Update_supplier()
    elif choice == "7":
        delete_supplier()
    elif choice == "8":
        print("Exiting the program.")
        break
    else:
        print("Invalid option. Please try again.")