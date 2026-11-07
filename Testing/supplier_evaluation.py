supplier = input("Enter Supplier Name: ")

delivery_score = float(input("Delivery Score (0-10): "))

quality_score = float(input("Quality Score (0-10): "))

price_score = float(input("Price Score (0-10): "))

service_score = float(input("Service Score (0-10): "))

total_score = delivery_score + quality_score + price_score + service_score

average_score = total_score / 4

print("********************")

print("Thanks for using Copilot")

print("********************")
print("Supplier:", supplier)
print("Total Score:", total_score)
print("Average Score:", round(average_score, 2))

if average_score >= 8:
    print("APPROVED SUPPLIER")

elif average_score >= 5:
    print("CONDITIONAL APPROVAL")

else:
    print("REJECTED SUPPLIER")