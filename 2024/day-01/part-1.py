import os
import sys
import re

# open input file
input = open(os.path.join(sys.path[0], "input.txt"), 'r')
lines = input.readlines()

# initialize variables
result = 0
left, right = [], []

# Add to left and right lists
for line in lines:
    # split line into left and right (separated by spaces)
    l, r = re.split(r'\s+', line.strip())

    # add to lists
    left.append(int(l.strip()))
    right.append(int(r.strip()))

# Sort lists
left.sort()
right.sort()

# Calculate sum of distances between pairs
result = sum(abs(l - r) for l, r in zip(left, right))

print(result) # print sum of distances
