class MyClass:
    # Class attribute
    class_variable = "I am a class variable"

    # Constructor to initialize instance attributes
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    # Instance method
    def instance_method(self):
        return "I am an instance method"

# Create an object of the class
my_object = MyClass("value1", "value2")

# Access instance attributes
print(my_object.attribute1)  # Output: value1
print(my_object.attribute2)  # Output: value2

# Access class attribute
print(MyClass.class_variable)  # Output: I am a class variable

# Call instance method
print(my_object.instance_method())  # Output: I am an instance method



    ## 
class childclass(partentClass):
    # attributes 

