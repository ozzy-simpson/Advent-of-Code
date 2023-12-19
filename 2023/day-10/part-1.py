import os
import sys

sys.setrecursionlimit(100000) # Set recursion limit to 100000

# open input file
input = open(os.path.join(sys.path[0], "input.txt"), 'r')
lines = input.readlines()
lines = [line.replace('\n', '') for line in lines] # remove newlines

start = (0, 0) # Starting position (row, col)
visited = [[-1] * len(lines[0]) for i in range(len(lines))] # Visited positions

# Find row, col of starting position S
for i, line in enumerate(lines):
    if 'S' in line:
        start = (i, line.index('S'))
        break

def moveRecur(current, steps):
    # Base case: if current position is not in the grid or is a ".", return out of the recursion
    if current[0] < 0 or current[0] >= len(lines) or current[1] < 0 or current[1] >= len(lines[0]) or lines[current[0]][current[1]] == '.':
        return

    # If current position has been visited before, see if we found a shorter path
    if visited[current[0]][current[1]] != -1: # If we have visited before
        if steps < visited[current[0]][current[1]]: # If we found a shorter path
            visited[current[0]][current[1]] = steps # Update the shortest path
        else:
            return # If we didn't find a shorter path, stop this recursion
    else: # If we haven't visited before, set the shortest path
        visited[current[0]][current[1]] = steps
        
    # Find next position(s)
    # If current position is a "|", recurse up and down
    if lines[current[0]][current[1]] == '|':
        moveRecur((current[0] - 1, current[1]), steps + 1) # Up
        moveRecur((current[0] + 1, current[1]), steps + 1) # Down
    # If current position is a "-", recurse left and right
    elif lines[current[0]][current[1]] == '-':
        moveRecur((current[0], current[1] - 1), steps + 1) # Left
        moveRecur((current[0], current[1] + 1), steps + 1) # Right
    # If current position is a "L", recurse up and right
    elif lines[current[0]][current[1]] == 'L':
        moveRecur((current[0] - 1, current[1]), steps + 1) # Up
        moveRecur((current[0], current[1] + 1), steps + 1) # Right
    # If current position is a "J", recurse up and left
    elif lines[current[0]][current[1]] == 'J':
        moveRecur((current[0] - 1, current[1]), steps + 1) # Up
        moveRecur((current[0], current[1] - 1), steps + 1) # Left
    # If current position is a "7", recurse down and left
    elif lines[current[0]][current[1]] == '7':
        moveRecur((current[0] + 1, current[1]), steps + 1) # Down
        moveRecur((current[0], current[1] - 1), steps + 1) # Left
    # If current position is a "F", recurse down and right
    elif lines[current[0]][current[1]] == 'F':
        moveRecur((current[0] + 1, current[1]), steps + 1) # Down
        moveRecur((current[0], current[1] + 1), steps + 1) # Right
    # If current position is a "S", see what's around it
    elif lines[current[0]][current[1]] == 'S':
        # See if connection to the right
        if lines[current[0]][current[1] + 1] in ['-', 'J', '7']:
            moveRecur((current[0], current[1] + 1), steps + 1) # Right
        # See if connection to the left
        if lines[current[0]][current[1] - 1] in ['-', 'L', 'F']:
            moveRecur((current[0], current[1] - 1), steps + 1) # Left
        # See if connection above
        if lines[current[0] - 1][current[1]] in ['|', '7', 'F']:
            moveRecur((current[0] - 1, current[1]), steps + 1) # Up
        # See if connection below
        if lines[current[0] + 1][current[1]] in ['|', 'L', 'J']:
            moveRecur((current[0] + 1, current[1]), steps + 1) # Down

# Start recursion
moveRecur(start, 0)

# Find the maximum value in visited
max = 0
for row in visited:
    for col in row:
        if col > max:
            max = col

print("Farthest position from start is", max, "steps away")