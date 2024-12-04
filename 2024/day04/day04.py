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

class Board:
    def __init__(self, lines) -> None:
        self.contents = lines

        self.width = len(lines)
        self.height = len(lines[0])

    def getChar(self, y, x):
        if (0 <= y < self.width) and \
           (0 <= x < self.height):
            return self.contents[y][x]
        return "."

def partA(inputText):
    lines=inputText.split("\n")[:-1]
    board = Board(lines)

    total = 0
    #for each starting poisition
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            #search in all 8 directions
            for dx, dy in dirs:
                found = True
                for i, c in enumerate("XMAS"):
                    cx, cy = y + dy * i, x + dx * i
                    if board.getChar(cy, cx) != c:
                        found = False
                        break

                if found:
                    total += 1

    return total

def partB(inputText):
    lines=inputText.split("\n")[:-1]
    board = Board(lines)

    total = 0
    #for each starting poisition
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if (board.getChar(y + 1, x + 1) + board.getChar(y, x) + board.getChar(y - 1, x - 1)) in ['MAS', 'SAM'] and \
               (board.getChar(y + 1, x - 1) + board.getChar(y, x) + board.getChar(y - 1, x + 1)) in ['MAS', 'SAM']:
                total += 1

    return total



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
