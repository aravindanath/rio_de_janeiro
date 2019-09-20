
marks = int(input("Enter your marks:"))

if marks < 35 :
    print("Fail")
elif marks >=35 and marks <55:
    print("Third class")
elif marks >=55 and marks <65:
    print("Second class")
elif marks >=65 and marks <85:
    print("First class")
elif marks >=85 and marks <=100:
    print("Topper!")
else:
    print("Invalid")

