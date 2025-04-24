income = float(input("Enter the annual income: "))

tax = 0

if income < 85_528:
    tax = income * 0.18 - 556.02
else:
    tax = (income - 85_528) * 0.32 + 14_839.02

tax = round(tax, 0)

if tax > 0:
    print("The tax is:", tax, "thalers")
else:
    print("The tax is:", 0, "thalers")