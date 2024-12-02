import os
import sys
import re

# open input file
input = open(os.path.join(sys.path[0], "input.txt"), 'r')
lines = input.readlines()

# initialize variables
safe = 0

def isSafe(levels):
    # Check if same direction (ascending or descending)
    if levels != sorted(levels) and levels != sorted(levels, reverse=True):
        return False
    
    # Check if the differences between consecutive levels are within [1, 3]
    return all(1 <= abs(levels[i] - levels[i - 1]) <= 3 for i in range(1, len(levels)))

# Check if line is safe or not
for line in lines:
    # Split line into levels, as integers
    levels = re.split(r'\s+', line.strip())
    levels = list(map(int, levels))

    if isSafe(levels):
        safe += 1
    else:
        # Check if removing a level makes the line safe
        for i in range(len(levels)):
            if isSafe(levels[:i] + levels[i + 1:]):
                safe += 1
                break

print(safe) # print number of safe reports
