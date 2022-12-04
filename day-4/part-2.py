import re
import os
import sys

# open input file
input = open(os.path.join(sys.path[0], "input.txt"), 'r')
lines = input.readlines()

# initialize variables
count = 0

for line in lines:
    assignment = re.split(',|-', line.strip()) # split on commas and dashes
    assignment = [eval(i) for i in assignment] # convert to int
    
    # create a set of the ranges
    part1 = set(range(assignment[0], assignment[1]+1))
    part2 = set(range(assignment[2], assignment[3]+1))

    # find the intersection
    intersection = part1.intersection(part2)

    # if intersection not empty, add to count
    if intersection:
        count += 1
        

print("Ranges that overlap:", count)