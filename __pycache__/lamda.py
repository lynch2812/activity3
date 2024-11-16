#Lambda functions can have many arguements with one expression - Lambda arguements : expression 
number = lambda x, y: x+y
print(number(3,6))
# used as a small function for only using once 
numberTwo = [1,2,3,4,5]
squares = list(map(lambda x: x**2, numberTwo))
print(squares)
# power of Lambda function is best used anonymously =, it takes 1 arguement 
def numbers(n):
    return lambda a:a*n
check = numbers(4)
another = numbers(6)
print(check(33))
print(another(4))