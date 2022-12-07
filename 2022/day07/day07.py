'''

'''

class Directory:

    def __init__(self, contents):
        self.contents = contents
        self.size = 0

def partA(inputText):
    lines=inputText.split("\n")
    n = 0
    cd = []
    fileSys = Directory({})
    allDirs = [(cd, fileSys)]
    while(n < len(lines)):
        if(lines[n][:4] == "$ cd"):
            dir = lines[n][5:]
            if(dir == ".."):
                cd = cd[:-1]
            elif(dir == "/"):
                cd = []
            else:
                cd += [dir]

            n+=1
        if(lines[n][:4] == "$ ls"):
            n+=1
            path = [fileSys]
            for dirName in cd:
                path += [path[-1].contents[dirName]]

            currentDir = path[-1]

            if(currentDir.contents == {}):
                while(n < len(lines) and lines[n][0] != "$"):
                    size, name = lines[n].split()
                    if(size == "dir"):
                        newDir = Directory({})
                        currentDir.contents.update({name: newDir})
                        allDirs.append((cd + [name], newDir))
                    else:
                        size = int(size)
                        currentDir.contents.update({name: size})

                        for dir in path:
                            dir.size += size

                    n+=1
            else:
                print(f"{dirName} already seen")

    total = 0
    for name, dir in allDirs:
        print(f"{name} {dir.size} {dir.contents}")
        if(dir.size <= 100000):
            total += dir.size

    return total

def partB(inputText):
    lines=inputText.split("\n")
    n = 0
    cd = []
    fileSys = Directory({})
    allDirs = [(cd, fileSys)]
    while(n < len(lines)):
        if(lines[n][:4] == "$ cd"):
            dir = lines[n][5:]
            if(dir == ".."):
                cd = cd[:-1]
            elif(dir == "/"):
                cd = []
            else:
                cd += [dir]

            n+=1
        if(lines[n][:4] == "$ ls"):
            n+=1
            path = [fileSys]
            for dirName in cd:
                path += [path[-1].contents[dirName]]

            currentDir = path[-1]

            if(currentDir.contents == {}):
                while(n < len(lines) and lines[n][0] != "$"):
                    size, name = lines[n].split()
                    if(size == "dir"):
                        newDir = Directory({})
                        currentDir.contents.update({name: newDir})
                        allDirs.append((cd + [name], newDir))
                    else:
                        size = int(size)
                        currentDir.contents.update({name: size})

                        for dir in path:
                            dir.size += size

                    n+=1
            else:
                print(f"{dirName} already seen")

    spaceNeeded = 30000000 - (70000000 - fileSys.size)
    total = 0
    candidates = []
    for name, dir in allDirs:
        if(dir.size >= spaceNeeded):
            print(f"{name} {dir.size} {dir.contents}")
            candidates += [dir.size]

    candidates.sort()

    return candidates[0]



import os

def readFile(fileName):
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, "input.txt"), "r") as inputFile:
        inputText = inputFile.read()

    return inputText

inputText = readFile("input.txt")
#print("Example partA", partA(inputText))

print("Example partB", partB(inputText))


'''inputText = readFile("input.txt")
print("partA", partA(inputText))
print("partB", partB(inputText))
'''