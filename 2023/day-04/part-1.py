import os
import sys
import re

# open input file
input = open(os.path.join(sys.path[0], "input.txt"), 'r')
lines = input.readlines()
lines = [line.replace('\n', '') for line in lines] # remove newlines

# initialize sum of points
sum = 0

# Parse
for card in lines:
    # get winning numbers for this card
    winningNumbers = card.split(' | ')[0].split(': ')[1].split(' ')
    winningNumbers = [int(re.sub('[^0-9]', '', num)) for num in winningNumbers if num != '']
    
    # count points
    points = 0
    nums = card.split(' | ')[1].split(' ')
    nums = [int(re.sub('[^0-9]', '', num)) for num in nums if num != '']
    for num in nums:
        if num in winningNumbers:
            if points == 0:
                points = 1
            else:
                points *= 2
    
    # add points to sum
    sum += points

# print results
print('Total points: ' + str(sum))
