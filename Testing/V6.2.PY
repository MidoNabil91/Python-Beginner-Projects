supplier = {
	"name": input("Enter supplier name: "),
	"quality": int(input("Enter quality score (0-100): ")),
	"delivery": int(input("Enter delivery score (0-100): ")),
	"price": int(input("Enter price score (0-100): ")),
	"country": input("Enter supplier country: "),
}

average = (
	supplier["quality"]
	+ supplier["delivery"]
	+ supplier["price"]
) / 3

supplier["average"] = average

if average >= 90:
	supplier["status"] = "Approved"
elif average >= 80:
	supplier["status"] = "Conditional"
else:
	supplier["status"] = "Rejected"

supplier.append(supplier)

print("*******************")
print("Supplier:", supplier["name"])
print("Average:", supplier["average"])
print("Status:", supplier["status"])
