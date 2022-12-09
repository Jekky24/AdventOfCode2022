# Import the .txt input file and save it as a file
with open("input_day05.txt") as f:
    # Save each line of the .txt file as a string including new line character \n
    lines = f.readlines()

# Iterate through the above lines and use the .strip() method to remove
# whitespace characters such as \n causing each iteration to output a string
# of characters 'move 1 from 5 to 8' returned as a list.
input_list = [l.strip() for l in lines]

# Set up the crate piles as a dictionary, with each pile stored as a list so
# that the last (top) crate can be removed with .pop and added to another pile
# with .append
piles = {
    "1": ["B", "Z", "T"],
    "2": ["V", "H", "T", "D", "N"],
    "3": ["B", "F", "M", "D"],
    "4": ["T", "J", "G", "W", "V", "Q", "L"],
    "5": ["W", "D", "G", "P", "V", "F", "Q", "M"],
    "6": ["V", "Z", "Q", "G", 'H', "F", "S"],
    "7": ["Z", "S", "N", "R", "L", "T", "C", "W"],
    "8": ["Z", "H", "W", "D", "J", "N", "R", "M"],
    "9": ["M", "Q", "L", "F", "D", "S"]
}

# Loop through the input list to:
# 1. Remove all the words and return a list of numerical instructions stored
#    as a list ["1", "7", "4"]
# 2. Move the crates according to the numerical instructions
for i in input_list:
    # i.split() will return a list of the words ['move', '1', 'from', '7', 'to', '4']
    # Splicing is used to obtain every second element starting from the second
    # element [1::2], which will give a list of the numerical instructions
    # ["1", "7", "4"]
    instructions = (i.split()[1::2])

    # Number 1: number of crates to move. Converted to integer as it will be
    # used in calculations
    num_crates = int(instructions[0])
    # Number 2: pile to move from, left as string to use in dictionary indexing
    from_pile = instructions[1]
    # Number 3: pile to move to, left as string to use in dictionary indexing
    to_pile = instructions[2]

    # The crates being moved will be copied into their new pile using .extend
    # from the old pile. The number of crates being moved will is calculated
    # using len(piles[from_pile])-num_crate to splice the crates to the end
    # of the pile
    piles[to_pile].extend(piles[from_pile][len(piles[from_pile])-num_crates:])

    # The crates that have been moved will need to be deleted from their old pile
    # using del function. The crates that have been moved will be indexed using
    # len(piles[from_pile] - num_crates to splice the crates to the end of the
    # pile
    del piles[from_pile][len(piles[from_pile])-num_crates:]

# Print the final piles arrangement with each pile on a new line
for i in piles:
    # Print with formatted string literals
    print(f"{i}: {piles[i]}")
