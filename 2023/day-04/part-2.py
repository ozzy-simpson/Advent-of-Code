import os
import sys
import re

# open input file
input = open(os.path.join(sys.path[0], "input.txt"), 'r')
lines = input.readlines()
lines = [line.replace('\n', '') for line in lines] # remove newlines

# initialize
sum = 0 # sum of points
multiples = [1] * len(lines) # stores how many of each card we have

# Parse
for i, card in enumerate(lines):
    # get winning numbers for this card
    winningNumbers = card.split(' | ')[0].split(': ')[1].split(' ')
    winningNumbers = [int(re.sub('[^0-9]', '', num)) for num in winningNumbers if num != '']
    
    # count matches
    matches = 0
    nums = card.split(' | ')[1].split(' ')
    nums = [int(re.sub('[^0-9]', '', num)) for num in nums if num != '']
    for num in nums:
        matches += 1 if num in winningNumbers else 0

    # starting at index i, add 1 to multiples for next matches
    j = i + 1
    while matches > 0 and j < len(lines):
        multiples[j] += multiples[i]
        matches -= 1
        j += 1  

    sum += multiples[i]

# print results
print('Total points: ' + str(sum))
