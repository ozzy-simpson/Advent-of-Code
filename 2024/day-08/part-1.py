import os
import sys
from itertools import combinations

# open input file
with open(os.path.join(sys.path[0], "input.txt"), 'r') as input_file:
    lines = input_file.read()

# initialize variables
lines = lines.split("\n")
antenna_freq = {}
antinodes = set()

# Extract freqs from input
for y in range(len(lines)):
    for x in range(len(lines[y])):
        f = lines[y][x]

        # Skip empty spaces
        if lines[y][x] == ".":
            continue
       
        # Add freq to dict
        if f not in antenna_freq:
            antenna_freq[f] = []
        antenna_freq[f].append((x, y))

# Find antinodes
for f in antenna_freq:
    # Get all combinations of two antennas of the same type
    for c in combinations(antenna_freq[f], 2):
        x1, y1 = c[0]
        x2, y2 = c[1]

        # Get slope
        rise, run = y1 - y2, x1 - x2

        # Create new antinodes
        newAntinodes = [(x1 + run, y1 + rise), (x2 - run, y2 - rise)]

        # Add to antinodes if within bounds
        for a in newAntinodes:
            if 0 <= a[0] < len(lines[0]) and 0 <= a[1] < len(lines):
                antinodes.add(a)

print(len(antinodes))
