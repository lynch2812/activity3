# 1. Create tuples to store student information (name, age, grade).

# 2. Use tuple methods to count and index elements.

# 3. Create sets to store unique student IDs and courses.

# 4. Perform set operations like union, intersection, and difference.

# 5. Use frozen sets to create immutable sets of student data.

#setting up the pupil tuples for the list 
footballer1 = ("Lewis", 16, "GK")
footballer2 = ("Craig", 14, "DEF")
footballer3 = ("Mark", 15, "DEF/Captain")
footballer4 = ("Darren", 18, "MID")
footballer5 = ("Gary", 17, "MID")
footballer6 = ("Luke", 18, "FWD")

# pulls the information from the Pupils 
footballers = (footballer1,footballer2,footballer3,footballer4,footballer5,footballer6)

# using the information 
print(f"Footballers involved: {len(footballers)}") # answer should be 6 
print(f"Captains shirt number: {footballers.index(footballer3)}") #answer should be 2 

# creating sets for goals scored per game and who has scored them 
goals_scored = {4,5,3,5,6}
scorers = {"Lewis", "Craig", "Lewis and Gary", "Mark, Darren and Luke", "Craig and Mark", "Gary,Mark and Luke"}

# print out the answers 
print(f"Goals scored: {goals_scored}")
print(f"Scorers: {scorers}")





