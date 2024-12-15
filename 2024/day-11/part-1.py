import os
import sys

# open input file
with open(os.path.join(sys.path[0], "input.txt"), 'r') as input_file:
    stones = input_file.read()

# initialize variables
stones = [int(stone) for stone in stones.split(" ")]

def blink(stones):
    newStones = []
    for stone in stones:
        if stone == 0:
            # Replace with 1
            newStones.append(1)
        elif len(str(stone)) % 2 == 0:
            # Split in two
            s = str(stone)
            newStones.append(int(s[:len(s)//2]))
            newStones.append(int(s[len(s)//2:]))
        else:
            # Replace with 2024 * old value
            newStones.append(2024 * stone)

    return newStones

for i in range(25):
    stones = blink(stones)

print(len(stones))