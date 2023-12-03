import os
import sys
import re

# open input file
input = open(os.path.join(sys.path[0], "input.txt"), 'r')
lines = input.readlines()
lines = [line.replace('\n', '') for line in lines] # remove newlines

# initialize sum of part numbers, list of numbers, and list of symbols
sum = 0
nums = []
symbols = []

# Parse
for row, line in enumerate(lines):
    i = 0
    while i < len(line):
        if line[i].isdigit():
            # found start of number, find end
            start = i
            while i+1 < len(line) and line[i+1].isdigit():
                i += 1
            num = int(line[start:i+1])
            nums.append((num, tuple((row, col) for col in range(start, i+1)))) # add number and coordinates to list
        elif line[i] != ".":
            # found symbol
            symbols.append((line[i], (row, i))) # add symbol and coordinates to list
        i += 1

# Add numbers to sum if they are next to/diagonal to a symbol
for num in nums:
    # Iterate through coordinates of number
    for numCoord in num[1]:
        # Iterate through symbols
        for symbol in symbols:
            # Check if number is next to/diagonal to symbol
            if abs(numCoord[0] - symbol[1][0]) <= 1 and abs(numCoord[1] - symbol[1][1]) <= 1:
                sum += num[0]
                break
        else:
            continue
        break

# print results
print('Sum of all part numbers: ' + str(sum))
