# open input file
input = open('input.txt', 'r')
lines = input.readlines()

# initialize variables
current = 0
elves = []

for line in lines:
    # check if blank line, if so add elf to list
    if line in ['\n', '\r\n']:
        elves.append(current) # add elf to list
        current = 0 # reset current amount
        continue # skip to next line

    # add current line to current amount
    current += int(line)
    
# sort results
elves.sort(reverse=True)
print("Top 3 elves are carrying", sum(elves[0:3]),"total calories")
