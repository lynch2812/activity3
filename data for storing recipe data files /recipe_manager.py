# title = Chicken wings and rice 
# ingredients - (chcken wings, franks hot sauce, rice, pepper  )
# instructions - maranade the chicken/ put them in the air fryer/ start the rice/ 
# finish the chicken wings/ serve the rice 


# interacts with the operating system, this checks where the recipes are stored (recipes.txt)
import os

# File where recipes are stored on the Operating system
RECIPES_FILE = "recipes.txt"

# Function to load recipes from the file, it checks if the file exists, if it exists it opens the file in read mode ('r')reading all the lines
# each line represents a recipe. We use line.strip () which makes sure there is no spaces when printed. line is just a word that 
# can be used for xplaining the string 
def load_recipes():
    if os.path.exists(RECIPES_FILE):
        with open(RECIPES_FILE, 'r') as file:
            return [line.strip() for line in file.readlines()]
    return []

# Function to save recipes to the file
def save_recipes(recipes):
    with open(RECIPES_FILE, 'w') as file:
        for recipe in recipes:
            file.write(f"{recipe}\n")

# Function to add a recipe
def add_recipe():
    name = input("Enter the name of the recipe: ")
    ingredients = input("Enter the ingredients (comma separated): ")
    instructions = input("Enter the instructions: ")
    recipe = f"Recipe: {name}\nIngredients: {ingredients}\nInstructions: {instructions}"
    
    recipes = load_recipes()
    recipes.append(recipe)
    save_recipes(recipes)
    print("Recipe added successfully.")

# Function to view all recipes
def view_recipes():
    recipes = load_recipes()
    if recipes:
        for i, recipe in enumerate(recipes, start=1):
            print(f"\nRecipe {i}:")
            print(recipe)
    else:
        print("No recipes available.")

# Function to search for a recipe by name
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

# Function to edit a recipe
def edit_recipe():
    name = input("Enter the recipe name to edit: ")
    recipes = load_recipes()
    for i, recipe in enumerate(recipes):
        if name.lower() in recipe.lower():
            print(f"Editing Recipe: {recipe}")
            new_ingredients = input("Enter new ingredients (comma separated): ")
            new_instructions = input("Enter new instructions: ")
            updated_recipe = f"Recipe: {name}\nIngredients: {new_ingredients}\nInstructions: {new_instructions}"
            recipes[i] = updated_recipe
            save_recipes(recipes)
            print("Recipe updated successfully.")
            return
    print("Recipe not found.")

# Function to delete a recipe
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
