material_count=int(input("How many Materials? "))

materials=[]
for i in range(material_count):
    material=input("Enter Material Name: ")
    current_stock=int(input("Enter Current Stock: "))
    minimum_stock=int(input("Enter Minimum Stock: "))
    materials.append([material, current_stock, minimum_stock])

print("\nMATERIAL RESULTS")
print("----------------")

reorder_count = 0
CRITICAL_count = 0
ok_count = 0


for material in materials:
    print("Material:", material[0])
    print("Current Stock:", material[1])
    print("Minimum Stock:", material[2])
    if material[1] < material[2]:
        print("REORDER REQUIRED")
        reorder_count += 1
    elif material[1] == material[2]:
        print("STOCK LEVEL CRITICAL")
        critical_count += 1
    else:
        print("STOCK LEVEL OK")
        ok_count += 1
    print("----------------")

print("\nSUMMARY")
print("-------")
print("Reorder Required:", reorder_count)
print("Stock Level CRITICAL:", critical_count)
print("Stock Level OK:", ok_count)
