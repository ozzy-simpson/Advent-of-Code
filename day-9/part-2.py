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


# set initial coordinates
ropes = [(0, 0) for i in range(10)]
visited = {(0, 0)}

def move(hi, ti, direction):
    hx, hy = ropes[hi]
    tx, ty = ropes[ti]

    # move head
    if direction == 'R':
        hx += 1
    elif direction == 'L':
        hx -= 1
    elif direction == 'D':
        hy += 1
    elif direction == 'U':
        hy -= 1
    
    # move tail if not adjacent
    if checkAdjacent((hx, hy), (tx, ty)):
        pass
    elif tx == hx:
        # same x, move vertically
        if ty < hy:
            ty += 1
        else:
            ty -= 1
    elif ty == hy:
        # same y, move horizontally
        if tx < hx:
            tx += 1
        else:
            tx -= 1
    else:
        # move diagonally
        if tx < hx:
            tx += 1
        else:
            tx -= 1
        if ty < hy:
            ty += 1
        else:
            ty -= 1
    
    ropes[hi] = (hx, hy)
    ropes[ti] = (tx, ty)

for line in lines:
    line = line.strip()
    line = line.split(" ")
    line[1] = int(line[1])

    for i in range(line[1]):
        move(0, 1, line[0]) # move head

        # move tails
        for j in range(1, len(ropes) - 1):
            move(j, j + 1, "")
        visited.add(ropes[-1])

print("Positions tail visited:", len(visited))