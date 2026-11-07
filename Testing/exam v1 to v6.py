##### Supplier Evaluation System #####
supplier =[
{
    "name": "Halliburton",
    "quality":90,
    "delivery": 85,
    "price": 80,
    "average": 0,
    "status": ""
},
{
    "name": "Weatherford",
    "quality": 70,
    "delivery": 75,
    "price": 70,
    "average": 0,
    "status": ""
},
{
    "name": "Baker Hughes",
    "quality": 45,
    "delivery": 60,
    "price": 50,
    "average": 0,
    "status": ""
}
]

for supplier_record in supplier:
    average = (
        supplier_record["quality"]
        + supplier_record["delivery"]
        + supplier_record["price"]
    ) / 3

    supplier_record["average"] = average

    if average >= 90:
        supplier_record["status"] = "Approved"
    elif average >= 80:
        supplier_record["status"] = "Conditional"
    else:
        supplier_record["status"] = "Rejected"

    print("=========================")
    print("Supplier:", supplier_record["name"])
    print("Average:", supplier_record["average"])
    print("Status:", supplier_record["status"])

print("=========================")
print("Total suppliers evaluated:", len(supplier))
print("=========================")
print("top 1 supplier is", max(supplier, key=lambda x: x["average"])["name"] , "status is", max(supplier, key=lambda x: x["average"])["status"])
print("=========================")