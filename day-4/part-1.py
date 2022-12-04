import re

# open input file
input = open('input.txt', 'r')
lines = input.readlines()

# initialize variables
count = 0

for line in lines:
    assignment = re.split(',|-', line.strip()) # split on commas and dashes
    assignment = [eval(i) for i in assignment] # convert to int
    
    # create a list of the ranges
    part1 = set(range(assignment[0], assignment[1]+1))
    part2 = set(range(assignment[2], assignment[3]+1))

    # if either part is a subset of the other, then the ranges overlap and we increase count
    if part1.issubset(part2) or part2.issubset(part1):
        count += 1
        

print("Ranges that fully contain the other:", count)