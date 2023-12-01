import os
import sys
import ast
import itertools as it

# open input file
input = open(os.path.join(sys.path[0], "input.txt"), 'r')
lines = input.readlines()

pairs = []
numPairs = (len(lines) + 1) // 3
sumIndices = 0

# parse input
for i in range(numPairs):
    pair1 = ast.literal_eval(lines[i*3].strip())
    pair2 = ast.literal_eval(lines[i*3+1].strip())
    pairs.append((pair1, pair2))

# compare two pairs
def compare(pair):
    if type(pair[0]) == int and type(pair[1]) == int:
        return compareInts(pair)
    if type(pair[0]) == list and type(pair[1]) == list:
        return compareLists(pair)
    return compareMix(pair)

# compare a pair of two ints
def compareInts(pair):
    if pair[0] > pair[1]:
        return False
    if pair[0] < pair[1]:
        return True
    return None

# compare a pair of two lists
def compareLists(pair):
    for l,r in it.zip_longest(pair[0], pair[1]):
        if l is None:
            return True
        if r is None:
            return False
        result = compare((l, r))
        if result is None:
            continue
        return result
    return None

# compare a pair of a list and an int
def compareMix(pair):
    if type(pair[0]) == int and type(pair[1]) == list:
        return compareLists(([pair[0]], pair[1]))
    if type(pair[0]) == list and type(pair[1]) == int:
        return compareLists((pair[0], [pair[1]]))
    return None

# compare all pairs
for i, pair in enumerate(pairs):
    if compare(pair):
        sumIndices += (i+1)

        
print("Sum of indices of correct pairs:", sumIndices)