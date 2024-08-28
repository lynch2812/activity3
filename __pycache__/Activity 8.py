#Create a list of test scores for a student. Done 
#Use floor division to calculate the average score. Done 
#Use comparison operators to determine the grade based on the average score. Done 
#Use assignment operators to update the student's grade. Done
#Use membership operators to check if a specific score exists in the list of scores.Done 
#Use identity operators to compare objects.
#Use bitwise operators to perform bitwise operations on the scores.

testScores = [21, 25, 95, 88, 51]
results = sum(testScores)
averageResults = len(testScores)
averageAnswer = results // averageResults

# Comparison operator used 
if averageAnswer >= 85:
    grade = "A"
elif averageAnswer >= 75:
    grade = "B"
elif averageAnswer >= 60:
    grade = "c"
elif averageAnswer >= 50:
    grade = "D"
elif averageAnswer >= 35:
    grade = "E"
else:
    grade = "Fail"


# Assignment operator used 
if averageAnswer >= 80:
    grade += "B+"

scoreChecker = 35    
if scoreChecker in testScores:
  print("The score can be found in the list.")

else:
  print("The score cannot be found in the list")

newScores = testScores
if testScores is newScores:
    print("The testScore and NewScore are the same") 
else:
    print("The testScores and newScores are the same")

bitwise_result = testScores[1] & testScores[2]
print(f"Bitwise AND of the first two scores: {bitwise_result}")

# Display the student's grade
print(f"The student's average score is {averageAnswer} and their grade is {grade}.")


print(averageAnswer)
print(grade)
