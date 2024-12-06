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
directionTurns = {
    "^": ">",
    ">": "v",
    "v": "<",
    "<": "^"
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

guardStart = guard

def withinBounds(x, y):
    return 0 <= x < len(guardMap[0]) and 0 <= y < len(guardMap)

# Move guard, until it would move out of bounds
while True:
    x, y = guard

    # Move guard
    dx, dy = directions[currentDirection]
    x += dx
    y += dy

    # Check if guard is going to move out of bounds
    if not withinBounds(x, y):
        break
    
    # Check if guard is going to hit an obstacle. If so, move 90 degrees to the right
    if guardMap[y][x] == '#':
        currentDirection = directionTurns[currentDirection]
        continue
    else:
        # No obstacle, so mark current position as visited and move guard
        visited.add((x, y))
        guard = (x, y)

# Try adding obstacles at all visited positions, count how many result in a cycle
cycles = 0
for x, y in visited:
    # Skip guard start position
    if (x, y) == guardStart:
        continue

    # Add obstacle at position
    newGuardMap = [row.copy() for row in guardMap]
    newGuardMap[y][x] = '#'
    
    # Move guard, until it re-visits a position with same direction
    newVisited = defaultdict(set)
    guard = guardStart
    currentDirection = '^'
    while True:
        x, y = guard

        # Move guard
        dx, dy = directions[currentDirection]
        x += dx
        y += dy

        # Check if guard is going to move out of bounds
        if not withinBounds(x, y):
            break
        
        # Check if guard is going to hit an obstacle. If so, move 90 degrees to the right
        if newGuardMap[y][x] == '#':
            currentDirection = directionTurns[currentDirection]
            continue

        # Check if guard has visited a position with same direction before
        if (x, y) in newVisited[currentDirection]:
            cycles += 1
            break
        else:
            newVisited[currentDirection].add((x, y))
            guard = (x, y)

    # Print current progress
    print(f"\rCycles found: {cycles}...", end='\r') if cycles % 100 == 0 else None

print(f"Total cycles found: {cycles}")
