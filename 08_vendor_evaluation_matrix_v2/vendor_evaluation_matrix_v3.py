# ==============================================================================
# Project 8: Vendor Evaluation Matrix v3.0 (JSON Persistent)
# Description: A CLI procurement decision-support tool to evaluate vendors using
#              technical pass/fail screening, weighted scoring, and JSON storage.
# Built with: Python (JSON File Handling, Nested Dictionaries, Functions, Tuples)
# Developer: Mohamed Nabil
# ==============================================================================
import json

def load_vendors():
    try:
        with open("vendors.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_vendors(vendors):
    with open("vendors.json", "w", encoding="utf-8") as file:
        json.dump(vendors, file, indent=4, ensure_ascii=False)


def add_new_vendor(vendors): # 1 . Adding Vendors
    """Adding Vendor With Full Process."""
    #All in put it's about percent between 1 to 100 so it's not the main prices and delivery .
    # 1. Name
    while True:
        name = input("Vendor name: ").strip().lower()
        if not name:
            print("⚠️ Name cannot be empty!")
            continue
        if name in vendors:
            print(f"⚠️ '{name.title()}' already exists!")
            return False
        break

# 2. Price Score
    while True:
        try:
            price = float(input("Price score (0-100): "))
            if not (0 <= price <= 100):
                print("⚠️ Price score must be 0-100!")
                continue
            break
        except ValueError:
            print("⚠️ Invalid price! Enter a number.")
    
    # 3. Delivery Score
    while True:
        try:
            delivery = float(input("Delivery score (0-100): "))
            if not (0 <= delivery <= 100):
                print("⚠️ Delivery score must be 0-100!")
                continue
            break
        except ValueError:
            print("⚠️ Invalid number! Enter a number.")    
    # 4. Quality
    while True:
        try:
            quality = float(input("Quality score (0-100): "))
            if not (0 <= quality <= 100):
                print("⚠️ Quality must be 0-100!")
                continue
            break
        except ValueError:
            print("⚠️ Invalid quality! Enter a number.")
    
    # 5. Technical
    while True:
        try:
            technical = float(input("Technical score (0-100): "))
            if not (0 <= technical <= 100):
                print("⚠️ Technical must be 0-100!")
                continue
            break
        except ValueError:
            print("⚠️ Invalid score! Enter a number.")
    
    # 6. Adding .. Process
    vendors[name] = {
        "price": price,
        "delivery": delivery,
        "quality": quality,
        "technical": technical
    }
    print(f"✅ '{name.title()}' added successfully!")
    return True


def technical_status(score): # # Returns Passed or Rejected based on technical score
    if score >= 70:
        return "Passed"
    return "Rejected"


def calculate_weighted_score(vendor_info): # # Calculate weighted commercial score
    return ((vendor_info["price"] * 0.40) + (vendor_info["delivery"] * 0.25) + (vendor_info["quality"] * 0.35))


def view_vendors(vendors): # 2 . View Vendors
    if not vendors:
        print("\n📭 No vendors added yet!")
        return
    for vendor, info in vendors.items():
        print("=" * 40)
        print(f"Vendor : {vendor.title()}")
        print(f"Price : {info['price']}")
        print(f"Delivery  : {info['delivery']}")
        print(f"Quality : {info['quality']}")
        print(f"Technical : {info['technical']}")
        print("=" * 40)
        print(f"Status : {technical_status(info['technical'])}")
        print(f"Weight Score : {calculate_weighted_score(info):.2f}")
        print("=" * 40)


def find_best_vendor(vendors): # Help to get the best Vendor. # Supp Add
    best_score = 0
    best_vendor = ""
    for vendor, info in vendors.items():
        if technical_status(info["technical"]) == "Rejected":
            continue
        current_score = calculate_weighted_score(info)
        if current_score > best_score:
            best_score = current_score
            best_vendor = vendor
    return (best_score, best_vendor)


def show_menu(): # Only Print Main Menu #
    """ Displays the list of options to the user. """
    print("\n" + "📋 " + "=" * 38)
    print(" 1. ➕ Add Vendor")
    print(" 2. 👁️  View Vendor")
    print(" 3. 🔍 Best Vendor")
    print(" 4. 🗑️  Delete Vendor")
    print(" 5. 🚪 Exit")
    print("=" * 43)


def winner_report(vendors): # 3 . Print the best Vendor #
    score, vendor = find_best_vendor(vendors)
    if not vendor:
        print("\n⚠️ No qualified vendors found (either list is empty or all failed technical screening).")
        return
    print("=" * 50)
    print("🏆 BEST VENDOR")
    print(f"Vendor : {vendor.title()}")
    print(f"Score : {score:.2f}")
    print("=" * 50)


def delete_vendor(vendors): # 5 . To delete vendor #
    del_input = input("\n🗑️  Name the vendor to delete: ").strip().lower()
    if del_input not in vendors:
        print(f"❌ Error: Vendor '{del_input}' not found!")
        return
    del vendors[del_input]
    print(f"✅ Success: Supplier '{del_input.title()}' removed successfully.")


def get_choice(): # # Validate menu choice from user
    """Ask the user for their choice and return number from 1 and 5."""
    while True:
        try:
            choice = int(input("👉 Please choose a number between 1 and 5: "))
            if 1 <= choice <= 5:
                return choice
            print("\n⚠️  Invalid choice! Please select a number between 1 and 5.")
        except ValueError:
            print("\n⚠️  Error: Invalid input! Please enter a valid number, not text.")


def main():
    vendors = load_vendors()
    print("\n" + "🚀 " + "=" * 46 + " 🚀")
    print(" 🏢 WELCOME TO VENDOR MATRIX V2 SYSTEM 🏢")
    print("🚀 " + "=" * 46 + " 🚀")
    while True:
        show_menu()
        choice = get_choice()
        if choice == 1:
            add_new_vendor(vendors)
            save_vendors(vendors)
        elif choice == 2:
            view_vendors(vendors)
        elif choice == 3:
            winner_report(vendors)
        elif choice == 4:
            delete_vendor(vendors)
            save_vendors(vendors)
        else:
            print("\n👋 Thank you for using Vendors Matrix V2. See you soon!")
            break


if __name__ == "__main__":
    main()