from collections import defaultdict
import os
import sys
import re

# open input file
with open(os.path.join(sys.path[0], "input.txt"), 'r') as input_file:
    lines = input_file.readlines()

# initialize variables
result = 0
pageOrderings = defaultdict(list)
updateStart = 0

# Get page orderings
for i, line in enumerate(lines):
    # Get the numbers
    numbers = re.findall(r'\d+', line)

    # Not a line that represents a page ordering
    if len(numbers) != 2:
        # Once we get a line that represents an update, we stop looking for page orderings
        updateStart = i + 1
        break

    # Get the page numbers
    first, second = int(numbers[0]), int(numbers[1])

    # Add to pageOrderings dictionary
    pageOrderings[first].append(second)

# Get the updates
for line in lines[updateStart:]:
    # Split the line into numbers (comma-separated)
    numbers = [int(n) for n in line.split(',')]

    # Initialize variables for this update
    seen = set()
    isValid = True

    # Iterate through the numbers
    for number in numbers:
        # If the number is in the pageOrderings dictionary
        if number in pageOrderings:
            for page in pageOrderings[number]:
                # If the page is already seen, then the update is invalid
                if page in seen:
                    isValid = False
                    break
            if not isValid:
                break
        seen.add(number)
    
    # If the update is valid, add the middle number to the result
    result += numbers[len(numbers) // 2] if isValid else 0

print(result)
