"""Restaurant rating lister."""

file = open("scores.txt")

scores = {}

for line in file:
    line = line.rstrip()
    restaurant, rating = line.split(":")
    scores[restaurant] = rating
    
    # sorted_scores = sorted(scores.items())


for key, value in scores.items():
    print(f"{key} is rated at {value}")



