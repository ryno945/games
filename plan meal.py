import pandas as pd
from random import choice

# Define a list of meals
breakfasts = ["Cereal", "Toast", "Eggs", "Fruit"]
lunches = ["Sandwich", "Salad", "Soup", "Pasta"]
dinners = ["Chicken", "Fish", "Vegetarian", "Beef"]

# Create a DataFrame to hold the meal plan
meal_plan = pd.DataFrame(columns=["Day", "Breakfast", "Lunch", "Dinner"])

# Generate the meal plan for the next 14 days
for i in range(14):
    breakfast = choice(breakfasts)
    lunch = choice(lunches)
    dinner = choice(dinners)
    meal_plan.loc[i] = [f"Day {i+1}", breakfast, lunch, dinner]

# Print the meal plan
print(meal_plan)
