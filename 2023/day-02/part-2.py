import os
import sys
import re

# open input file
input = open(os.path.join(sys.path[0], "input.txt"), 'r')
lines = input.readlines()
lines = [line.replace('\n', '') for line in lines] # remove newlines

sum = 0 # initialize sum of powers

for line in lines:
    # initialize minimums needed for each color
    mins = {
        "red": 0,
        "blue": 0,
        "green": 0
    }

    # split at ": "
    line = line.split(': ')
    game = line[0].split(' ')[1]

    # divide sets
    sets = line[1].split('; ')
    
    # determine minimums needed for each color
    for set in sets:
        # split at " "
        set = set.split(', ') # separates colors
        for color in set:
            colorInfo = color.split(' ')
            if int(colorInfo[0]) > mins[colorInfo[1]]:
                mins[colorInfo[1]] = int(colorInfo[0])

    power = mins['blue'] * mins['red'] * mins['green'] # power is product of minimums
    sum += power # add power to sum

# print results
print('Sum of powers: ' + str(sum))
