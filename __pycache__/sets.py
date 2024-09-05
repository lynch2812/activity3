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
numbers = (1,2,3)
newNumbers = numbers.add(12)
print(numbers)