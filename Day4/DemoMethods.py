
def addNum(x,y):
    add =  x+y
    print("Addition of two num : ",add)
    return add

def subNum(x, y):
    sub = x - y
    # print(sub)
    return sub



def sutudentDeatils():
    print("Martin")

# addNum(20,30)
# addNum(11,221211)
# addNum(210,3320)

# sutudentDeatils()
# val = subNum(33333,4555)
# print(val+30)
#
# ad = addNum(y=33,x=221)
# print(ad+10)


def printRange(x,y):

    print(list(range(x,y)))

def metroCity(city):
    metro =["Hyd","Del","Blr","Mumbai","Che"]

    if city in metro:
        print(city ," is metro city")
    else:
        print("You r in non metro")

metroCity("Amd")


