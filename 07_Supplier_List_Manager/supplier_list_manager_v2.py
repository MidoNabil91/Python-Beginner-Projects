# ==============================================================================
# Project 7: Supplier List Manager v2.0
# Description: A CLI tool to add, view, search, update, and remove suppliers.
# Built with: Python (Dictionaries, Functions, Loops, Conditionals, Defensive Input Handling)
# Developer: Mohamed Nabil
# ==============================================================================
def login():
    attempts = 0
    while attempts < 3:
        username = input("Please enter username : ").strip().lower()
        password = input("Please enter userPassword : ").strip()
        if username in users and password == users[username]:
            print("✅ Login successful.")
            return True
        print("⚠️ Invalid username or password. Please try again.")
        attempts += 1
    print("🔒 Account locked! Too many failed attempts.")
    return False

suppliers = {
    "kgl": {"category": "Logistics", "status": "Approved"},
    "agility": {"category": "Freight", "status": "Conditional"}
}

users = {"nabel": "1234", "admin": "0000"}

if not login():
    exit()

print("\n" + "🚀 " + "=" * 46 + " 🚀")
print("    🏢 WELCOME TO SUPPLIER LIST MANAGER SYSTEM 🏢")
print("🚀 " + "=" * 46 + " 🚀")

while True:
    print("\n" + "📋 " + "=" * 38)
    print(" 1. ➕ Add Supplier")
    print(" 2. 👁️  View Suppliers")
    print(" 3. 🔍 Search Supplier")
    print(" 4. 📋 Update Supplier Status")
    print(" 5. 🗑️  Delete Supplier")
    print(" 6. 🚪 Exit")
    print("=" * 43)

    # Defensive Input Handling
    try:
        user_input = int(input("👉 Please choose a number between 1 to 6: "))
    except ValueError:
        print("\n⚠️  Error: Invalid input! Please enter a valid number, not text.")
        continue

    # 1. Add new supplier
    if user_input == 1:
        try:
            add_supplier = input("\n📝 Please enter supplier name: ").lower().strip()
        except ValueError:
            print("Please enter correct data !")
        if not add_supplier:
            print("⚠️  Warning: Supplier name cannot be empty!")
        elif add_supplier in suppliers:
            print(f"⚠️  Warning: Supplier '{add_supplier}' already exists!")
        else:
            add_supp_cat = input("\n♻️ Please enter supplier category: ").lower().strip()
            add_supp_stat = input("\n📌 Please enter supplier status: ").title().strip()
            suppliers[add_supplier] = {"category": add_supp_cat,
                                       "status": add_supp_stat}
            print(f"✅ Success: Supplier '{add_supplier}' added successfully!")

    # 2. View suppliers
    elif user_input == 2:
        if len(suppliers) == 0:
            print("\n📭 The supplier list is currently empty!")
        else:
            print("\n" + "📦 " + "=" * 38)
            print("         SUPPLIERS LIST SUMMARY")
            print("=" * 41)
            print(f"🏢 Total Suppliers List is : {len(suppliers)}")
            for name , info in suppliers.items():
                print(f"🏢 {name.title()} | {info['status'].title()} | {info['category'].title()}")
            print("=" * 41)

    # 3. Search for supplier
    elif user_input == 3:
        search_user = input("\n🔍 Enter Supplier Name to search: ").lower().strip()
        found = False
        for name, info in suppliers.items():
            if search_user in name:
                print(f"✅ Found: {name.title()} | Category: {info['category'].title()} | Status: {info['status']}")
                found = True
        if not found:
            print(f"❌ Not Found: No supplier matching '{search_user}'.")
    
    # 4. Update supplier :
    elif user_input == 4:
        update_name = input("\n📋 Name the supplier to update: ").lower().strip()
        if update_name in suppliers:
            new_status = input("New Status For the supplier: ").strip().title()
            suppliers[update_name]["status"] = new_status
            print(f"✅ Success: '{update_name.title()}' status updated to '{new_status}'.")
        else:
            print(f"❌ Error: Supplier '{update_name}' not found!")
    
    # 5. Delete supplier
    elif user_input == 5:
        remove_supplier = input("\n🗑️  Name the supplier to delete: ").lower().strip()
        if remove_supplier in suppliers:
            del suppliers[remove_supplier]
            print(f"✅ Success: Supplier '{remove_supplier.title()}' removed successfully.")
        else:
            print(f"❌ Error: Supplier '{remove_supplier}' not found!")
    
    # 6. Exit
    elif user_input == 6:
        print("\n👋 Thank you for using Supplier List Manager. See you soon!")
        break
    
    # Wrong choice (1-6)
    else:
        print("\n⚠️  Invalid choice! Please select a number between 1 and 6.")
