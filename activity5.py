#madrid = "This is the Spanish capital"
#london = "This is the English captial"
#paris = "This is the French capital"
#berlin = "This is the German capital"
#rome = "This is the Italian capiltal"
#x = slice(20)
#print(madrid.upper())
#print(london.lower())
#print(paris[x])
#print(len(berlin))
#for rome in rome:
 #   print(rome)#

input_string = input("Enter a string: ")

print("\nString manipulation menu")
print("1. Convert to upercase ")
print("2. convert  to lowercase")
print("3. Slice the string")
print("4. calculate string length")
print("5. Loop through the characters")

choice = int(input("Enter your choice (1-5):"))

if choice == 1:
    result = input_string.upper()
    print("Uppercase:",result)
elif choice == 2:
    result = input_string.lower()
    print("Lowercase:", result)
elif choice == 3:
    start = int(input("start: "))
    end = int(input("End: "))
    result = input_string[start:end]
    print("Sliced string:", result)
elif choice ==4:
    length = len(input_string)
    print("String length:", length)
elif choice == 5:
    print("Characters:")
    for char in input_string:
        print(char)
else:
    print("invalid choice")

    

