import os
import sys

# open input file
input = open(os.path.join(sys.path[0], "input.txt"), 'r')
lines = input.readlines()

# initialize stacks
stacks = [ [] for _ in range(len(lines[0])//4) ]

for line in lines:
    # stop after stacks are initialized
    if '[' not in line:
        break
    
    for i in range(len(line)//4):
        if line[i*4+1] != ' ':
            stacks[i].insert(0, line[i*4+1])

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
