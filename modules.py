import mymodule
from mymodule import person1
import platform

mymodule.greeting("Gary")

a = mymodule.person1["age"] # change the function you want to print as is on the other module 
x = platform.system()
y = dir(platform)
print(a)
print(x)
print(y)