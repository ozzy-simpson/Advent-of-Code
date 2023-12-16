import os
import sys
import re

# open input file
input = open(os.path.join(sys.path[0], "input.txt"), 'r')
lines = input.readlines()

# Parse lines
lines = [re.sub('[^0-9 ]', '', line).lstrip() for line in lines] # remove non-numbers, leading spaces
lines = [re.sub(' +', ' ', line).split(" ") for line in lines] # remove extra spaces

winningWays = 1

for race in range(len(lines[0])):
    time = int(lines[0][race])
    record = int(lines[1][race])

    currentWays = 0

    # For possible starting speeds, calculate distance
    for speed in range(time):
        remainingTime = time - speed
        distance = speed * remainingTime

        currentWays += 1 if distance > record else 0

    winningWays *= currentWays

print("Multiple of ways to win:", winningWays)
