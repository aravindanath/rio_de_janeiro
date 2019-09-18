"""
Sets
Sets are an unordered collection of unique elements which
 can be constructed using the set() function.
# We add to sets with the add() method
"""

x = set()
print(x)

# We add to sets with the add() method

x.add(1)
print(x)

# Add a different element


x.add(2)

print(x)

# Try to add the same element x.add(1)

x.add(1)
print(x)


"""

Notice, how it won't place another 1 there as a set is only concerned with unique elements!
However, We can cast a list with multiple repeat elements to a set to get the unique elements. 
"""

# Create a list with repeats

l = [1,1,2,2,3,4,5,6,1,1]

# Cast as set to get unique values

print(set(l))

print(l[6])