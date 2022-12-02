# open input file
input = open('d2-input.txt', 'r')
lines = input.readlines()

score = 0
for line in lines:
    moves = line.replace("\n","").split(' ')
    
    # add score of move
    if moves[1] == 'X':
        score += 1
    elif moves[1] == 'Y':
        score += 2
    elif moves[1] == 'Z':
        score += 3

    # add score of round
    if (ord(moves[0]) - ord('A')) == (ord(moves[1]) - ord('X')):
        # same move, tie
        score += 3
    elif moves[1] == 'X' and moves[0] == 'C':
        # rock beats scissors
        score += 6
    elif moves[1] == 'Y' and moves[0] == 'A':
        # paper beats rock
        score += 6
    elif moves[1] == 'Z' and moves[0] == 'B':
        # scissors beats paper
        score += 6

print("Score:", score)
