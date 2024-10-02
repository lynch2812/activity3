def greet(name):
    print(f"Hello , {name}!")

greet("John")
# below will print out the fist names and put it before the string introducing the second names 
def tester(fname):
    print(fname+" johnson")
tester("Chris")
tester("Steve")
tester("John")

def testertwo(country = "Denmark"):
    print("a scandanavian country is" +country)
testertwo(" Sweden")
testertwo(" Iceland")

# creating arguements and listing seperately 

def testerthree(food):
 for x in food:
    print(x)
meats = ["Pork", "Chicken", "Lamb"]
testerthree(meats)