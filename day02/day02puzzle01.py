# Import the .txt input file and save it as a file
with open("input_day02.txt") as f:
    # Save each line of the .txt file as a string including new line character \n
    lines = f.readlines()

# Iterate through the above lines and use the .strip() method to remove
# whitespace characters such as \n causing each iteration to output a string
# of characters "A X" returned as a list.
input_list = [l.strip() for l in lines]

# Initialise score at 0
score = 0

# Lists
# A Rock, B Paper, C Scissors
# X Rock, Y Paper, Z Scissors
win_scenarios = ["A Y", "B Z", "C X"]
draw_scenarios = ["A X", "B Y", "C Z"]

# Extra points for option selected
# 1 for Rock, 2 for Paper, 3 for Scissors
extra_points = {"X": 1, "Y": 2, "Z": 3}

# Loop through input_list
for i in input_list:
    # If round is won, add 6 to score
    if i in win_scenarios:
        score += 6
    # If round is draw, add 3 to score
    elif i in draw_scenarios:
        score += 3

    # Add bonus points for option selected
    score += extra_points[i[-1]]

# Print the final score
print(score)
