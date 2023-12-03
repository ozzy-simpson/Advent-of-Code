import os
import sys
import re

# open input file
input = open(os.path.join(sys.path[0], "input.txt"), 'r')
lines = input.readlines()
lines = [line.replace('\n', '') for line in lines] # remove newlines

# initialize sum of part numbers, list of numbers, and list of gears
sum = 0
nums = []
gears = []

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
        elif line[i] == "*":
            # found gear
            gears.append((line[i], (row, i))) # add gear and coordinates to list
        i += 1

for gear in gears:
    countNums = 0
    ratio = 1
    for num in nums:
        # Iterate through coordinates of number
        for numCoord in num[1]:
            # Check if number is next to/diagonal to gear
            if abs(numCoord[0] - gear[1][0]) <= 1 and abs(numCoord[1] - gear[1][1]) <= 1:
                countNums += 1 # increment count of numbers next to gear
                ratio *= num[0] # multiply number to ratio
                break
    if countNums == 2:
        # Two numbers are adjacent to a gear, add ratio to sum
        sum += ratio

# print results
print('Sum of all gear ratios: ' + str(sum))
