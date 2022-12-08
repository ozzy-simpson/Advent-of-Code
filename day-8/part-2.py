import os
import sys

# open input file
input = open(os.path.join(sys.path[0], "input.txt"), 'r')
lines = input.readlines()

width = len(lines[0].strip())
height = len(lines)

result = [[0 for x in range(width)] for y in range(height)] # will store result here
grid = [[0 for x in range(width)] for y in range(height)] # will store input here

# parse input
for y in range(height):
    for x in range(width):
        grid[y][x] = int(lines[y][x])

maxScenicScore = 0

for y in range(height):
    for x in range(width):
        scenicScore = 1
        current = grid[y][x]
        count = 0

        # check to the left
        for i in range(x - 1, -1, -1):
            if grid[y][i] >= current:
                count += 1
                break
            elif grid[y][i] < current:
                count += 1

        scenicScore *= count
        count = 0

        # check to the right
        for i in range(x + 1, width):
            if grid[y][i] >= current:
                count += 1
                break
            elif grid[y][i] < current:
                count += 1

        scenicScore *= count
        count = 0

        # check above
        for i in range(y - 1, -1, -1):
            if grid[i][x] >= current:
                count += 1
                break
            elif grid[i][x] < current:
                count += 1
            
        scenicScore *= count
        count = 0

        # check below
        for i in range(y + 1, height):
            if grid[i][x] >= current:
                count += 1
                break
            elif grid[i][x] < current:
                count += 1

        scenicScore *= count

        # print(scenicScore) if scenicScore > 0 else None

        result[y][x] = scenicScore

        # replace maxScenicScore if necessary
        if scenicScore > maxScenicScore:
            maxScenicScore = scenicScore

print("Maximum scenic score possible:", maxScenicScore)
