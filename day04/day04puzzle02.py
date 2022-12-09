# Imports
import re

# Import the .txt input file and save it as a file
with open("input_day04.txt") as f:
    # Save each line of the .txt file as a string including new line character \n
    lines = f.readlines()

# Iterate through the above lines and use the .strip() method to remove
# whitespace characters such as \n causing each iteration to output a string
# of characters "22-65,22-66" returned as a list.
input_list = [l.strip() for l in lines]

# Initialise duplicate allocations counter
duplicates = 0

# Loop through input_list and converts allocated job pairs into set objects.
# The set method (isdisjoint) is used to check whether the job allocations
# overlap at all. It will return True if no overlap, otherwise return False.
# If overlapping sets are found, increment duplicates tally
for i in input_list:

    # Uses the re.split() method to split strings on both the "-" and ","
    # characters simultaneously to return a list of 4 strings ["22", "65", "22", "66"]
    allocations = (re.split("-|,", i))

    # Uses the range method to convert the job allocations into sets of all
    # allocated jobs inclusive of the last element.
    job1 = set(range(int(allocations[0]), int(allocations[1]) + 1))
    job2 = set(range(int(allocations[2]), int(allocations[3]) + 1))

    # Compares the two allocated pairs for any overlap and if found, increment
    # the duplicates counter. .isdisjoint will return True if no overlap and
    # False if there are any overlaps, so need to add not to reverse if statement
    if not job1.isdisjoint(job2):
        duplicates += 1

# Print the final duplicates score
print(duplicates)
