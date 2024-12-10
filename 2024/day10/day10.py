'''

'''

SQ_OUT_OF_BOUNDS = -1

class Board:
    def __init__(self, inputText) -> None:
        lines = inputText.split("\n")[:-1]
        self.contents = [list(map(int, line)) for line in lines]

        self.width = len(self.contents[0])
        self.height = len(self.contents)

    def getChar(self, x, y):
        if (0 <= x < self.width) and \
           (0 <= y < self.height):
            return self.contents[y][x]
        return SQ_OUT_OF_BOUNDS
    
    def findChars(self, c) -> list[tuple[int, int]]:
        coords = []
        for y in range(self.height):
            for x in range(self.width):
                if self.contents[y][x] == c:
                    coords += [(x, y)]
        return coords

dirs = [
    ( 0, -1), #up
    (+1,  0), #right
    ( 0, +1), #down
    (-1,  0), #left
]

def partA(inputText):
    board = Board(inputText)
    trailheads = board.findChars(0)

    total = 0
    for trailheadX, trailheadY in trailheads:
        squares = set()
        squares.add((trailheadX, trailheadY))

        for mountainHeight in range(9):

            #all available squares from the currently visited ones
            nextSquares = set()
            for x, y in squares:
                for dx, dy in dirs:
                    newX, newY = x + dx, y + dy
                    if board.getChar(newX, newY) == mountainHeight + 1:
                        nextSquares.add((newX, newY))

            squares = nextSquares

        total += len(squares)

    return total

def nPaths(board, currentHeight, x, y):
    if currentHeight == 9:
        return 1
    
    total = 0
    for dx, dy in dirs:
        newX, newY = x + dx, y + dy
        if board.getChar(newX, newY) == currentHeight + 1:
            total += nPaths(board, currentHeight + 1, newX, newY)
            
    return total

def partB(inputText):
    board = Board(inputText)
    trailheads = board.findChars(0)

    total = 0
    for trailheadX, trailheadY in trailheads:
        total += nPaths(board, 0, trailheadX, trailheadY)

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
