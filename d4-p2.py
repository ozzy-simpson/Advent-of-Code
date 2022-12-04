import re

# open input file
input = open('d4-input.txt', 'r')
lines = input.readlines()

# initialize variables
count = 0

for line in lines:
    assignment = re.split(',|-', line.strip()) # split on commas and dashes
    assignment = [eval(i) for i in assignment] # convert to int
    
    # create a list of the ranges
    part1 = list(range(assignment[0], assignment[1]+1))
    part2 = list(range(assignment[2], assignment[3]+1))

    # convert to set
    part1 = set(part1)
    part2 = set(part2)

    # find the intersection
    intersection = part1.intersection(part2)

    # if intersection not empty, add to count
    if intersection:
        count += 1
        

print("Ranges that overlap:", count)