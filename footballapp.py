# Import necessary libraries
import requests
import pandas as pd

# Placeholder function to fetch results (replace this with real API calls or web scraping)
def fetch_results()):
    # Example of hardcoded results (replace with actual results)
    results = {
        "Match 1": "Team A vs Team B - 2:1",
        "Match 2": "Team C vs Team D - 1:1",
        "Match 3": "Team E vs Team F - 0:3",
        "Match 4": "Team G vs Team H - 2:2",
        "Match 5": "Team I vs Team J - 1:0",
    }
    return results

# Function to get user predictions
def get_user_predictions():
    user_name = input("Enter your name: ")
    predictions = {}
    for i in range(1, 6):
        match = input(f"Enter prediction for Match {i} (e.g., 'Team A vs Team B - 2:1'): ")
        predictions[f"Match {i}"] = match
    return user_name, predictions

# Function to calculate scores
def calculate_scores(predictions, actual_results):
    score = 0
    for match, prediction in predictions.items():
        if prediction == actual_results[match]:
            score += 3
    return score

# Main function to run the predictor
def football_predictor():
    # Fetch actual results (replace with real-time fetching)
    actual_results = fetch_results()
    
    # List to store users and their scores
    leaderboard = []
    
    # Number of users (for demo purposes, fixed to 2 users)
    num_users = 2  # You can change this to any number of users
    
    # Get predictions and calculate scores for each user
    for _ in range(num_users):
        user_name, user_predictions = get_user_predictions()
        score = calculate_scores(user_predictions, actual_results)
        leaderboard.append({"Name": user_name, "Score": score})
    
    # Sort the leaderboard by scores in descending order
    leaderboard = sorted(leaderboard, key=lambda x: x['Score'], reverse=True)
    
    # Display the leaderboard
    print("\nLeaderboard:")
    for i, user in enumerate(leaderboard, 1):
        print(f"{i}. {user['Name']} - {user['Score']} points")
    
    # Display the predictions table
    print("\nPredictions for the week:")
    for user in leaderboard:
        print(f"{user['Name']}'s predictions:")
        for match, prediction in user_predictions.items():
            print(f"{match}: {prediction}")
        print()  # Blank line for better readability

# Run the football predictor
if __name__ == "__main__":
    football_predictor()
