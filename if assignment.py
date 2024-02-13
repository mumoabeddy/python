Weight = float(input("Enter weight:"))
Height = float(input("Enter height:"))

BMI = Weight/Height*Height

if BMI >= 30:
    print("Obesity")
elif BMI >= 25 and BMI <= 29.9:
    print("Overweight")
elif BMI >= 18.5 and BMI <= 24.9:
    print("Normalweight")
else:
    print("Underweight")
