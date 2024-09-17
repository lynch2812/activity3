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

# creating sets for goals scored per season and who has scored the most
goals_scored = {4,5,3,5,6,1}
scorers = {"Lewis", "Craig", "Gary", "Darren", "peter", "Gary"}

# print out the answers 
print(f"Goals scored: {goals_scored}")
print(f"Scorers: {scorers}")

# New scorer added to list  from below updating it using .update 
new_scorer = {"Harry, Lucifer"}
scorers.update(new_scorer)
print(f"New Scorer added:{scorers}")
scorers.remove("Gary")
print(f"Mistake made, scorer taken out: {scorers}")
#Frozen set confirming theses goals have ben scored 
confirmedgoals= frozenset(goals_scored)
print(f"Confirmed goals scored:{confirmedgoals}")

# confirmedgoals.add(10) - if this comment note is taken away it will create an error as it is a frozen ist object 

confirmed_scorers = frozenset(scorers)
print(f" The confirmed scorers are in: {confirmed_scorers}")

## completed the activity 








