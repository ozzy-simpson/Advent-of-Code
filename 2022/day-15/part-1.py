import os
import sys
import re

# open input file
input = open(os.path.join(sys.path[0], "input.txt"), 'r')
lines = input.readlines()

# read sensors and beacons in
devices = []
for line in lines:
    device = line.replace("Sensor at ", "",).replace("closest beacon is at ", "").strip()
    device = re.split(': |, |=', device)

    devices.append([(int(device[1]), int(device[3])), (int(device[5]), int(device[7]))])

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

sections = []
target = 2000000

# find all ranges that are blocked
for d in devices:
    sensor, beacon = d
    dist = distance(sensor, beacon)
    
    distFromY = abs(sensor[1] - target)
    if distFromY <= dist:
        startBlock = sensor[0] - (dist - distFromY)
        endBlock = sensor[0] + (dist - distFromY)
        sections.append([startBlock, endBlock])


# combine overlapping sections
combinedSections = []
for low,high in sorted(sections):
    if combinedSections and combinedSections[-1][1] >= low-1:
        combinedSections[-1][1] = max(combinedSections[-1][1], high)
    else:
        combinedSections.append([low, high])

print("Positions that cannot contain a beacon:", sum(h-l for l, h in combinedSections))
