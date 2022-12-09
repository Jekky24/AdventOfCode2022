# Import the .txt input file and save it as a file
with open("input_day03.txt") as f:
    # Save each line of the .txt file as a string including new line character \n
    lines = f.readlines()

# Iterate through the above lines and use the .strip() method to remove
# whitespace characters such as \n causing each iteration to output a string
# of characters "abc" returned as a list.
input_list = [l.strip() for l in lines]

# Initialise total_priority to 0
total_priority = 0

# Lists all the priority values for each item in a dictionary so they can be
# looked up later
priority = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8,
            "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15,
            "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22,
            "w": 23, "x": 24, "y": 25, "z": 26, "A": 27, "B": 28, "C": 29,
            "D": 30, "E": 31, "F": 32, "G": 33, "H": 34, "I": 35, "J": 36,
            "K": 37, "L": 38, "M": 39, "N": 40, "O": 41, "P": 42, "Q": 43,
            "R": 44, "S": 45, "T": 46, "U": 47, "V": 48, "W": 49, "X": 50,
            "Y": 51, "Z": 52}

# Loop through input_list and look at 3 rows at a time. Each elf's items are
# converted from a string object to a set object. Items that are common to all
# 3 elves are found using the set method intersection (&) and their priority
# scores are added to the total priority score
# Initialise loop counter at 0
i = 0
while i < len(input_list):
    # Look at 3 rows at a time and convert the strings in each row to set objects
    elf1 = set(input_list[i])
    elf2 = set(input_list[i+1])
    elf3 = set(input_list[i+2])

    # Identify items that are common to all 3 elves using intersection (&)
    # method of set objects. The "".join method is used to convert the returned
    # set objects back to to a string. The resulting string is then used to look
    # up its priority value using the priority dictionary, and the total priority
    # score is tallied up
    total_priority += priority["".join(elf1 & elf2 & elf3)]

    # Increment loop counter
    i += 3

# Print the final total priority score
print(total_priority)
