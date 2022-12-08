# Import the .txt input file and save it as a file
with open("input_day01.txt") as f:
    # Save each line of the .txt file as a string including new line character \n
    lines = f.readlines()

# Iterate through the above lines and use the .strip() method to remove
# whitespace characters such as \n causing each iteration to output a string
# of numbers '123' returned as a list. Empty rows will be listed as an
# empty element ''
input_list = [l.strip() for l in lines]

# Set totals to be empty list to hold each elf's total snack calories
totals = []

# Set combined_calories to be 0 which accumulate each elf's total calories
combined_calories = 0

# Loop through input_list
for i in input_list:
    # If element is not empty, add the snack's calories to the elf's total
    # combined calories
    if i != '':
        combined_calories += int(i)
    # Otherwise element is empty, meaning moving on to new elf
    else:
        # Append the elf's total combined calories to the totals list
        totals.append(combined_calories)
        # Reset the combined calories accumulator to 0
        combined_calories = 0

# Sort the totals list in descending order
totals.sort(reverse=True)

# Print the sum of the 3 largest combined calories value
print(totals[0] + totals[1] + totals[2])
