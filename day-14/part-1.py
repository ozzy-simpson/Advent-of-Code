import os
import sys
import numpy as np

# open input file
input = open(os.path.join(sys.path[0], "input.txt"), 'r')
lines = input.readlines()

# find minimum and maximum x and y values in the input
minX = 500
maxX = 0
minY = 0
maxY = 0
for line in lines:
    moves = line.strip().split(' -> ')
    for move in moves:
        splitCoords = move.split(',')
        splitCoords = [eval(i) for i in splitCoords]
        x, y = map(int, splitCoords)
        minX = min(minX, x)
        maxX = max(maxX, x)
        minY = min(minY, y)
        maxY = max(maxY, y)

dimensions = (maxX - minX + 1, maxY - minY + 1)

# create a 2D array of the input
grid = [['.' for i in range(dimensions[0])] for j in range(dimensions[1])]

# fill in the 2D array with the input
for line in lines:
    moves = line.strip().split(' -> ')
    for i in range(1, len(moves)):
        start = moves[i-1].split(',')
        start = [eval(j) for j in start]
        start[0] = start[0] - minX
        start[1] = start[1] - minY
        end = moves[i].split(',')
        end = [eval(j) for j in end]
        end[0] = end[0] - minX
        end[1] = end[1] - minY

        if start[0] == end[0] and start[1] < end[1]:
            # move down
            for j in range(start[1], end[1]+1):
                grid[j][start[0]] = '#'
        elif start[0] == end[0] and start[1] > end[1]:
            # move up
            for j in range(start[1], end[1]-1, -1):
                grid[j][start[0]] = '#'
        elif start[1] == end[1] and start[0] < end[0]:
            # move right
            for j in range(start[0], end[0]+1):
                grid[start[1]][j] = '#'
        elif start[1] == end[1] and start[0] > end[0]:
            # move left
            for j in range(start[0], end[0]-1, -1):
                grid[start[1]][j] = '#'

# drop sand!
sand = (500 - minX, 0)
countSand = 0
end = False

def dropSand():
    global end, sand, countSand
    atRest = False
    pos = sand
    while not atRest:
        print(pos, dimensions)
        if pos[0] < 0 or pos[0] >= dimensions[0] or pos[1] + 1 >= dimensions[1]:
            end = True
            atRest = True
        elif grid[pos[1]+1][pos[0]] == '.':
            # move down
            pos = (pos[0], pos[1] + 1)
        elif grid[pos[1]+1][pos[0]-1] == '.':
            # move left
            pos = (pos[0] - 1, pos[1])
        elif grid[pos[1]+1][pos[0]+1] == '.':
            # move right
            pos = (pos[0] + 1, pos[1])
        else:
            grid[pos[1]][pos[0]] = 'o'
            countSand += 1
            if pos[0] == sand[0] and pos[1] == sand[1]:
                end = True
            atRest = True

while not end:
    dropSand()

print("Sand at rest:", countSand)
