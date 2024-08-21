print("python lists".upper())
my_list=[1, 2, 3, 4, 5]
#starts from zero in lists 
first_element = my_list[1]
#will print the number 2 off using [1]
print(first_element)
# .append adds to the last position 
#below will add 6 and so will print [1,2,3,4,5,6]
my_list.append(6)
print(my_list)
#### .insert(first number is the position, second number is the placement)
my_list.insert(0, 10)
result=my_list
print(result)
#.remove(remove the actual item from the list in this instance 3)
my_list.remove(3)
result = my_list
print(result)
########## slicing [two different positions split by :second position here ]
result=my_list[1:3]
print(result)
######### combined list 

# + combines lists combined_list = my_list + [what you are combining]
#len()- the length of the list 
#reverse()
#count()
#index()
# list comprehension
#squared_numbers= [x **2 for x in my_list] check x put it in to the power of 2 and add it in to my_list

