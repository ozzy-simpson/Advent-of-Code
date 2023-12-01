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

def findBlocked(row):
    sections = []

    # find all ranges that are blocked
    for d in devices:
        sensor, beacon = d
        dist = distance(sensor, beacon)
        
        distFromY = abs(sensor[1] - row)
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
        
    return combinedSections

for i in range (4000000 + 1):
    progress = round(i/4000000, 2) * 100
    print("Progress:", str(round(progress)) + "%", end="\r", flush=True)
    blocked = findBlocked(i)
    if len(blocked) > 1:
        x = (blocked[1][0] + blocked[0][1])//2
        freq = x*4000000+i
        print("Tuning frequency:", freq, end="\n", flush=True)
        break
