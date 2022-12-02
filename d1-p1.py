# open input file
input = open('d1-input.txt', 'r')
lines = input.readlines()

# initialize variables
count = 1
current = 0
max_elf = 0
max_amount = 0

for line in lines:
    # check if blank line, if so check if current amount is greater than max. if it is, that is our new best elf
    if line in ['\n', '\r\n']:
        if current > max_amount:
            max_elf = count # set new max elf
            max_amount = current # set new max amount
        count += 1 # increment elf count
        current = 0 # reset current amount

        continue

    # add current line to current amount
    current += int(line)
    
# print results
print('Elf ' + str(max_elf) + ' has the most amount of Calories: ' + str(max_amount))