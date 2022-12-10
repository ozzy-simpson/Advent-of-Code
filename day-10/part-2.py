import os
import sys
import numpy as np

# open input file
input = open(os.path.join(sys.path[0], "input.txt"), 'r')
lines = input.readlines()

# initialize variables
x = 1
cycle = 1

def checkCycle():
    global signalStrength

    sprite = [x-1, x, x+1]

    if ((cycle-1) % 40) in sprite:
        print("#", end="")
    else:
        print(".", end="")
    
    if cycle % 40 == 0:
        print()

for line in lines:
    if line.startswith("noop"):
        # noop does nothing
        checkCycle()
        cycle += 1
    elif line.startswith("addx"):
        for i in range(2):
            checkCycle()
            cycle += 1
        x += int(line.strip().split(" ")[1])