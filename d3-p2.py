# open input file
input = open('d3-input.txt', 'r')
lines = input.readlines()

# initialize variables
prioritiesSum = 0

for count, line in enumerate(lines[::3]):
    commonChar = ''.join(set(line.strip()).intersection(lines[count*3+1]).intersection(lines[count*3+2]))
    if commonChar.islower():
        # convert ASCII (lower) to priority
        prioritiesSum += ord(commonChar) - 96
    else:
        # convert ASCII (upper) to priority
        prioritiesSum += ord(commonChar) - 38


print("Sum of item priorixties:", prioritiesSum)