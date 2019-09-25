# bhuvaneswari
sample=set()
# printing empty set
print(sample)
sample.add(1)
sample.add(2)
sample.add(3)
# printing a set after adding the items
print(sample)
# printing the type to know the class
print(type(sample))
# adding data to a set using for loop
for x in range(4,11):
    sample.add(x)
print(sample)
# creating a second set
sample1=set()
for i in range(10,21):
    sample1.add(i)
print(sample1)
# copying the values of sample to sample1
sample1=sample.copy()
print(sample1)
# removing elements from a set
sample1.remove(5)
print(sample1)
# union of two sets
print(sample.union(sample1))

# to find the ascii value of a character
print(ord('C'))
print(ord('c'))

