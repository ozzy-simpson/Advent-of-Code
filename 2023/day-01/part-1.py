import os
import sys
import re

# open input file
input = open(os.path.join(sys.path[0], "input.txt"), 'r')
lines = input.readlines()

sum = 0 # initialize sum of calibration values

for line in lines:
    # remove non numeric characters using regex
    line = re.sub('[^0-9]', '', line)

    # add number to sum
    sum += int(line[0] + line[-1])

# print results
print('Sum of all calibration values: ' + str(sum))
