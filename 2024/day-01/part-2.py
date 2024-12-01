import os
import sys
import re
from collections import Counter

# open input file
input = open(os.path.join(sys.path[0], "input.txt"), 'r')
lines = input.readlines()

# initialize variables
result = 0
left, right = [], Counter()

# Add to left and right lists
for line in lines:
    # split line into left and right (separated by spaces)
    l, r = re.split(r'\s+', line.strip())

    # append to left list
    left.append(int(l.strip()))
    
    # increase multiplier by 1
    right[int(r.strip())] += 1

# Calculate similarity scores
result = sum(l * right[l] for l in left if l in right)

print(result) # print sum of distances
