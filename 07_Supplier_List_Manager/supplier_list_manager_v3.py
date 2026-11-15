# ==============================================================================
# Project 7: Supplier List Manager v3.0
# Description: A CLI tool to add, view, search, update, and remove suppliers.
# Built with: Python (Dictionaries, Functions, Loops, Defensive Input)
# Developer: Mohamed Nabil
# ==============================================================================

def show_menu():
    """ Displays the list of options to the user. """
    print("\n" + "📋 " + "=" * 38)
    print(" 1. ➕ Add Supplier")
    print(" 2. 👁️  View Suppliers")
    print(" 3. 🔍 Search Supplier")
    print(" 4. 📋 Update Supplier Status")
    print(" 5. 🗑️  Delete Supplier")
    print(" 6. 🚪 Exit")
    print("=" * 43)


def get_choice():
    """Ask the user for their choice and return number from 1 to 6."""
    while True:
        try:
            choice = int(input("👉 Please choose a number between 1 and 6: "))
            if 1 <= choice <= 6:
                return choice
            print("\n⚠️  Invalid choice! Please select a number between 1 and 6.")
        except ValueError:
            print("\n⚠️  Error: Invalid input! Please enter a valid number, not text.")


def login(users):
    """It requests login credentials and verifies them. It returns True/False."""
    attempts = 0
    while attempts < 3:
        username = input("Please enter username: ").strip().lower()
        password = input("Please enter password: ").strip()
        if username in users and password == users[username]:
            print("✅ Login successful.")
            return True
        print("⚠️ Invalid username or password. Please try again.")
        attempts += 1
    print("🔒 Account locked! Too many failed attempts.")
    return False


def add_supplier(suppliers):
    """Adds a new supplier to the dictionary after verifying the name."""
    name = input("\n📝 Please enter supplier name: ").strip().lower()
    if not name:
        print("⚠️  Warning: Supplier name cannot be empty!")
        return
    if name in suppliers:
        print(f"⚠️  Warning: Supplier '{name}' already exists!")
        return
    category = input("\n♻️ Please enter supplier category: ").strip().lower()
    status = input("\n📌 Please enter supplier status: ").strip().title()
    suppliers[name] = {"category": category, "status": status}
    print(f"✅ Success: Supplier '{name}' added successfully!")


def view_suppliers(suppliers):
    """Display All suppliers in List."""
    if not suppliers:
        print("\n📭 The supplier list is currently empty!")
        return
    print("\n" + "📦 " + "=" * 38)
    print("         SUPPLIERS LIST SUMMARY")
    print("=" * 41)
    print(f"🏢 Total Suppliers: {count_suppliers(suppliers)}")   # ← استخدمنا الدالة الجديدة
    print("-" * 41)
    for i, (name, info) in enumerate(suppliers.items(), start=1):
        print(f"  {i}. 🏢 {name.title()} | {info['status'].title()} | {info['category'].title()}")
    print("=" * 41)


def search_supplier(suppliers):
    """Search for a resource by name (partial search)."""
    term = input("\n🔍 Enter Supplier Name to search: ").strip().lower()
    found = False
    for name, info in suppliers.items():
        if term in name:
            print(f"✅ Found: {name.title()} | Category: {info['category'].title()} | Status: {info['status'].title()}")
            found = True
    if not found:
        print(f"❌ Not Found: No supplier matching '{term}'.")


def update_supplier(suppliers):
    """An existing resource state occurs."""
    name = input("\n📋 Name the supplier to update: ").strip().lower()
    if name not in suppliers:
        print(f"❌ Error: Supplier '{name}' not found!")
        return
    new_status = input("New Status For the supplier: ").strip().title()
    suppliers[name]["status"] = new_status
    print(f"✅ Success: '{name.title()}' status updated to '{new_status}'.")


def delete_supplier(suppliers):
    """Delete an existing resource."""
    name = input("\n🗑️  Name the supplier to delete: ").strip().lower()
    if name not in suppliers:
        print(f"❌ Error: Supplier '{name}' not found!")
        return
    del suppliers[name]
    print(f"✅ Success: Supplier '{name.title()}' removed successfully.")


def main():
    """The program's main entry point."""
    users = {"nabel": "1234", "admin": "0000"}
    suppliers = {
        "kgl": {"category": "logistics", "status": "Approved"},
        "agility": {"category": "freight", "status": "Conditional"}
    }

    print("\n" + "🚀 " + "=" * 46 + " 🚀")
    print("    🏢 WELCOME TO SUPPLIER LIST MANAGER SYSTEM 🏢")
    print("🚀 " + "=" * 46 + " 🚀")

    if not login(users):
        return

    while True:
        show_menu()
        choice = get_choice()
        if choice == 1:
            add_supplier(suppliers)
        elif choice == 2:
            view_suppliers(suppliers)
        elif choice == 3:
            search_supplier(suppliers)
        elif choice == 4:
            update_supplier(suppliers)
        elif choice == 5:
            delete_supplier(suppliers)
        elif choice == 6:
            print("\n👋 Thank you for using Supplier List Manager. See you soon!")
            break

def count_suppliers(suppliers):
    return len(suppliers)

if __name__ == "__main__":
    main()