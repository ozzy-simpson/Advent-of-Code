import os
import sys
import re

# open input file
input = open(os.path.join(sys.path[0], "input.txt"), 'r')
lines = input.readlines()

sum = 0 # initialize sum of calibration values

# map spellings to numbers, include first/last letters to account for overlapping spellings (eighthree = 83)
spellings = {
    'one': "o1e",
    'two': "t2o",
    'three': "t3e",
    'four': "f4r",
    'five': "f5e",
    'six': "s6x",
    'seven': "s7n",
    'eight': "e8t",
    'nine': "n9e"
}

for line in lines:
    # replace spellings with numbers, but in order of appearance
    i = 0
    while (i < len(line)):
        for spelling in spellings:
            if line[i:i+len(spelling)] == spelling:
                line = line[:i] + str(spellings[spelling]) + line[i+len(spelling):]
                break
        i += 1

    # remove non-numeric characters using regex
    line = re.sub('[^0-9]', '', line)

    # add first/last numbers to sum
    sum += int(line[0] + line[-1])

# print results
print('Sum of all calibration values: ' + str(sum))
