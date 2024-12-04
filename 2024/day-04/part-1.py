import os
import sys
import re

# open input file
input = open(os.path.join(sys.path[0], "input.txt"), 'r')
lines = input.readlines()

# initialize variables
result = 0
word = "XMAS"
grid = [list(line.strip()) for line in lines] # Convert lines into grid of characters
rows = len(grid)
cols = len(grid[0])
word_len = len(word)
directions = [
    (0, 1),   # right
    (0, -1),  # left
    (1, 0),   # down
    (-1, 0),  # up
    (1, 1),   # diagonal down-right
    (-1, -1), # diagonal up-left
    (1, -1),  # diagonal down-left
    (-1, 1)   # diagonal up-right
]

# Search for "XMAS" in all directions at each cell
for r in range(rows):
    for c in range(cols):
        # Check each direction
        for dr, dc in directions:
            found = True
            
            # Check each character in the word
            for k in range(word_len):
                nr, nc = r + k * dr, c + k * dc # Move k steps in the direction
                # Check if out of bounds or character doesn't match
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != word[k]:
                    found = False
                    break

            # Found in current direction
            if found:
                result += 1

print(result) # print number of "XMAS"
