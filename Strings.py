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