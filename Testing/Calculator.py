#Calculator
num1 = float(input("First Number : "))
opera = input("Choose an Operation : ")
num2 = float(input("Second Number : "))
if opera == "+":
    resault = num1+num2
    print("Resault : ", num1, "+", num2, "=", resault)
elif opera == "-":
    resault = num1-num2
    print("Resault : ", num1, "-", num2, "=", resault)
elif opera == "*":
    resault = num1*num2
    print("Resault : ", num1, "*", num2, "=", resault)
elif opera == "%":
    resault = num1%num2
    print("Resault : ", num1, "%", num2, "=", resault)
elif opera == "/":
    if num2 != 0:
        resault = num1/num2
        print("Resault : ", num1, "/", num2, "=", resault)
    else:
        print("Can't Division by Zero !!")
else:
    ("Invalid Operation! Ya Basha")