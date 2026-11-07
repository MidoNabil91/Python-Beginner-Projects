suppliers = []

def calculate_average(quality, delivery, price):
    return (quality + delivery + price) / 3

def calculate_status(average_score):
    if average_score >= 90:
        return "Approved"
    elif average_score >= 70:
        return "Pending"
    else:
        return "Rejected"

def create_supplier(name, quality, delivery, price):
    average_score = calculate_average(quality, delivery, price)
    return {
        "name": name,
        "quality": quality,
        "delivery": delivery,
        "price": price,
        "average_score": average_score,
        "status": calculate_status(average_score),
    }

def get_score(score_name):
    while True:
        try:
            score = float(input(f"Enter {score_name} score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input.")

def find_supplier(search_name):
    return ((s for s in suppliers if search_name.lower() in s["name"].lower()), None)

def supplier_exists(name):
    return any(supplier["name"].lower() == name.lower() for supplier in suppliers)

def add_supplier():
    name = input("Enter supplier name: ")
    if supplier_exists(name):
        print(f"Supplier {name} already exists.")
        return
    quality = get_score("quality")
    delivery = get_score("delivery")
    price = get_score("price")

    new_supplier = create_supplier(name, quality, delivery, price)
    suppliers.append(new_supplier)
    save_suppliers(suppliers)
    print(f"Supplier {name} added with average score: {new_supplier['average_score']:.2f} ({new_supplier['status']})")
    
def show_statistics():
    if not suppliers:
        print("No suppliers available.")
        return

    total_quality = sum(supplier["quality"] for supplier in suppliers)
    total_delivery = sum(supplier["delivery"] for supplier in suppliers)
    total_price = sum(supplier["price"] for supplier in suppliers)
    total_average = sum(supplier["average_score"] for supplier in suppliers)

    count = len(suppliers)
    print(f"Total Suppliers: {count}")
    print(f"Average Quality Score: {total_quality / count:.2f}")
    print(f"Average Delivery Score: {total_delivery / count:.2f}")
    print(f"Average Price Score: {total_price / count:.2f}")
    print(f"Overall Average Score: {total_average / count:.2f}")
    