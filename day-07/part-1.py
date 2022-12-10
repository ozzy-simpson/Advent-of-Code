import os
import sys

# open input file
input = open(os.path.join(sys.path[0], "input.txt"), 'r')
lines = input.readlines()

class Directory(object):
    name = ""
    files = []
    size = 0

    def __init__(self, name, size = 0):
        self.name = name
        self.size = size
        self.files = []

    def add_file(self, file):
        self.files.append(file)
    
    def add_directory(self, directory):
        self.files.append(directory)
    
    def get_dir(self, name):
        for file in self.files:
            if file.name == name and type(file) == Directory:
                return file
        return None

    #calculate size of directory
    def calc_size(self):
        # self.size = 0
        for file in self.files:
            if type(file) == Directory:
                file.calc_size()
                self.size += file.size
            else:
                self.size += file.size

    # sum directories with size <= 100000
    def sum_dir(self):
        sum = 0
        for file in self.files:
            if type(file) == Directory:
                sum += file.sum_dir()
                if file.size <= 100000:
                    sum += file.size
        return sum

class File(object):
    name = ""
    size = 0

    def __init__(self, name, size):
        self.name = name
        self.size = size

fs = Directory("/")
currentDir = [fs]

for line in lines:
    if line.startswith("$ cd "):
        # change directory!
        current = line.split(" ")[-1].strip()
        if current == "/":
            continue
        elif current == "..":
            # go up a directory
            currentDir.pop()
            continue

        # create directory
        newDir = currentDir[-1].get_dir(current)
        currentDir.append(newDir)
        
        continue
    elif line.startswith("$ ls"):
        # skip ls command
        continue
    elif line.startswith("dir"):
        # create directory
        newDir = Directory(line.split(" ")[-1].strip())
        currentDir[-1].add_directory(newDir)
        continue
    else:
        # create file
        line = line.split(" ")
        size = int(line[-2])
        name = line[-1].strip()
        newFile = File(name, size)
        # print(currentDir, newFile)
        currentDir[-1].add_file(newFile)
        continue
        
fs.calc_size()
print("Sum of the total sizes of directories <= 100000:", fs.sum_dir())
