import os
import sys
import re

# open input file
with open(os.path.join(sys.path[0], "input.txt"), 'r') as input_file:
    content = input_file.read().replace('\n', '')

# initialize variables
result = 0
enabled = True

# Extract all `mul(X,Y)`, `do()`, `don't()` in the content
matches = re.findall(r'mul\((\d+),(\d+)\)|(do)\(\)|(don\'t)\(\)', content)

for match in matches:
    if enabled and match[0] and match[1]:
        result += int(match[0]) * int(match[1])
    elif match[2] == 'do':
        enabled = True
    elif match[3]:
        enabled = False

print(result) # print sum of multiplications
