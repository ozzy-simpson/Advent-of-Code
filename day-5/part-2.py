import os
import sys

# open input file
input = open(os.path.join(sys.path[0], "input.txt"), 'r')
lines = input.readlines()

# initialize variables
stacks = []
stacks.append(['B', 'L', 'D', 'T', 'W', 'C', 'F', 'M'])
stacks.append(['N', 'B', 'L'])
stacks.append(['J', 'C', 'H', 'T', 'L', 'V'])
stacks.append(['S', 'P', 'J', 'W'])
stacks.append(['Z', 'S', 'C', 'F', 'T', 'L', 'R'])
stacks.append(['W', 'D', 'G', 'B', 'H', 'N', 'Z'])
stacks.append(['F', 'M', 'S', 'P', 'V', 'G', 'C', 'N'])
stacks.append(['W', 'Q', 'R', 'J', 'F', 'V', 'C', 'Z'])
stacks.append(['R', 'P', 'M', 'L', 'H'])

# for each line in the input
for line in lines:
    # skip initial lines that don't say the moves
    if line[0] != 'm':
        continue

    move = line.strip().split(' ')

    # get the source and destination stacks and how many to move
    source = int(move[3]) - 1
    destination = int(move[5]) - 1
    count = int(move[1])

    temp = []

    # move the crates to temp stack
    for i in range(count):
        temp.append(stacks[source].pop())
        
    # move the crates from temp stack to destination
    for i in range(count):
        stacks[destination].append(temp.pop())

# print the top of each stack
for stack in stacks:
    print(stack.pop(), end='')
print()