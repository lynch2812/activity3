person = {
    'Name' : "Gary",
    'Age' : "20",
    'City' : "Leighton Buzzard"
    
    }


#the .get function can also work like below, a bracket within this and a comma seperated will give the answer if it cannot find in the dictionary as per city below
name = person['Name'] = "john"
age = person['Age']
city =person.get('City', 'unknown city')

print(name)
print(age)
print(city)
# below finds if the name is in the dictionary and prints out your text and the word its loking for
print("name: ", person["Name"])
#Built in methods in dictionaries 
#methods have brackets after them 
# keys() reaturns a list of keys for exampple will return dict_keys(['Name', 'Age', 'City'])
# values() returns a list of values fro eample will return dict_values(['john', '20', 'Leighton Buzzard'])
# items() returns a list of items for exapmle returns dict_items([('Name', 'john'), ('Age', '20'), ('City', 'Leighton Buzzard')])

print(person.keys())
print(person.values())
print(person.items())
# looks up the key in the dictionary
for key in person:
    print(key,person[key])
for key, value in person.items():
    print(key, value)


#copies the dictionary from above and now person becomes mycopy
mycopy=person.copy()

print(mycopy)

items = {
     "price" : "20",
     "location": " Watford"
 }
#dict method, simpler version to copy dictionary over as below 
mycopy=dict(person)

print(mycopy)

