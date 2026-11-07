item = input("Enter Item Name: ")

stock = int(input("Enter Current Stock: "))

minimum_stock = 10

print("----------------")

print("Item:", item)

print("Current Stock:", stock)

if stock < minimum_stock:
    print("REORDER REQUIRED")

else:
    print("Stock level is okay")

print("----------------")