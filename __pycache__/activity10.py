#Project Frequency Counter 
#Create a Python script that counts the frequency of words in a given text using dictionaries, 
# conditional sentences, loops, and recursive functions.
#nstructions:

#1. Create a function that takes a string of text as input.
def word_frequency (goal): 
    if not goal:   
        return {}
    goal = goal.upper().replace(",", "").replace(".", "").replace("!", "").replace("?", "!!!!!")
# splitting the words in to a format we want to use
    words = goal.split()
        
        #word frequency 
    frequency_used = {}
     # recursive process 
    def word_process(words,index):
         if index == len(words):
            return
         # gets the current word 
         word = words[index]

         
         if word in frequency_used: 
                frequency_used [word] += 1 
         else:
                frequency_used [word] = 1 
# recursive call to  process the next word 
         word_process(words, index + 1)

    word_process(words, 0)
        
    return frequency_used


goal = "goal at the Riverside stadium!, goal at vicarage road!, penalty at Stamford Bridge! will it be scored?, red card at loftus road!"

goal_frequency = word_frequency(goal)

for word, count in goal_frequency.items():
 print(f"{word}: {count}")





#2. Use a dictionary to store the frequency of each word in the text.

#3. Use conditional sentences to handle special cases (e.g., empty input).

#4. Use loops to iterate over the words in the text.

#5. Use a recursive function to process the text and update the word frequency dictionary.

#"goal at the Riverside stadium!, goal at vicarage road!, penalty at Stamford Bridge! will it be scored?, red card at loftus road!"