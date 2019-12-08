x = set()

# adds stuff to set
x.add(33)
x.add('Hello')
x.add(True)

print(x)

# This messes around with set functions
set1 = set([33, "ben", True, 567, "hello", 3869])
set2 = set(["ben", False, 364, 643, "bye", 3869])
set3 = set(['nathan', 465, 2309, "whats up", "goodbye"])
set4 = set([False, 643, "bye"])

#! | is the or and the union character
print(set1|set2)

# difference of both
# Notice that order matters
print(set1 - set2)
print(set2 - set1)

#! & is the and operator
print(set1 & set2)

# Is disjoint returns True if nothing is in common with set 1 and set 3
print(set1.isdisjoint(set3))

# Is subset returns True if all of set 4 is in set 2
print(set4.issubset(set2))

print(set3.issubset(set2))

#! ^ is symetrical difference sign
print(set2 ^ set1)

# This next program shows that arrays are slower than sets
"""
import time
array = []

for i in range (10000000):
    array.append(i)

s = set(array)

# Time for array to check : takes 0.1 seconds
start = time.time()

# Prints true because it is in array
print(5000000 in array)

print(time.time() - start)

# Time for set to check : takes 0.001
start = time.time()

# Prints true because it is in set
print(500000 in s)

print(time.time() - start)
"""