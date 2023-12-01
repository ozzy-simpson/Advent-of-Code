import os
import sys

# open input file
input = open(os.path.join(sys.path[0], "input.txt"), 'r')
lines = input.readlines()

# initialize variables
x = 1
cycle = 1
signalStrength = 0

def checkCycle():
    global signalStrength

    if (cycle - 20) % 40 == 0:
        current = x * cycle
        signalStrength += current

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

print("Sum of signal strengths =", signalStrength)