import os
import sys
import functools

def differences(numbers):
    # Store differences between neighboring numbers, until we get all 0s
    differences = []

    atEnd = False

    # Iterate through each number
    for i in range(len(numbers)):
        # If we're at the end of the list, break
        if i == len(numbers) - 1:
            break

        # Get the difference between the current number and the next number
        difference = numbers[i + 1] - numbers[i]

        # Append difference to list
        differences.append(difference)

    # If all 0s, atEnd = True
    if functools.reduce(lambda a, b: a + b, differences) == 0:
        atEnd = True

    return (differences, atEnd)

# open input file
input = open(os.path.join(sys.path[0], "input.txt"), 'r')
lines = input.readlines()
lines = [line.replace('\n', '') for line in lines] # remove newlines

# Sum of predictions
sum = 0

# Iterate through each line
for line in lines:
    # Split line into numbers
    numbers = [int(i) for i in line.split(' ')]

    # Store differences between neighboring numbers, until we get all 0s
    diffs = []

    # Get differences
    prevDiff = differences(numbers)
    diffs.append(prevDiff[0])

    # While we haven't reached the end, keep getting differences
    while (prevDiff[1] == False):
        prevDiff = differences(prevDiff[0])
        diffs.append(prevDiff[0])

    # Prepare diffs for extrapolation
    diffs[-1].insert(0, 0) # Insert 0 at beginning of last diff
    diffs.insert(0, numbers) # Insert input at beginning of diffs
    diffs.reverse() # Reverse diffs

    for i, diff in enumerate(diffs[1:]): # Iterate through diffs, except first one
        new = diff[0] - diffs[i][0]
        diffs[i + 1].insert(0, new)

    sum += diffs[-1][0] # Add extrapolated value to sum

print("Sum of extrapolated values:", sum)
