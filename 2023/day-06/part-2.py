import os
import sys
import re
import math

# open input file
input = open(os.path.join(sys.path[0], "input.txt"), 'r')
lines = input.readlines()

# Parse lines
lines = [re.sub('[^0-9 ]', '', line).lstrip() for line in lines] # remove non-numbers, leading spaces
lines = [re.sub(' +', '', line) for line in lines] # remove extra spaces

time = int(lines[0])
record = int(lines[1])

firstWin = 0
lastWin = 0

# For possible starting speeds, find first speed that wins
for speed in range(0, time):
    remainingTime = time - speed
    distance = speed * remainingTime

    if distance > record:
        firstWin = speed
        break

# For possible starting speeds, find last speed that wins
for speed in range(time, 0, -1):
    remainingTime = time - speed
    distance = speed * remainingTime

    if distance > record:
        lastWin = speed
        break

# Calculate number of speeds that win
winningWays = lastWin - firstWin + 1

print("Number of ways to win:", winningWays)
