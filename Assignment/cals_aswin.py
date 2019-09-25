print("add-1")
print("sub-2")
print("mul-3")
print("div-4")
print("floor-5")
print("round-6")
opt = (input("enter the option"))
# a = (input("enter the number a"))
# b = (input("enter the number b"))
if opt == "1":
    a = (input("enter the number a"))
    b = (input("enter the number b"))
    print("the addition of two number is", float(a) + float(b))
elif opt == "2":
    a = (input("enter the number a"))
    b = (input("enter the number b"))
    print("the subtraction of two number is", float(a) - float(b))
elif opt == "3":
    a = (input("enter the number a"))
    b = (input("enter the number b"))
    print("the multiplication of two number is", float(a) * float(b))
elif opt == "4":
    a = (input("enter the number a"))
    b = (input("enter the number b"))
    print("the division of two number is", float(a) / float(b))
elif opt == "5":
    a = (input("enter the number a"))
    b = (input("enter the number b"))
    print("the floor of two number is", float(a) // float(b))
elif opt == "6":
    a = (input("enter the number a"))
    b = (input("enter the number b"))
    print("the round of two number is", round(float(a)) / round(float(b)))
else:
    print("please enter the valid number")








