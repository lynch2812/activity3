#three speechmarks on either side let you print on three different lines
name='''this is  a test line, 
a major line, 
good practice'''

print(name)
#square brackets with a number index print the letter starting from 0
name= 'Gary Lynch'
print(name[0])
print(name[1])
print(name[2])
print(name[3])
#####################Modifying strings##############
x = "we love chelsea"
#### changes to uppercase 
print(x.upper())
###takes out whitespace 
print(x.strip())
## replace words 
print(x.replace("we", "I "))
##split which creates a list
print(x.split(","))
#########String  concatenate to adad to strings together 

a = "Real"
b = "Madrid"
c = a + " " + b
print(c)
###### format strings 
## To print the age string and number in the same string you have to add : {} in the string variable and the format option in print 
age  = 36
my_age="My age is: {} "
print(my_age.format(age))
#### to add multiple in a string see the below 
home= 2
away= 0
points= 3
#the {} decide which variable goes where, automatically or using numbers 0 onwards depending on position
football_match = "chelsea {} vs {} arsenal, chelsea get {} points"
print(football_match.format(home,away,points))
################# String methods 
#capitalize() first character to uppercase 
#casefold( Converts string to Lowercase )
#center() Returns a centered string 
#count() Returns the number of times a specified value occurs in a string 
#encode() Returns an encoded version of the string 
#endswith(returns true if the string ends with a specified value)
#expandtabs() sets the tab size of the string 
#find() Searches the string for a specified value and returns the position of where it was found 
# alot more can be used https://www.w3schools.com/python/python_ref_string.asp
