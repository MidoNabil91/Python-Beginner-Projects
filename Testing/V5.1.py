suppliers = []

while True:
    print("\n===== Supplier Database =====")
    print("1. Add Supplier")
    print("2. Show Suppliers")
    print("3. Count Suppliers")
    print("4. Search Supplier")
    print("5. Delete Supplier")
    print("6. Update Supplier")
    print("7. exit")

    choice = input("Choose an option: ")
    if choice == "1":
        supplier_name = input("Enter Supplier Name: ")
        suppliers.append(supplier_name)
        print(f"Supplier '{supplier_name}' added successfully!")

    elif choice == "2":
        if suppliers:
            print("Suppliers List:")
            for i, supplier in enumerate(suppliers):
                print(f" {i + 1}: {supplier}")
        else:
            print("No suppliers found.")

    elif choice == "3":
        print(f"Total number of suppliers: {len(suppliers)}")

    elif choice == "4":
        supplier_to_search = input("Enter Supplier Name to search: ")
        if supplier_to_search in suppliers:
            print(f"Supplier '{supplier_to_search}' found.")
        else:
            print(f"Supplier '{supplier_to_search}' not found.")

    elif choice == "5":
        supplier_to_delete = input("Enter Supplier Name to delete: ")
        if supplier_to_delete in suppliers:
            suppliers.remove(supplier_to_delete)
            print(f"Supplier '{supplier_to_delete}' deleted successfully!")
        else:
            print(f"Supplier '{supplier_to_delete}' not found.")

    elif choice == "6":
        supplier_to_update = input("Enter Supplier Name to update: ")
        if supplier_to_update in suppliers:
            new_supplier_name = input("Enter new Supplier Name: ")
            supplier_index = suppliers.index(supplier_to_update)
            suppliers[supplier_index] = new_supplier_name
            print(f"Supplier '{supplier_to_update}' updated to '{new_supplier_name}' successfully!")
        else:
            print(f"Supplier '{supplier_to_update}' not found.")

    elif choice == "7":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")
