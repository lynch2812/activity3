#Python sets 
#Sets are defined by {} curly brackets 
numbers = (1,2,3)

real_numbers = ([6,7,8])

print(real_numbers)

#add(): Adds an element to the set.
#remove(): Removes an element from the set; raises an error if the element is not in the set.
#discard(): Removes an element from the set if it exists; does not raise an error if the element is not in the set. 
#clear(): Removes all elements from the set. 
#copy(): Creates a shallow copy of the set.
#pop(): Removes and returns an arbitrary element from the set.
# len(): Returns the number of elements in the set.
numbers = {1,2,3}
newNumbers = numbers.add(12)
print(numbers)

# Sets 
set1={1,2,3}
set2={4,5,6}

# set union will combine both sets 
set3= set1.union(set2)
print(set3)

set5={7,8,9}
set6={9,11,12}
# intersection pulls the numbe that is the most common
set7=set5.intersection(set6)

print(set7)

set8={1,2,3}
set9={3,4,5}
# .difference pulls the difference out from the two sets, the primary set being the one attached to the .difference set type 
set10=set9.difference(set8)
print(set10)

set11={4,5,6}
set12={6,7,8}
# symetric difference just pulls the numbers which are not common, more than one of the same number in the  instance below. 
set13=set11.symmetric_difference(set12)
print(set13)

# Frozen sets an immutable set, canot be changed or altered 
numbers_set=frozenset([1,2,3])
print(numbers_set)



