# Import the .txt input file and save it as a file
with open("input_day06.txt") as f:
    # Save each line of the .txt file as a string including new line character \n
    lines = f.readlines()

# When lines is imported and read, it saves each line as a separate element of
# a list. Since there is only one line in the input file, converting the list to
# a string makes easier handling
lines = lines[0]

# Initialise the start_packet_pos to 0
start_packet_pos = 0

# Initialise the loop counter to 0
i = 0
# Loop through each character of lines
while i < len(lines):
    # Convert 4 characters at a time into a set and then check their length. If
    # there are repeating characters, then the length will reduce and no longer
    # be equal to the original length (4). When the first occurence of 4 unique
    # characters in a row is found, the if statement will be true
    if len(set(lines[i:i+4])) == len(lines[i:i+4]):
        # Update the start packet position to be 4 positions after i. Python
        # indexes at 0, but the packet position is indexed at 1, so need to +4
        # instead of +3
        start_packet_pos = i + 4
        # Break out of the loop
        break
    else:
        # Increment the loop counter if starter packet not found
        i += 1

# Print the start packet position
print(start_packet_pos)
