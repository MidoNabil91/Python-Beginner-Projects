suppliers = [
    {
        "name": "Halliburton",
        "quality": 90,
        "delivery": 91,
        "price": 87,
        },
    {
        "name": "Weatherford",
        "quality": 80,
        "delivery": 85,
        "price": 75,
    },
    {
        "name": "Baker Hughes",
        "quality": 70,
        "delivery": 75,
        "price": 65,
    },
]

for supplier in suppliers:

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

    print("*******************")
    print("Supplier:", supplier["name"])
    print("Average:", supplier["average"])
    print("Status:", supplier["status"])