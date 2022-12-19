# Imports
from collections import defaultdict

# Import the .txt input file and save it as a file
with open("input_day07.txt") as f:
    # Save each line of the .txt file as a string including new line character \n
    lines = f.readlines()

# Iterate through the above lines and use the .strip() method to remove
# whitespace characters such as \n causing each iteration to output a string
# of characters 'move 1 from 5 to 8' returned as a list.
input_list = [l.strip().split() for l in lines]

# Set the current current working directory to a blank list, so folders can be
# added to the list as elements, and then the list joined together with "/" to
# build the full file path for the current working directory
cwd = []

# Intialise foldersize with defaultdict so if any keys have not yet been assigned
# values will automatically be assigned a value of 0
foldersize = defaultdict(int)

# Loop through the inputs
for i in input_list:
    # If the input is a change directory command, will update the cwd list to
    # update the file path
    if i[0] == "$" and i[1] == "cd":
        # If "$ cd ..", then remove the last element of cwd as moving up one folder
        if i[2] == "..":
            cwd.pop()
        # Otherwise, add the folder to cwd, as will be changing directory to the
        # new folder
        else:
            cwd.append(i[2])
    # If the input is not a command line command starting with "$", and not a
    # folder starting with "dir", then it is a file. Therefore will need to add
    # the file size to the foldersize dictionary. However, all parent folders
    # will also need the file size added to them, so will need to increment the
    # file path directory to the cwd using path
    elif i[0] != "$" and i[0] != "dir":
        # Set the path to be a blank list, this will gradually build into the cwd, so that
        # with each increment towards the full file path, file sizes can be added to each
        # increment path. This is so the filesize of a file found in the cwd can be added
        # to all the parent folders
        path = []

        # Loop through the folders in the cwd
        for j in cwd:
            # For each iteration, add the folder to the path list
            path.append(j)
            # Add the file size to the current path
            foldersize["/".join(path)] += int(i[0])

# Initialise the total_space of the device to 70000000
total_space = 70000000
# Initialise the req_space for the update to 30000000
req_space = 30000000
# Amount of free space currently on device is total_space - used_spaced
free_space = total_space - foldersize["/"]
# Target space required with deleting folders
target_space = req_space - free_space

# Set the del_folder to an empty list to hold all the candidate folders suitable
# for deletion based on their size
del_folder = []


# Loop through the foldersize dictionary
for folder in foldersize:
    # If the foldersize is larger than the required target space, add the folder's
    # size to the del_folder list
    if foldersize[folder] > target_space:
        del_folder.append(foldersize[folder])

# Sort the del_folder list in ascending order
del_folder.sort()
# Print the size of the smallest folder to delete
print(del_folder[0])
