import os
import sys

# open input file
input = open(os.path.join(sys.path[0], "input.txt"), 'r')
lines = input.readlines()

grid = [list(x.strip()) for x in lines] # populate grid
start = (0,0)

# parse grid: find start/end and convert letters to numbers (ASCII values)
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "S":
            grid[i][j] = "a"
        elif grid[i][j] == "E":
            start = (i, j)
            grid[i][j] = "z"
        grid[i][j] = ord(grid[i][j])

queue = [(0, start)] # queue of positions to check
seen = set() # set of positions already seen

while True:
    length, point = queue.pop(0) # get length, point from queue
    if point in seen:
        continue
        
    seen.add(point) # add position to seen
    y, x = point # get y, x from point

    if grid[y][x] == ord("a"):
        print("Closest a to E:", length)
        break

    # check all 4 directions
    for dy, dx in ((1,0), (-1,0), (0,1), (0,-1)):
        newY, newX = y + dy, x + dx

        # check if new position is in bounds
        if 0 <= newY < len(grid) and 0 <= newX < len(grid[0]) and (newY, newX) not in seen and (grid[y][x] - grid[newY][newX]) <= 1:
            queue.append((length + 1, (newY, newX)))
