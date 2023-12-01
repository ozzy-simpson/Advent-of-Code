import os
import sys

# open input file
input = open(os.path.join(sys.path[0], "input.txt"), 'r')
lines = input.readlines()

monkeys = []

class Monkey(object):
    global monkeys

    items = [] # list of worry levels of items monkey has
    numInspected = 0 # number of times monkey has inspected an item
    operation = "" # operation monkey performs
    test = 0 # test monkey performs
    testOps = [] # testOps[0] is the monkey the item gets thrown to if test is True, testOps[1] is the monkey the item gets thrown to if test is False

    def __init__(self, items, operation, test, testOps):
        self.items = items
        self.operation = operation
        self.test = test
        self.testOps = testOps

    # updates each item's worry level
    def calcOperation(self):
        newItems = []
        for item in self.items:
            op = self.operation.replace("old", str(item)) # replace "old" with item
            newItems.append(eval(op)) # evaluate operation
            self.numInspected += 1
        
        self.items = newItems # update items

    # monkey bored, worry level divided by 3
    def bored(self):
        self.items[:] = [x // 3 for x in self.items]
    
    # add item to monkey's items
    def addItem(self, item):
        self.items.append(item)

    # inspect items
    def inspect(self):
        self.calcOperation()
        self.bored()
    
    # perform tests and throw items
    def throw(self):
        for i in range(len(self.items)):
            item = self.items.pop()
            if item % self.test == 0:
                # move item to monkey in testOps[0]
                monkeys[self.testOps[0]].addItem(item)
            else:
                # move item to monkey in testOps[1]
                monkeys[self.testOps[1]].addItem(item)

# parse input
for line in lines:
    if line.startswith("  Starting items"):
        # set items
        line = line.strip().split("Starting items: ")
        items = []
        for item in line[1].split(", "):
            items.append(int(item))
    elif line.startswith("  Operation"):
        # set operation
        operation = line.strip().split("Operation: new = ")[1]
    elif line.startswith("  Test"):
        # set test
        test = int(line.strip().split("Test: divisible by ")[1])
    elif line.startswith("    If true"):
        # set trueTest
        trueTest = int(line.strip().split("If true: throw to monkey ")[1])
    elif line.startswith("    If false"):
        # set falseTest
        falseTest = int(line.strip().split("If false: throw to monkey ")[1])
        monkeys.append(Monkey(items, operation, test, [trueTest, falseTest]))

for i in range(20):
    for monkey in monkeys:
        monkey.inspect()
        monkey.throw()

monkeys.sort(key=lambda x: x.numInspected, reverse=True)

monkeyBiz = monkeys[0].numInspected * monkeys[1].numInspected

print("Level of monkey business:", monkeyBiz)
