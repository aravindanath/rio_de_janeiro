
empty=[]

tup= (1,2,3,55.3,3)



x = 0

while x<=10:
    print(x)
    empty.append(x)
    x=x+3

    # break
else:
    print("Out of loop!..")


print(empty)
empty.sort(reverse=True)
print(empty)
empty.pop()
print(empty)