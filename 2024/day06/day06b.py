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
                
    def show(self): #DEBUG
        for line in self.contents:
            print(''.join(line))

class Guard:
    #add a state of the guard (the position and rotation) to the list of previous states
    #return True if the state has been seen before (implying a loop)
    def visit(self, x, y) -> bool:
        self.x, self.y = x, y

        if (self.x, self.y, self.rot) in self.visited:
            return True
        
        self.visited.add((self.x, self.y, self.rot))
        return False

    def __init__(self, board : Board):
        self.board = board
        self.startX, self.startY = self.board.findChar(SQ_GUARD_START)

        self.reset()
        

    def reset(self):
        self.visited : set[tuple[int, int]] = set() #set of coordinates
        self.rot : int = 0 #0 is up

        self.visit(self.startX, self.startY)

    #move the guard until she reaches a loop or goes out of bounds
    #return True if a loop if found
    def simulateToEnd(self) -> bool:
        dirs = [
            ( 0, -1), #up
            (+1,  0), #right
            ( 0, +1), #down
            (-1,  0), #left
        ]

        while True:
            dx, dy = dirs[self.rot]
            nextX, nextY = self.x + dx, self.y + dy

            nextSpace = self.board.getChar(nextX, nextY)
            if nextSpace == SQ_EMPTY or nextSpace == SQ_GUARD_START:
                #step forward
                if self.visit(nextX, nextY):
                    return True #loop found
            elif nextSpace == SQ_OBSTACLE:
                #rotate 90 deg right
                self.rot = (self.rot + 1) % 4
            elif nextSpace == SQ_OUT_OF_BOUNDS:
                return False #loop not found
        

#brute force solution by placing an obstacle on each square one by one
#can be made more efficient by only trying squares in the original path of the guard
def partB(inputText):
    lines=list(map(list, inputText.split("\n")[:-1]))
    board = Board(lines)
    guard = Guard(board)

    possiblePositions = []
    for y in range(board.width):
        for x in range(board.height):
            if board.getChar(x, y) != SQ_EMPTY: #only try empty squares
                continue

            guard.reset() #reset position/rotation and visited squares
            #add an obstacle
            guard.board.contents[y][x] = SQ_OBSTACLE

            if guard.simulateToEnd():
                print(f"found position {(x, y)}")
                possiblePositions += [(x, y)]
            
            #clear obstacle
            guard.board.contents[y][x] = SQ_EMPTY
            
    
    return len(possiblePositions)



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

resultB = partB(inputTextExample)
print("Example partB", resultB)
assert resultB == 6

resultB = partB(inputText)
print("partB", resultB)
assert resultB == 1688