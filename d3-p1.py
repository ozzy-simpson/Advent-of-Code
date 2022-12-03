# open input file
input = open('d3-input.txt', 'r')
lines = input.readlines()

# initialize variables
prioritiesSum = 0

for line in lines:
    # split line into compartments
    compartments = []
    compartments.append(line[:len(line)//2])
    compartments.append(line[len(line)//2:])

    for char in compartments[0]:
        if char in compartments[1]:
            if char.islower():
                # convert ASCII (lower) to priority
                prioritiesSum += ord(char) - 96
            else:
                # convert ASCII (upper) to priority
                prioritiesSum += ord(char) - 38
            break


print("Sum of item priorities:", prioritiesSum)