#+ addition operators 
#- Subtraction
 #* multiplication 
#/ Division 
#// Floor division 
#% modulus 
#** exponentiation the power of 


a = 10
b = 3

addition = a+b
subtraction = a-b
multiplication = a*b
division = a/b
floor_division = a//b
modulus = a%b
exponentiation = a**b

print(addition)
print(subtraction)
print(multiplication)
print(division)
print(floor_division)
print(modulus)
print(exponentiation)

###### comparison operators 
#== equal to 
#!= not equal to 
#< Less than 
#> Greater than
#<= Less than or equal to 
#>= Greater or equal to 

x =5 
y = 10 

is_equal = x==y 
print(is_equal)
is_not_equal = x!=y
print(is_not_equal)
is_less_then = x<y
print(is_not_equal)
is_greater_than = x>y
print(is_not_equal)
is_less_equal = x<=y
print(is_less_equal)
is_greater_equal = x>=y
print(is_greater_than) 

###########Logical operators 
# and_
#or_
#not_
print("logical operators".upper())
p=True 
q=False

result_and=p and q 
result_not=  not p 
result_or = p or q 



print(result_and)
print(result_not)
print(result_or)

#### Assignment operators 
print("assignment operators".upper())
# = Assignment 
# += Add and Assign 
# -= Subtract and assign 
# *=Multiply and assign
# /= Divide and Assign 
#//= Floor divide and assign 
# %= Modulus and assign gives you the remainder after multiplying in to the number 
# **= Exponentiate and assign 

x = 10
x %= 4 # use the operator to do the math 
print(x)

##### Membership operators 
#to test if a value is in the sequence giving you a true or false, checking if a value in a list like below for example 

print("Membership operators".upper())

my_list= [1,2,3,4]
even = 6 in my_list # for example 3
odd = 3 in my_list
outcast = 7 not in my_list
print(even)
print(odd)
print(outcast)

#########Identity operator 
#is: True if two variables reference the same object 
#is not: True if two variables reference different objects
# 
print("identity operator".upper())
c = [1, 2, 3] 
d = c
# the below will = True because d  = c we are checking that they are the same object 
same_operator = d is c
print(same_operator)

