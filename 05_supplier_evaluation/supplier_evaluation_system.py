# ==========================================
# Supplier Evaluation System
# Created by Mohamed Nabil
# ==========================================

def header():
    print("=" * 40)
    print("📋 Supplier Evaluation System")
    print("=" * 40)

def calc_average(quality, delivery, price):
    return (quality * 0.4) + (delivery * 0.3) + (price * 0.3)

def get_supp_status(score):
    if score >= 90:
        return "Approved"
    elif score >= 80:
        return "Conditional"
    else:
        return "Rejected"

def get_supp_risk(score):
    if score >= 90:
        return "Low Risk"
    elif score >= 80:
        return "Medium Risk"
    else:
        return "High Risk"

def generate_report(quality, delivery, price):
    # Calculating the average based on the inputs
    avg_score = calc_average(quality, delivery, price)
    status = get_supp_status(avg_score)
    risk = get_supp_risk(avg_score)
    
    # Print the coordination report
    print("\n")
    header()
    print(f"Quality Score   : {quality:.2f}")
    print(f"Delivery Score  : {delivery:.2f}")
    print(f"Price Score     : {price:.2f}")
    print("*" * 50)
    print(f"Average Score   : {avg_score:.2f}")
    print("*" * 50)
    print(f"Status          : {status}")
    print(f"Risk Level      : {risk}")
    print("=" * 50)

# ==========================================
# Main Program
# ==========================================
header()

while True: # While here to make loop if we need to add other supplier or not .. very helpful for checking more then 1 supplier
    # 1. Data Entry
    quality = float(input("Please Enter Quality Score (0-100) = "))
    delivery = float(input("Please Enter Delivery Rate Score (0-100) = "))
    price = float(input("Please Enter Price Rate Score (0-100) = "))

    # 2. Print Report
    generate_report(quality, delivery, price)

    # 3. Question if need to check other supplier ?
    start_again = input("\nEvaluate another supplier? (y/n): ").lower().strip() # used lower to be sure it's correct for condition

    # 4. condition for exit
    if start_again != "y":
        print("👋 Thanks for using Supplier Evaluation System!")
        break  # y for continue or n break the loop and exit.