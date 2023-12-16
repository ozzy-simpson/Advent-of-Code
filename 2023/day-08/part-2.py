import os
import sys
import math
import re

# open input file
input = open(os.path.join(sys.path[0], "input.txt"), 'r')
lines = input.readlines()
lines = [line.replace('\n', '') for line in lines] # remove newlines

# Get directions
directions = lines[0]

# Store nodes and left/right values
nodes = {}

nodesEndA = []

# Parse
for node in lines[2:]:
    node = re.sub('[^A-Z0-9 ]', '', node)
    node, left, right = re.sub(' +', ' ', node).split(' ')
    
    nodes[node] = [left, right]

    if node[-1] == "A":
        nodesEndA.append(node)

# Initialize
currentDirection = 0 # index of `directions`
steps = 0 # number of steps taken
solutions = []

# Start at nodes that end in A
currentNodes = nodesEndA

numSolutions = len(currentNodes)

# Keep going until we reach the end
while len(solutions) < numSolutions:
    # Get current direction
    direction = directions[currentDirection]

    nextNodes = []

    for node in currentNodes:
        nextNode = nodes[node][0] if direction == "L" else nodes[node][1]

        if nextNode[-1] == "Z":
            solutions.append(steps + 1)
        else:
            nextNodes.append(nextNode)
    
    # Update current node
    currentNodes = nextNodes

    # Update steps
    steps += 1
    
    # Update direction
    currentDirection = (currentDirection + 1) % len(directions)

    # If all current nodes end in Z, we're done
    if all([node[-1] == "Z" for node in currentNodes]):
        break

print("Steps taken:", math.lcm(*solutions))
