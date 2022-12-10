import os
import sys

# open input file
input = open(os.path.join(sys.path[0], "input.txt"), 'r')
lines = input.readlines()

width = len(lines[0].strip())
height = len(lines)

results = set()
grid = [[0 for x in range(width)] for y in range(height)] # will store input here

# parse input
for y in range(height):
    for x in range(width):
        grid[y][x] = int(lines[y][x])

# mark edges as visible
for y in range(height):
    for x in range(width):
        if x == 0 or y == 0 or x == width - 1 or y == height - 1:
            # if edge, then visible
            results.add(str(x) + "," + str(y))

# check horizontally
for y in range(1, height - 1):
    # check starting from left
    prevMax = grid[y][0]
    for x in range(1, width - 2):
        # iterate through inner part of row
        if grid[y][x] > prevMax:
            # if current value is greater than previous, then visible
            results.add(str(x) + "," + str(y))
            prevMax = grid[y][x]  

    # check starting from right
    prevMax = grid[y][width - 1]
    for x in range(width - 2, 0, -1):
        # iterate through inner part of row
        if grid[y][x] > prevMax:
            # if current value is greater than previous, then visible
            results.add(str(x) + "," + str(y))
            prevMax = grid[y][x]            

# check vertically
for x in range(1, width - 1):
    # check starting from top
    prevMax = grid[0][x]
    for y in range(1, height - 2):
        # iterate through inner part of column
        if grid[y][x] > prevMax:
            # if current value is greater than previous, then visible
            results.add(str(x) + "," + str(y))
            prevMax = grid[y][x]  

    # check starting from bottom
    prevMax = grid[height - 1][x]
    for y in range(height - 2, 0, -1):
        # iterate through inner part of column
        if grid[y][x] > prevMax:
            # if current value is greater than previous, then visible
            results.add(str(x) + "," + str(y))
            prevMax = grid[y][x]     

print("There are", len(results), "tree(s) visible from outside the grid")
