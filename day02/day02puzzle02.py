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

# Lists all the potential scenarios and the points gained for each as a
# dictionary, so the scenarios can be looked up later
# Opponent plays: A Rock, B Paper, C Scissors
# X Lose (+0), Y Draw (+3), Z Win (+6)
# Extra points for option selected: Rock (+1), Paper (+2), Scissors (+3)
scenarios = {
    "A X": 3,   # Rock + Scissors
    "A Y": 4,   # Rock + Rock
    "A Z": 8,   # Rock + Paper
    "B X": 1,   # Paper + Rock
    "B Y": 5,   # Paper + Paper
    "B Z": 9,   # Paper + Scissors
    "C X": 2,   # Scissors + Paper
    "C Y": 6,   # Scissors + Scissors
    "C Z": 7,   # Scissors + Rock
}

# Loop through input_list and tally scores gained based on scenario
for i in input_list:

    # Adds to the score by looking up the scenario dictionary
    score += scenarios[i]

# Print the final score
print(score)
