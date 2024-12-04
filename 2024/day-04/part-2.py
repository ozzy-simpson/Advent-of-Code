import os
import sys
import re

# open input file
input = open(os.path.join(sys.path[0], "input.txt"), 'r')
lines = input.readlines()

# initialize variables
result = 0
grid = [list(line.strip()) for line in lines] # Convert lines into grid of characters
rows = len(grid)
cols = len(grid[0])
patterns = [
    [(-1, -1, 'M'), (1, 1, 'S'), (-1, 1, 'M'), (1, -1, 'S')], # M's at top
    [(-1, -1, 'M'), (1, 1, 'S'), (1, -1, 'M'), (-1, 1, 'S')], # M's at left
    [(1, -1, 'M'), (-1, -1, 'S'), (1, 1, 'M'), (-1, 1, 'S')], # M's at bottom
    [(1, 1, 'M'), (-1, -1, 'S'), (-1, 1, 'M'), (1, -1, 'S')], # M's at right
]

# Search for patterns with each cell as the center
for r in range(rows):
    for c in range(cols):
        # Skip if cell is not 'A'
        if grid[r][c] != 'A':
            continue

        # Check if any of the patterns match
        for pattern in patterns:
            found = True

            # Check each character in the pattern
            for dr, dc, char in pattern:
                nr, nc = r + dr, c + dc
                # Check if out of bounds or character doesn't match
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != char:
                    found = False
                    break

            # Found in current pattern
            if found:
                result += 1

print(result) # print number of "X-MAS" patterns
