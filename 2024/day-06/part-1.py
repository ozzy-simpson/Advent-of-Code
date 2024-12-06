from collections import defaultdict
import os
import sys
import re

# open input file
with open(os.path.join(sys.path[0], "input.txt"), 'r') as input_file:
    lines = input_file.readlines()

# initialize variables
guardMap = []
visited = set()
guard = (0, 0)
directions = {
    "^": (0, -1),
    "v": (0, 1),
    "<": (-1, 0),
    ">": (1, 0)
}
currentDirection = '^'
guardFound = False

# Parse input, find guard
for i, line in enumerate(lines):
    current = list(line.strip())
    guardMap.append(current)
    if not guardFound:
        for j, point in enumerate(current):
            if point == '^':
                # Guard found, save position
                guard = (j, i)
                visited.add(guard)
                guardFound = True
                break

# Move guard, until it would move out of bounds
while True:
    x, y = guard

    # Move guard
    dx, dy = directions[currentDirection]
    x += dx
    y += dy

    # Check if guard is going to move out of bounds
    if x < 0 or y < 0 or x >= len(guardMap[0]) or y >= len(guardMap):
        break
    
    # Check if guard is going to hit an obstacle. If so, move 90 degrees to the right
    if guardMap[y][x] == '#':
        currentDirection = {
            "^": ">",
            ">": "v",
            "v": "<",
            "<": "^"
        }[currentDirection]
        continue
    else:
        # No obstacle, so mark current position as visited and move guard
        visited.add((x, y))
        guard = (x, y)

print(len(visited))
