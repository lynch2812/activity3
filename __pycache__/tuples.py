###### Tuples 

numbers=(1,2,3)

print(numbers[2])

## prints the numbers from individuual variables. after numbers has been assigned above 
a,b,c = numbers

print(a,b,c)
## prints the length of the variable 
print(len(numbers))

## iterating over a tuple 
names = ("Gary","Liam","Chris")

for i in names:
 print(i)

 ## tuple methods 
numbers = 2,8,93,9,8,4,5,2,83,2,5,2,52,2,6
print(numbers.count(8))
# when do we use tuples, they are used when the items wont change during the programmes execution i.e coordinates 
def coordinates():
 return ("j",4)
x,y = coordinates()
print(x,y)