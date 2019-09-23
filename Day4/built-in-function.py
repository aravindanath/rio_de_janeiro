"""
max()

min()

abs()

type()

"""


def largest_num(*arg):
    print(max(arg))
  #  return(max(arg))



largest_num(10,22,33,4444,1)


def smallest_num(*arg):
    print(min(arg))

smallest_num(33,21,22,11,1)


def abs_function(arg):
    print(abs(arg))


abs_function(-20)
abs_function((20))

print(type(99))
print(type(99.00))
print(type("99"))

l = [2,3,4,2]
print(type(l))