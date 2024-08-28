#& The & operator performs a bitwise and operation on coresponding bits of two  integars, ot returns a new integar with bits set to 1  if both inputs are 1 

a = 2
b = 9 
result=a&b

print(result)
 
 # OR
 # | = or turns binary back in to decimal 
a = 5 
b = 3
result = a|b
print(result)

# << left shift , shifts the bits of an integar left by the number of positions and multiplys the integar
a = 10
result = a<<2
print(result)

# >> right shift divides the integar by the number requested 

a = 20
result = a>>4
print(result)
#############  precedence
#() evaluated first 
# exponentiation are next 
# multiplaction / division / and floor division are the same precedence 
# addition and subtraction have the same precedence 
# Bitwise left shift and bitwise right shift 
#• Addition + and Subtraction-: Addition and subtraction have the same precedence and are evaluated from left to right.
#• Bitwise Left Shift « and Bitwise Right Shift »: These bitwise shift operators have lower precedence than addition and subtraction.
#• Bitwise AND &: Bitwise AND has lower precedence than bitwise shift operators.
#• Bitwise XOR ^: Bitwise XOR has lower precedence than bitwise AND.
#• Bitwise OR I: Bitwise OR has lower precedence than bitwise XOR.
#• comparison Operators (< =,›, >, l= ==) and Identity Operators (is, is not): These operators are used for comparisons and have lower precedence than bitwise OR.
# membership operators 
#• Membership Operators (in, not in): Membership operators are used to test for membership in sequences and have lower precedence than comparison and identity operators.
#• Logical NOT not: The logical NOT operator has lower precedence than membership operators.
#• Logical AND: Logical AND has lower precedence than logical NOT.
#• Logical OR or: Logical OR has the lowest precedence of all binary operators.
#• When in doubt about the order of evaluation in complex expressions, it's a good practice to use parentheses to make your intentions clear. Parentheses override operator precedence and ensure that the enclosed expressions are evaluated first.
