item = input("Enter Item Name: ")

stock = int(input("Enter Current Stock: "))

if stock == 0:
    print("CRITICAL - OUT OF STOCK")

elif stock < 10:
    print("WARNING - REORDER REQUIRED")

else:
    print("STOCK LEVEL OK")