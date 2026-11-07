import json

def load_suppliers():
    try:
        with open("suppliers.json", "r") as file:
            return json.load(file)
    except:
        return {}

def save_suppliers(suppliers):

    with open("suppliers.json", "w") as file:
        json.dump(suppliers, file, indent=4)

def add_supplier():

    suppliers = load_suppliers()

    supplier_id = input("Supplier ID: ")
    name = input("Supplier Name: ")

    quality = float(input("Quality Score: "))
    delivery = float(input("Delivery Score: "))
    price = float(input("Price Score: "))

    suppliers[supplier_id] = {
        "name": name,
        "quality": quality,
        "delivery": delivery,
        "price": price
    }

    save_suppliers(suppliers)

    print("Supplier Added Successfully")

def view_suppliers():

    suppliers = load_suppliers()

    if not suppliers:
        print("No Suppliers Found")
        return

    for supplier_id, data in suppliers.items():

        print("\n-------------------")

        print("ID:", supplier_id)
        print("Name:", data["name"])
        print("Quality:", data["quality"])
        print("Delivery:", data["delivery"])
        print("Price:", data["price"])

def calculate_score(data):

    score = (
        data["quality"] * 0.4 +
        data["delivery"] * 0.3 +
        data["price"] * 0.3
    )

    return round(score, 2)


def view_suppliers():

    suppliers = load_suppliers()

    if not suppliers:
        print("No Suppliers Found")
        return

    for supplier_id, data in suppliers.items():

        total_score = calculate_score(data)

        print("\n-------------------")

        print("ID:", supplier_id)
        print("Name:", data["name"])
        print("Final Score:", total_score)

def best_supplier():

    suppliers = load_suppliers()

    if not suppliers:
        print("No Suppliers Found")
        return

    best_score = 0
    best_name = ""

    for supplier_id, data in suppliers.items():

        score = calculate_score(data)

        if score > best_score:

            best_score = score
            best_name = data["name"]

    print("\nBest Supplier")
    print(best_name)
    print(best_score)

def delete_supplier():

    suppliers = load_suppliers()

    supplier_id = input("Supplier ID to delete: ")

    if supplier_id not in suppliers:
        print("Supplier Not Found")
        return

    del suppliers[supplier_id]
    save_suppliers(suppliers)
    print("Supplier Deleted Successfully")

def search_supplier():
    suppliers = load_suppliers()

    if not suppliers:
        print("No Suppliers Found")
        return

    query = input("Enter Supplier ID or Name: ").strip().casefold()
    matches = [
        (supplier_id, data)
        for supplier_id, data in suppliers.items()
        if query in supplier_id.casefold() or query in data["name"].casefold()
    ]

    if not matches:
        print("Supplier Not Found")
        return

    for supplier_id, data in matches:
        print("\n-------------------")
        print("ID:", supplier_id)
        print("Name:", data["name"])
        print("Quality:", data["quality"])
        print("Delivery:", data["delivery"])
        print("Price:", data["price"])
        print("Final Score:", calculate_score(data))

def update_supplier():
    suppliers = load_suppliers()

    if not suppliers:
        print("No Suppliers Found")
        return

    supplier_id = input("Supplier ID to update: ").strip()

    if supplier_id not in suppliers:
        print("Supplier Not Found")
        return

    data = suppliers[supplier_id]
    name = input(f"Supplier Name [{data['name']}]: ").strip()
    if name:
        data["name"] = name

    for field in ("quality", "delivery", "price"):
        value = input(f"{field.title()} Score [{data[field]}]: ").strip()
        if value:
            try:
                data[field] = float(value)
            except ValueError:
                print("Invalid score")
                return

    save_suppliers(suppliers)
    print("Supplier Updated Successfully")


while True:

    print("\n===== Supplier Evaluation System =====")

    print("1. Add Supplier")
    print("2. View Suppliers")
    print("3. Best Supplier")
    print("4. Delete Supplier")
    print("5. Search Supplier")
    print("6. Update Supplier")
    print("7. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_supplier()

    elif choice == "2":
        view_suppliers()

    elif choice == "3":
        best_supplier()

    elif choice == "4":
        delete_supplier()

    elif choice == "5":
        search_supplier()

    elif choice == "6":
        update_supplier()

    elif choice == "7":
        print("Good Bye")
        break

    else:
        print("Invalid Choice")