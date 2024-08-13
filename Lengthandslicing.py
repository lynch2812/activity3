x = "I love eating"

print("love" in x)
#using 'in ' to check if a word is in the string
if "love" in x:
    print("Yes it damn well is") 
    #using  'not in' to check a word isnt in the string
if "hate" not in x:
    print("it damn wel isnt!")

################################################Slicing 
x = "I love football"
#includes spaces as numbers {2:6} prints only that section of the string
#if you use this format 2: this will pull every letter after the 2nd position 
#if you use this format :4 this will pull every letter before the 4th position 
#if you use this format -2: this will pull every letter after the 2nd position from the right and so on 
print(x[:-2])