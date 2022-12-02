# open input file
input = open('d2-input.txt', 'r')
lines = input.readlines()

score = 0
for line in lines:
    moves = line.replace("\n","").split(' ')

    move_to_play = ord(moves[0]) - ord('A')

    # determine move
    if moves[1] == 'X':
        # need to lose
        move_to_play = (move_to_play + 2) % 3
    elif moves[1] == 'Y':
        # need to tie, play same move
        score += 3
    elif moves[1] == 'Z':
        # need to win
        move_to_play = (move_to_play + 1) % 3
        score += 6
        
    # add score of move
    score += move_to_play + 1

print("Score:", score)
