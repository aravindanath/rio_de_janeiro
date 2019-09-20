"""
 We can use the loops to iterate on the Strings, list, tuples, set, Dictionary

"""


myString= 'abcabcaaa'

for c in myString:
    if c=='a':
        print("A", end='')
    else:
        print(c, end='')

print(c, end='')



cars = ['bmw', 'honda', 'audi']

for car in cars:
    if car == 'bmw':
        print("BMW", end='')
    else:
        print(car,end='')
