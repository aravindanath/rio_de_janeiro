"""
While loop

Looping Techniques in Python

Different looping techniques are primarily useful in the places where we don’t need to actually manipulate
 the structure and ordering of overall container, rather only print the elements for a single use instance,
 no inplace change occurs in the container. This can also be used in instances to save time.

 We can use the loops to iterate on the String, list, tuples, set, Dictionary

"""
# Initialization
x = 0
#Condition
while x < 10:
    print("Value of x is "+str(x))
    # Increment
    x = x +1
    #break




l=[]
num=0
while num <10:
    l.append(num)
    num+=1
    print(" Value of num "+ str(num))

print(l)

