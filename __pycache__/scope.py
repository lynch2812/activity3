def myfunction():
    first_local = 10
    print(first_local)
myfunction()


def outerFunction():
    outerVariable = 20
    def innerFunction(): 
     print(outerVariable) # Access the variable from the outer scope
    innerFunction() # Call the inner function
outerFunction()

#Example: In complex systems, 
# nested functions are used to ensure helper functions don’t interfere with global or module-level functions.

def calculate_discount(price):
    def apply_discount():
        return price * 0.5
    return apply_discount() #The apply_discount function is only accessible within calculate_discount.

print(calculate_discount(200))  # Output: 100.0

x = 15
def f1(counter):
    x = 50
    def inFunction():
        x = 60
        print(x)  # Prints the local x in inFunction

    if counter > 0:
        inFunction()
        f1(counter - 1)  # Reduce counter to avoid infinite recursion
    print(x)  # Prints the local x in f1

f1(3)  # Start with a counter of 3 including the first local which is called again on 0



 
 
      
      