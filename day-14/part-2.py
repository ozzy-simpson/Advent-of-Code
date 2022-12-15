import os
import sys

# open input file
input = open(os.path.join(sys.path[0], "input.txt"), 'r')
lines = input.readlines()

# find minimum and maximum x and y values in the input
maxY = 0
for line in lines:
    moves = line.strip().split(' -> ')
    for move in moves:
        splitCoords = move.split(',')
        splitCoords = [eval(i) for i in splitCoords]
        x, y = map(int, splitCoords)
        maxY = max(maxY, y)

maxY = maxY + 2

blocked = set()

# fill in the 2D array with the input
for line in lines:
    moves = line.strip().split(' -> ')
    for i in range(1, len(moves)):
        start = moves[i-1].split(',')
        start = [eval(j) for j in start]
        end = moves[i].split(',')
        end = [eval(j) for j in end]

        if start[0] == end[0] and start[1] < end[1]:
            # move down
            for j in range(start[1], end[1]+1):
                blocked.add((start[0], j))
        elif start[0] == end[0] and start[1] > end[1]:
            # move up
            for j in range(start[1], end[1]-1, -1):
                blocked.add((start[0], j))
        elif start[1] == end[1] and start[0] < end[0]:
            # move right
            for j in range(start[0], end[0]+1):
                blocked.add((j, start[1]))
        elif start[1] == end[1] and start[0] > end[0]:
            # move left
            for j in range(start[0], end[0]-1, -1):
                blocked.add((j, start[1]))

# drop sand!
countSand = 1
queue = {(500, 0)}

while len(queue) > 0:
    newQueue = set()
    for sand in queue:
        if sand[1] < maxY - 1:
            if (sand[0], sand[1]+1) not in blocked:
                # add below to queue
                newSand = (sand[0], sand[1] + 1)
                blocked.add(newSand)
                newQueue.add(newSand)
            if (sand[0]-1, sand[1] + 1) not in blocked:
                # add left below to queue
                newSand = (sand[0] - 1, sand[1] + 1)
                blocked.add(newSand)
                newQueue.add(newSand)
            if (sand[0]+1, sand[1] + 1) not in blocked:
                # add right below to queue
                newSand = (sand[0] + 1, sand[1] + 1)
                blocked.add(newSand)
                newQueue.add(newSand)
    queue = newQueue
    countSand += len(newQueue)

print("Sand at rest:", countSand)
