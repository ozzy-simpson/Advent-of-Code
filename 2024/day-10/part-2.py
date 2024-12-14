import os
import sys
from itertools import combinations

# open input file
with open(os.path.join(sys.path[0], "input.txt"), 'r') as input_file:
    lines = input_file.read()

# initialize variables
lines = lines.split('\n')
map = [[int(i) for i in lines] for lines in lines]
trailheads = []
score = 0

# find trailheads
for y in range(len(map)):
    for x in range(len(map[y])):
        if map[y][x] == 0:
            trailheads.append((x, y))

for th in trailheads:
    curScore = 0
    visited = set()

    queue = [th]

    while queue:
        cur = queue.pop()

        # check if at peak (9)
        if (val := map[cur[1]][cur[0]]) == 9:
            curScore += 1
            continue

        # add neighbors to queue (up, down, left, right), if they are the next value
        dirs = [
            (0, -1),  # up
            (0, 1),  # down
            (-1, 0),  # left
            (1, 0)  # right
        ]

        for d in dirs:
            x = cur[0] + d[0]
            y = cur[1] + d[1]

            if x < 0 or x >= len(map[0]) or y < 0 or y >= len(map):
                continue

            if map[y][x] == val + 1:
                queue.append((x, y))

    score += curScore

print(score)
