# open input file
input = open('d2-input.txt', 'r')
lines = input.readlines()

score = 0
for line in lines:
    moves = line.replace("\n","").split(' ')

    move_to_play = ''

    # determine move
    if moves[1] == 'X':
        # need to lose
        move_to_play = chr((ord(moves[0]) - ord('A') + 2) % 3 + ord('X'))
    elif moves[1] == 'Y':
        # need to tie, play same move
        move_to_play = chr(ord(moves[0]) - ord('A') + ord('X'))
        score += 3
    elif moves[1] == 'Z':
        # need to win
        move_to_play = chr((ord(moves[0]) - ord('A') + 1) % 3 + ord('X'))
        score += 6
        
    # add score of move
    score += ord(move_to_play) - ord('X') + 1

print("Score:", score)
