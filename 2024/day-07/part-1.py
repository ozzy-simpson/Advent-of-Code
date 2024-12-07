import os
import sys

# open input file
with open(os.path.join(sys.path[0], "input.txt"), 'r') as input_file:
    lines = input_file.readlines()

# initialize variables
calibration = 0
operators = [lambda a,b: a+b, lambda a,b: a*b]

def checkValid(result, ints, current):
    global operators

    # Base case: If we went above desired result, return false
    if current > result:
        return False
    
    # Base case: If one int left, check operations on it
    if len(ints) == 1:
        for op in operators:
            if op(current, ints[0]) == result:
                return result
        
        return False # Couldn't get result, invalid
    
    # For each possible operation, make recursive calls on the rest of the ints
    for op in operators:
        if checkValid(result, ints[1:], op(current, ints[0])):
            return result
        
    return False # Couldn't get result, invalid

for line in lines:
    result = int(line.split(": ")[0])
    ints = [int(n) for n in line.split(": ")[1].split(" ")]

    if checkValid(result, ints[1:], ints[0]):
        calibration += result

print(calibration)
