import os
import sys

# checks if two coordinates are overlapping or adjacent
def checkAdjacent(x, y):
    if x == y:
        # if x is the same as y
        return True
    elif (x[0] + 1, x[1]) == y:
        # if x is to the right of y
        return True
    elif (x[0] - 1, x[1]) == y:
        # if x is to the left of y
        return True
    elif (x[0], x[1] + 1) == y:
        # if x is above y
        return True
    elif (x[0], x[1] - 1) == y:
        # if x is below y
        return True
    elif (x[0] + 1, x[1] + 1) == y:
        # if x is to the top right of y
        return True
    elif (x[0] - 1, x[1] + 1) == y:
        # if x is to the top left of y
        return True
    elif (x[0] + 1, x[1] - 1) == y:
        # if x is to the bottom right of y
        return True
    elif (x[0] - 1, x[1] - 1) == y:
        # if x is to the bottom left of y
        return True
    else:
        return False

# open input file
input = open(os.path.join(sys.path[0], "input.txt"), 'r')
lines = input.readlines()

visited = set()

# set initial coordinates
head = (0, 0)
tail = (0, 0)
visited.add(tail) # add initial tail position to visited

for line in lines:
    line = line.strip()
    line = line.split(" ")
    line[1] = int(line[1])
    
    if line[0] == "R":
        # move right
        for i in range(line[1]):
            head = (head[0] + 1, head[1])
            
            # move tail if not adjacent
            if not checkAdjacent(head,tail):
                if tail[1] < head[1] and tail[0] + 2 == head[0]:
                    # head is above and to the right of tail, move diagonally
                    tail = (tail[0] + 1, tail[1] + 1)
                elif tail[1] > head[1] and tail[0] + 2 == head[0]:
                    # head is below and to the right of tail, move diagonally
                    tail = (tail[0] + 1, tail[1] - 1)
                else:
                    # head and tail on same row, move tail to the right
                    tail = (tail[0] + 1, tail[1])

            visited.add(tail)
    elif line[0] == "L":
        # move left
        for i in range(line[1]):
            head = (head[0] - 1, head[1])
            
            # move tail if not adjacent
            if not checkAdjacent(head,tail):
                if tail[1] < head[1] and tail[0] - 2 == head[0]:
                    # head is above and to the left of tail, move diagonally
                    tail = (tail[0] - 1, tail[1] + 1)
                elif tail[1] > head[1] and tail[0] - 2 == head[0]:
                    # head is below and to the left of tail, move diagonally
                    tail = (tail[0] - 1, tail[1] - 1)
                else:
                    # head and tail on same row, move tail to the left
                    tail = (tail[0] - 1, tail[1])
            
            visited.add(tail)
    elif line[0] == "U":
        # move up
        for i in range(line[1]):
            head = (head[0], head[1] + 1)
            
            # move tail if not adjacent
            if not checkAdjacent(head,tail):
                if tail[0] < head[0] and tail[1] + 2 == head[1]:
                    # head is above and to the left of tail, move diagonally
                    tail = (tail[0] + 1, tail[1] + 1)
                elif tail[0] > head[0] and tail[1] + 2 == head[1]:
                    # head is above and to the right of tail, move diagonally
                    tail = (tail[0] - 1, tail[1] + 1)
                else:
                    # head and tail on same column, move tail up
                    tail = (tail[0], tail[1] + 1)

            visited.add(tail)
    elif line[0] == "D":
        # move down
        for i in range(line[1]):
            head = (head[0], head[1] - 1)
            
            # move tail if not adjacent
            if not checkAdjacent(head,tail):
                if tail[0] < head[0] and tail[1] - 2 == head[1]:
                    # head is below and to the left of tail, move diagonally
                    tail = (tail[0] + 1, tail[1] - 1)
                elif tail[0] > head[0] and tail[1] - 2 == head[1]:
                    # head is below and to the right of tail, move diagonally
                    tail = (tail[0] - 1, tail[1] - 1)
                else:
                    # head and tail on same column, move tail down
                    tail = (tail[0], tail[1] - 1)

            visited.add(tail)
    
print("Positions tail visited:", len(visited))