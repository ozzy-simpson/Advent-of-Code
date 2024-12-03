import os
import sys
import re

# open input file
with open(os.path.join(sys.path[0], "input.txt"), 'r') as input_file:
    content = input_file.read().replace('\n', '')

# initialize variables
result = 0

# Extract all `mul(X,Y)` from the line
matches = re.findall(r'mul\((\d+),(\d+)\)', content)

# Perform multiplications, add them to the result
for mul in matches:
    result += int(mul[0]) * int(mul[1])

print(result) # print sum of multiplications
