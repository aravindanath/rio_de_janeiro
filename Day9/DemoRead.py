
rd = open("./TestData1.txt",'r+')

count = rd.readlines()

print(len(count))
# print(rd.readline())
# print(rd.readline())
# print(rd.readline())

for i in range(len(count)):
    print(rd.readline())


