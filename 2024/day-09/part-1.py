import os
import sys
from itertools import combinations

# open input file
with open(os.path.join(sys.path[0], "input.txt"), 'r') as input_file:
    lines = input_file.read()

# initialize variables
filesystem = []
currentFile = 0

# create filesystem
for i, c in enumerate(lines):
    freeSpace = (i % 2 == 1)
    if freeSpace:
        # Add c number of '.' to the filesystem
        for _ in range(int(c)):
            filesystem.append('.')
    else:
        # Add c number of currentFile to the filesystem
        for _ in range(int(c)):
            filesystem.append(currentFile)
        
        # Increment currentFile
        currentFile += 1

print(filesystem)

# consolidate filesystem by moving elements from the end to the first '.'
for i in range(len(filesystem)):
    if filesystem[i] == '.':
        for j in range(len(filesystem) - 1, i, -1):
            if filesystem[j] != '.':
                filesystem[i], filesystem[j] = filesystem[j], filesystem[i]
                break

print(filesystem)

# calculate checksum
checksum = 0
for i, file in enumerate(filesystem):
    if file != '.':
        checksum += i * int(file)

print(checksum)
