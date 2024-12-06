'''

'''

SQ_OUT_OF_BOUNDS = "x"
SQ_GUARD_START = "^"
SQ_EMPTY = "."
SQ_OBSTACLE = "#"

class Board:
    def __init__(self, lines) -> None:
        self.contents = lines

        self.width = len(lines)
        self.height = len(lines[0])

    def getChar(self, x, y):
        if (0 <= y < self.width) and \
           (0 <= x < self.height):
            return self.contents[y][x]
        return SQ_OUT_OF_BOUNDS
    
    #find the first character matching c, scanning left to right, top to bottom
    def findChar(self, c) -> tuple[int, int]:
        for y in range(self.width):
            for x in range(self.height):
                if self.contents[y][x] == c:
                    return (x, y)

class Guard:
    def visit(self, x, y):
        self.x, self.y = x, y
        self.visited.add((self.x, self.y))

    def __init__(self, board : Board):
        self.board = board
        self.visited : set[tuple[int, int]] = set() #set of coordinates
        self.rot : int = 0 #0 is up

        self.visit(*self.board.findChar(SQ_GUARD_START))

    #attempt to move the guard
    #return if the move was still in bounds
    def move(self) -> bool:
        dirs = [
            ( 0, -1), #up
            (+1,  0), #right
            ( 0, +1), #down
            (-1,  0), #left
        ]

        dx, dy = dirs[self.rot]
        nextX, nextY = self.x + dx, self.y + dy

        nextSpace = self.board.getChar(nextX, nextY)
        if nextSpace == SQ_EMPTY or nextSpace == SQ_GUARD_START:
            #step forward
            self.visit(nextX, nextY)
        elif nextSpace == SQ_OBSTACLE:
            #rotate 90 deg right
            self.rot = (self.rot + 1) % 4
        elif nextSpace == SQ_OUT_OF_BOUNDS:
            return False
        
        return True


def partA(inputText):
    lines=inputText.split("\n")[:-1]
    board = Board(lines)
    guard = Guard(board)

    while True:
        if not guard.move():
            break

    return len(guard.visited)

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

inputTextExample = readFile("einput.txt")
inputText = readFile("input.txt")

resultA = partA(inputTextExample)
print("Example partA", resultA)
assert resultA == 41

print("partA", partA(inputText))


resultB = partB(inputTextExample)
print("Example partB", resultB)
#assert resultB == 6

print("partB", partB(inputText))
