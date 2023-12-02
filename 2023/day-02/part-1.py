import os
import sys
import re

# open input file
input = open(os.path.join(sys.path[0], "input.txt"), 'r')
lines = input.readlines()
lines = [line.replace('\n', '') for line in lines] # remove newlines

sum = 0 # initialize sum of ids

limits = {
    "red": 12,
    "blue": 14,
    "green": 13
}

for line in lines:

    # split at ": "
    line = line.split(': ')
    game = line[0].split(' ')[1]

    # divide sets
    sets = line[1].split('; ')
    
    # determine if set is valid
    valid = True
    for set in sets:
        # split at " "
        set = set.split(', ') # separates colors
        for color in set:
            colorInfo = color.split(' ')
            if int(colorInfo[0]) > limits[colorInfo[1]]:
                valid = False
                break

    if valid:
        sum += int(game)

# print results
print('Sum of all possible game IDs: ' + str(sum))
