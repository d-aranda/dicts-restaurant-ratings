"""Restaurant rating lister."""

import sys
terminal_filename = sys.argv[1]

file = open(terminal_filename)

scores = {}

for line in file:
    line = line.rstrip()
    restaurant, rating = line.split(":")
    scores[restaurant] = rating
    
    # sorted_scores = sorted(scores.items())

user_restaurant = input(f"Enter New Restaurant: ")
user_score = input(f"Enter {user_restaurant} Score: ")
scores[user_restaurant.capitalize()] = user_score



for key, value in sorted(scores.items()):
    print(f"{key} is rated at {value}")



