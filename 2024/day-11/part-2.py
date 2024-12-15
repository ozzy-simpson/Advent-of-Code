import os
import sys
from functools import cache

# open input file
with open(os.path.join(sys.path[0], "input.txt"), 'r') as input_file:
    stones = input_file.read()

# initialize variables
stones = [int(stone) for stone in stones.split(" ")]

@cache
def blink(stone, n):
    if n == 0:
        return 1
    
    if stone == 0:
        # Replace with 1
        return blink(1, n - 1)
    elif len(str(stone)) % 2 == 0:
        # Split in two
        s = str(stone)
        return blink(int(s[:len(s)//2]), n - 1) + blink(int(s[len(s)//2:]), n - 1)
    else:
        # Replace with 2024 * old value
        return blink(2024 * stone, n - 1)
    
stones = sum([blink(stone, 75) for stone in stones])

print(stones)