import os
import sys

# open input file
input = open(os.path.join(sys.path[0], "input.txt"), 'r')
lines = input.readlines()
lines = [line.replace('\n', '') for line in lines] # remove newlines

emptyRows = [True] * len(lines)
emptyCols = [True] * len(lines[0])

# Determine which rows and columns are empty
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == '#':
            emptyRows[i] = False
            emptyCols[j] = False

# Determine galaxy (#) points. Store (row, col) tuples in set
galaxies = set()
for row in range(len(lines)):
    numEmptyRows = 0
    for e in emptyRows[0:row]:
        numEmptyRows += 1 if e else 0
    rowOffset = row + (1_000_000 - 1) * numEmptyRows

    for col in range(len(lines[i])):
        numEmptyCols = 0
        for e in emptyCols[0:col]:
            numEmptyCols += 1 if e else 0
        colOffset = col + (1_000_000 - 1) * numEmptyCols

        if lines[row][col] == '#':
            # Found galaxy, offset by empty rows and cols
            galaxies.add((rowOffset, colOffset))

# Convert set to list for indexing
galaxies = list(galaxies)

# Calculate shortest path between each pair of galaxies
shortestPathSum = 0
for i, galaxy1 in enumerate(galaxies):
    for galaxy2 in galaxies[i+1:]:
        # Calculate distance between galaxies
        shortestPathSum += abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])

print("Sum of shortest paths between each pair of galaxies =", shortestPathSum)
