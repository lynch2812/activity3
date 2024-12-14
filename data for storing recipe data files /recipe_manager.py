# title = Chicken wings and rice 
# ingredients - (chcken wings, franks hot sauce, rice, pepper  )
# instructions - maranade the chicken/ put them in the air fryer/ start the rice/ 
# finish the chicken wings/ serve the rice 


# interacts with the operating system, this checks where the recipes are stored (recipes.txt)
import os

# File where recipes are stored on the Operating system
RECIPES_FILE = "recipes.txt"

# Function to load recipes from the file, it checks if the file exists (true or false),
#  if it exists it opens the file in read mode ('r')reading all the lines
# open with(...)  ensures that the file is automatically closed after reading, 
# with the file variable being used to access the contents of the file 
#file.read() reads all the contents as a single string and \n\n creates a double gap 
# and block of code so as to create each recipe with instructions etc as one recipe
# strip removes any extra spaces or newline characters around each block making each recipe one neat string

# in simple terms 
#How It All Works Together:
#Check if the file exists: It looks for the file where recipes should be stored.
#Read the file content: If the file exists, it opens the file and reads everything in it.
#Split into recipes: It splits the content into blocks (each block represents a recipe) and strips away extra spaces.
#Return the recipes: It returns the list of recipes as separate strings in a list.
#If file doesn't exist: It returns an empty list so your program doesn’t break.


def load_recipes():
    if os.path.exists(RECIPES_FILE):
        with open(RECIPES_FILE, 'r') as file:
            return [line.strip() for line in file.read().split('\n\n')]
    return []

#The save_recipes function saves all recipes to a file and overwrites any existing content.
#'w' opens the file in write mode:
#If the file doesn’t exist, it creates a new file.
#If the file already exists, it clears its content before writing.
#For each recipe in the recipes list:
#The function writes the recipe to the file, adding a new line after each one using file.write(f"{recipe}\n").
#\n ensures that each recipe is written on its own line.
#It does not check for duplicates or return anything.
#It simply replaces the file content with the updated recipes list

# explanation below for the steps above

# The save_recipes function saves recipes to a file and overwrites any existing content. 
# It uses 'w' to open the file in write mode, creating the file if it doesn’t exist. 
# For each recipe in the list, it writes the recipe to the file, adding a new line (\n) after each one. 
# The function completely replaces the file content with the updated recipes list.
def save_recipes(recipes):
    with open(RECIPES_FILE, 'w') as file:
        for recipe in recipes:
            file.write(f"{recipe}\n")




# Function to add a recipe to the file 
# Asks the user to enter the answers for the sections 
# recipe = then combines the answers the user has entered and creates a string with the answers 
# loads the existing recipes from the file using load_recipes 
# adds it to the list, using recipes.append(recipe)
# saves the list with the new recipe added using asave_recipes()
# prints message saying it was added succesfully 
def add_recipe():
    name = input("Enter the name of the recipe: ")
    ingredients = input("Enter the ingredients (comma separated): ")
    instructions = input("Enter the instructions: ")
    recipe = f"Recipe: {name}\nIngredients: {ingredients}\nInstructions: {instructions}"
    
    recipes = load_recipes()
    recipes.append(recipe)
    save_recipes(recipes)
    print("Recipe added successfully.")

# Function calls 'load_recipes' to display all the recipes 
# looping through the recipes and printing each recipe
# the system prints the recipes displayed for example  (e.g recipe1, recipe2) using the enumerate function 
# i as the variable used to makesure the it numbers the list but i could be anything, although it is commonly used
# if a recipe doesnt exist it prints "No recipes avalable"
def view_recipes():
    recipes = load_recipes()
    if recipes:
        for i, recipe in enumerate(recipes, start=1):
            print(f"\nRecipe {i}:")
            print(recipe)
    else:
        print("No recipes available.")



# finds and displays a recipe by name 
#What it does: Finds and displays a recipe by name.
# Steps:
# uses the name variable and to allow the user to type the name of the recipe they are searching for 
# this then saves the recipe to the name variable
# recipes = load_recipes() is used to call the list of saved recipes 
# found = false is a flag ( a variable that keeps track if it is found or not) initially it is found as false 
# for 'recipe in recipes' looks at each recipe in the recipes list 1 by 1 looping through each in the file 
# it then checks if name is IN recipe and makes the comparison case insensitive
# if it matches then the program moves to the next step
# the next step is to print the recipe the found flag turns to true and then break to stop the loop, 
# if not found it generates the message recipe not found



def search_recipe():
    name = input("Enter the recipe name to search for: ")
    recipes = load_recipes()
    found = False
    for recipe in recipes:
        if name.lower() in recipe.lower():
            print(f"\nFound Recipe: {recipe}")
            found = True
            break
    if not found:
        print("Recipe not found.")





# Function to edit a recipes ingredients and instructions 
# 
def edit_recipe():
    name = input("Enter the recipe name to edit: ") # asks the user to type the name of the recipe to edit 
    recipes = load_recipes() # Loads the file from load_recipes 
    for i, recipe in enumerate(recipes): # i makes sure that recipes is numbered when put in list form
        if name.lower() in recipe.lower():# checks if the name is case-insensitive
            print(f"Editing Recipe: {recipe}")# if the recipe is found it prints the current versions name.
            new_ingredients = input("Enter new ingredients (comma separated): ")# asks the user to enter the new ingredients 
            new_instructions = input("Enter new instructions: ") # asks the user to enter the new instructions
            updated_recipe = f"Recipe: {name}\nIngredients: {new_ingredients}\nInstructions: {new_instructions}" # updates the old recipe with the new one and prints it out
            recipes[i] = updated_recipe # i as the variable used to make the items are listed numerically 
            save_recipes(recipes) # saves recipes for the updated list 
            print("Recipe updated successfully.") # prints when recipe is updated succesfully 
            return
    print("Recipe not found.") # prints if recipe not found 

# Function to delete a recipemove recipe from the file
def delete_recipe():
    name = input("Enter the recipe name to delete: ")
    recipes = load_recipes()
    for i, recipe in enumerate(recipes):
        if name.lower() in recipe.lower():
            del recipes[i]
            save_recipes(recipes)
            print("Recipe deleted successfully.")
            return
    print("Recipe not found.")

# Main menu for the Recipe Manager
def main():
    while True:
        print("\nRecipe Manager")
        print("1. Add Recipe")
        print("2. View Recipes")
        print("3. Search Recipe")
        print("4. Edit Recipe")
        print("5. Delete Recipe")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_recipe()
        elif choice == '2':
            view_recipes()
        elif choice == '3':
            search_recipe()
        elif choice == '4':
            edit_recipe()
        elif choice == '5':
            delete_recipe()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
