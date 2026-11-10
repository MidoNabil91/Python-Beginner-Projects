# ==============================================================================
# Project 7: Supplier List Manager
# Description: A CLI tool to add, view, search, and remove suppliers.
# Built with: Python (Lists, Loops, Conditionals, Defensive Input Handling)
# Developer: Mohamed Nabil
# ==============================================================================

suppliers_list = []

print("\n" + "🚀 " + "=" * 46 + " 🚀")
print("    🏢 WELCOME TO SUPPLIER LIST MANAGER SYSTEM 🏢")
print("🚀 " + "=" * 46 + " 🚀")

while True:
    print("\n" + "📋 " + "=" * 38)
    print(" 1. ➕ Add Supplier")
    print(" 2. 👁️  View Suppliers")
    print(" 3. 🔍 Search Supplier")
    print(" 4. 🗑️  Delete Supplier")
    print(" 5. 🚪 Exit")
    print("=" * 43)

    # Defensive Input Handling
    try:
        user_input = int(input("👉 Please choose a number between 1 to 5: "))
    except ValueError:
        print("\n⚠️  Error: Invalid input! Please enter a valid number, not text.")
        continue

    # 1. Add new supplier
    if user_input == 1:
        add_supplier = input("\n📝 Please enter supplier name: ").lower().strip()
        if not add_supplier:
            print("⚠️  Warning: Supplier name cannot be empty!")
        elif add_supplier in suppliers_list:
            print(f"⚠️  Warning: Supplier '{add_supplier}' already exists!")
        else:
            suppliers_list.append(add_supplier)
            print(f"✅ Success: Supplier '{add_supplier}' added successfully!")

    # 2. View suppliers
    elif user_input == 2:
        if len(suppliers_list) == 0:
            print("\n📭 The supplier list is currently empty!")
        else:
            print("\n" + "📦 " + "=" * 38)
            print("         SUPPLIERS LIST SUMMARY")
            print("=" * 41)
            for i in range(len(suppliers_list)):
                print(f"  {i + 1}. 🏢 {suppliers_list[i].title()}")
            print("=" * 41)
            print(f"📊 Total Approved Suppliers: {len(suppliers_list)}")

    # 3. Search for supplier
    elif user_input == 3:
        search_user = input("\n🔍 Enter Supplier Name to search: ").lower().strip()
        if search_user in suppliers_list:
            print(f"✅ Found: '{search_user.title()}' is in the list.")
        else:
            print(f"❌ Not Found: Supplier '{search_user}' is not in the list.")

    # 4. Delete supplier
    elif user_input == 4:
        remove_supplier = input("\n🗑️  Name the supplier to delete: ").lower().strip()
        if remove_supplier in suppliers_list:
            suppliers_list.remove(remove_supplier)
            print(f"✅ Success: Supplier '{remove_supplier.title()}' removed successfully.")
        else:
            print(f"❌ Error: Supplier '{remove_supplier}' not found!")

    # 5. Exit
    elif user_input == 5:
        print("\n👋 Thank you for using Supplier List Manager. See you soon!")
        break

    # Wrong choice (1-5)
    else:
        print("\n⚠️  Invalid choice! Please select a number between 1 and 5.")