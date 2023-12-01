import os
import sys
import ast
import itertools as it
from functools import cmp_to_key

# open input file
input = open(os.path.join(sys.path[0], "input.txt"), 'r')
lines = input.readlines()

pairs = []
numPairs = (len(lines) + 1) // 3
decoderKey = 0

# parse input
for i in range(numPairs):
    pairs.append(ast.literal_eval(lines[i*3].strip()))
    pairs.append(ast.literal_eval(lines[i*3+1].strip()))

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

pairs_sorted = [[[2]], [[6]]]

for i, pair in enumerate(pairs):
    for j, item in enumerate(pairs_sorted):
        compared = compare((item, pair))
        if not compared:
            pairs_sorted.insert(j, pair)
            break
        if j == len(pairs_sorted) - 1:
            pairs_sorted.append(pair)

i1, i2 = pairs_sorted.index([[2]]) + 1, pairs_sorted.index([[6]]) + 1
print("Decoder key:", i1*i2)
