# Highest Score: Write a program that print the highest score from a list of scores.

scores = [90, 60, 70, 75, 89, 34, 65, 99, 23, 10]

# First Approach
highest_score = 0
for score in scores:
    if score > highest_score:
        highest_score = score

print(highest_score)

# Second Approach 
print(max(scores))