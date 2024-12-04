'''

'''

dirs = [
    ( 1,  0),
    ( 1,  1),
    ( 0,  1),
    (-1,  1),
    (-1,  0),
    (-1, -1),
    ( 0, -1),
    ( 1, -1)
]

def partA(inputText):
    lines=inputText.split("\n")[:-1]

    total = 0
    #for each starting poisition
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            #search in all 8 directions
            for dx, dy in dirs:
                found = True
                for i, c in enumerate("XMAS"):
                    cx, cy = y + dy * i, x + dx * i
                    if not ((0 <= cy < len(lines)) and \
                            (0 <= cx < len(lines[0])) and \
                            (lines[cy][cx] == c)):
                        found = False
                        break

                if found:
                    total += 1

    return total

def partB(inputText):
    lines=inputText.split("\n")
    for line in lines:
        pass

    return 1



import os

def readFile(fileName):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )
    with open(os.path.join(__location__, fileName), "r") as inputFile:
        inputText = inputFile.read()
    return inputText

inputText = readFile("einput.txt")
print("Example partA", partA(inputText))
print("Example partB", partB(inputText))

inputText = readFile("input.txt")
print("partA", partA(inputText))
print("partB", partB(inputText))
