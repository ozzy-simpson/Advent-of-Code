import os
import sys

# open input file
input = open(os.path.join(sys.path[0], "input.txt"), 'r')
buffer = input.readlines()[0].strip()

for i in range(len(buffer) - 3):
    if len(set(buffer[i:i+4])) == len(buffer[i:i+4]):
        print("Marker after character", str(i+4) + ":", buffer[i:i+4])
        break
