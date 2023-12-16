import os
import sys
import functools
import re

# open input file
input = open(os.path.join(sys.path[0], "input.txt"), 'r')
lines = input.readlines()
lines = [line.replace('\n', '') for line in lines] # remove newlines

# Get directions
directions = lines[0]

# Store nodes and left/right values
nodes = {}

# Parse
for node in lines[2:]:
    node = re.sub('[^A-Z ]', '', node)
    node, left, right = re.sub(' +', ' ', node).split(' ')
    
    nodes[node] = [left, right]

# Initialize
currentDirection = 0 # index of `directions`
steps = 0 # number of steps taken

# Start at node A
currentNode = "AAA"
endNode = "ZZZ"

# Keep going until we reach the end
while currentNode != endNode:
    # Get current direction
    direction = directions[currentDirection]
    
    # Get next node
    nextNode = nodes[currentNode][0] if direction == "L" else nodes[currentNode][1]
    
    # Update current node
    currentNode = nextNode
    
    # Update steps
    steps += 1
    
    # Update direction
    currentDirection = (currentDirection + 1) % len(directions)

print("Steps taken:", steps)