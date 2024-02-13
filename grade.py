marks=int(input("Enter marks code"))

if marks>=80 and marks<=100:
    print("you have scored an A")
elif marks>=60 and marks<80:
    print("you have scored a B")
elif marks>=50 and marks<60:
    print("you have scored a C")
elif marks>=30 and marks<50:
    print("you have scored a D")
elif marks>=0 and marks<30:
    print("you have scored a E")