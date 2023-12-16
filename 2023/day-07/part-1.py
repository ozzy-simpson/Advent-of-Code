import os
import sys
import functools

# Hand Types:
#     0: "Five of a kind",
#     1: "Four of a kind",
#     2: "Full house",
#     3: "Three of a kind",
#     4: "Two pair",
#     5: "One pair",
#     6: "High card"

cardMappings = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "J": 10,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1
}

# Given a string of a hand (such as "32T3K"), return the type of hand (index of handTypes)
def handType(hand):
    # Get frequency of each card
    freq = {}
    for card in hand:
        if card in freq:
            freq[card] += 1
        else:
            freq[card] = 1

    # Get number of unique cards
    uniqueCards = len(freq)

    # If all unique, it's high card
    if uniqueCards == len(hand):
        return 6
    
    # If all the same, it's five of a kind
    if uniqueCards == 1:
        return 0
    
    # If 4 cards have the same label and 1 card has a different label, it's a 4 of a kind
    if uniqueCards == 2 and 4 in freq.values():
        return 1
        
    # If 3 cards have the same label and remaining 2 share a different label, full house
    if uniqueCards == 2 and 3 in freq.values():
        return 2
        
    # If 3 cards have the same label and remaining 2 are unique, 3 of a kind
    if uniqueCards == 3 and 3 in freq.values():
        return 3
    
    # If 2 cards share label, two other cards share a label, and the last card is unique, two pair
    if uniqueCards == 3 and 2 in freq.values() and 1 in freq.values():
        return 4
    
    # If 2 cards share label, other 3 are unique, one pair
    if uniqueCards == 4 and 2 in freq.values():
        return 5

        
# Determine which hand is better
def rank(hand1, hand2):
    types = [
        handType(hand1["hand"]),
        handType(hand2["hand"]),
    ]
    if types[0] < types[1]:
        # Hand 1 is better
        return 1
    elif types[0] > types[1]:
        # Hand 2 is better
        return -1
    else:
        # Same hand type, compare individual cards
        # Compare cards in each hand, whichever has higher card first is better
        for i in range(5):
            if (cardMappings[hand1["hand"][i]] > cardMappings[hand2["hand"][i]]):
                return 1
            elif (cardMappings[hand1["hand"][i]] < cardMappings[hand2["hand"][i]]):
                return -1
            
    return 0 # same hand


# open input file
input = open(os.path.join(sys.path[0], "input.txt"), 'r')
lines = input.readlines()
lines = [line.replace('\n', '') for line in lines] # remove newlines

# Store hands
hands = []

# Parse
for card in lines:
    # Split into hand and bid
    hand, bid = card.split(' ')

    # Add object with hand and bid to hands array
    hands.append({"hand": hand, "bid": bid})

# Sort hands, using rank on hand key of objects
sorted = sorted(hands, key=functools.cmp_to_key(rank))

# Calculate winnings
winnings = 0
i = 1
for hand in sorted:
    winnings += int(hand["bid"]) * i
    i += 1

# print results
print('Total winnings:', winnings)
