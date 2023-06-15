"""Restaurant rating lister."""

import sys 
terminal_file = sys.argv[1]


def restaurant_scores(file):
    """Add restaurants: scores in a dictionary"""
    with open(terminal_file) as file:
        scores = {}
        
        for line in file:
            restaurant, rating = line.rstrip().split(":")
            scores[restaurant] = rating
    

        return scores
            
def user_input(scores):
    """Allows users to add restaurant name and score"""

    user_restaurant = input(f"Enter New Restaurant: ")
    user_score = input(f"Enter {user_restaurant} Score: ")
    scores[user_restaurant.capitalize()] = user_score


    return scores 


def print_dict_scores(scores):
    """Prints dict scores"""

    for key, value in sorted(scores.items()):


        print(f"{key} is rated at {value}")





scores1 = restaurant_scores(terminal_file)
user_input(scores1)
print_dict_scores(scores1)






























