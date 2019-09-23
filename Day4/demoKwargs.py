
def values(val,*args,**kwargs):
    print(val,args,kwargs)

# values("Sahoo",22,"Java","python","c++",type='online',time=10)


def val(a=10,g=20):
    print(a*g)



def launchBrowser(browser="ios"):
    if browser is "ios":
        print("Launching ios")
    elif browser is "android":
        print("Launching android")
    elif browser is "harmonyOS":
        print("Launching harmonyOS")
    else:
        print("Pls enter rite browser name!")


# launchBrowser("android")


bool_order = True or not False and False
print(bool_order)
