# Import the .txt input file and save it as a file
with open("input_day01.txt") as f:
    # Save each line of the .txt file as a string including new line character \n
    lines = f.readlines()

# Iterate through the above lines and use the .strip() method to remove whitespaces
# causing each iteration to output a string of numbers '123', '123', '123' which will be returned as a list
# Empty rows will be an empty element. ie ''
input_list = [l.strip() for l in lines]

totals = []
ind = 0
combined_calories = 0
for i in input_list:
    if i != '':
        combined_calories += int(i)
    else:
        totals.append(combined_calories)
        combined_calories = 0

totals.sort(reverse=True)
print(totals[0] + totals[1] + totals[2])