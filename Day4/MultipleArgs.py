
def singleArgs(a):
    print("Single args",a)

def multipleArgs(*args):
    print("Multiple args",args)

def multipleKwargs(**kwargs):
    print("Multiple key words args",kwargs)


singleArgs("Arvind")
multipleArgs("Arvind","Deepak","BHuvaneshwari",202773)
multipleKwargs(Subject='Java',City='Bangalore')


def exampleArgs(single,*multy,**kwMulty):

    print(single)
    print(multy)
    print(kwMulty)

exampleArgs(333,2345,2345,2345,google="java")




