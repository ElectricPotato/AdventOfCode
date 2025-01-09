'''

'''

SQ_OUT_OF_BOUNDS = "x"
SQ_ROBOT_START = "@"
SQ_EMPTY = "."
SQ_WALL = "#"

SQ_BOX_OLD = "O"

SQ_BOX_L = "["
SQ_BOX_R = "]"
SQ_BOX = SQ_BOX_L + SQ_BOX_R

dirs = {
    "^": ( 0, -1), #up
    ">": (+1,  0), #right
    "v": ( 0, +1), #down
    "<": (-1,  0), #left
}

class Board:
    def __init__(self, lines) -> None:
        lines = lines.replace(SQ_EMPTY, SQ_EMPTY * 2) \
                     .replace(SQ_WALL, SQ_WALL * 2) \
                     .replace(SQ_BOX_OLD, SQ_BOX) \
                     .replace(SQ_ROBOT_START, SQ_ROBOT_START + SQ_EMPTY)
        
        self.contents = list(map(list, lines.split("\n")))

        self.width = len(self.contents[0])
        self.height = len(self.contents)

    def getChar(self, x, y):
        if (0 <= y < self.height) and \
           (0 <= x < self.width):
            return self.contents[y][x]
        return SQ_OUT_OF_BOUNDS
    
    def setChar(self, x, y, c):
        self.contents[y][x] = c
    
    #find the first character matching c, scanning left to right, top to bottom
    def findChar(self, c) -> tuple[int, int]:
        for y in range(self.height):
            for x in range(self.width):
                if self.contents[y][x] == c:
                    return (x, y)
                
    def sumBoxes(self):
        total = 0
        for y in range(self.height):
            for x in range(self.width):
                if self.contents[y][x] == SQ_BOX:
                    total += 100 * y + x
        
        return total

class Robot:
    def __init__(self, inputText):
        lines, self.instructions = inputText.rstrip().split("\n\n")
        self.instructions = self.instructions.replace("\n", "")

        self.board = Board(lines)
        self.posX, self.posY = self.board.findChar(SQ_ROBOT_START)
        self.board.setChar(self.posX, self.posY, SQ_EMPTY)


    def move(self, instr):
        dx, dy = dirs[instr]
        newX, newY = self.posX + dx, self.posY + dy
        if self.board.getChar(newX, newY) == SQ_EMPTY:
            self.posX, self.posY = newX, newY
        elif self.board.getChar(newX, newY) == SQ_BOX:
            #raycast in the same direction until an empty space is found
            scanPosX, scanPosY = newX + dx, newY + dy

            while self.board.getChar(scanPosX, scanPosY) == SQ_BOX:
                scanPosX, scanPosY = scanPosX + dx, scanPosY + dy

            if self.board.getChar(scanPosX, scanPosY) == SQ_EMPTY:
                #move box and robot
                self.board.setChar(scanPosX, scanPosY, SQ_BOX)
                self.board.setChar(newX, newY, SQ_EMPTY)
                self.posX, self.posY = newX, newY
        #elif self.board.getChar(newX, newY) == SQ_WALL:
        #    pass #do nothing
        
    def runAllMoves(self):
        for instr in self.instructions:
            self.move(instr)

def partB(inputText):
    robot = Robot(inputText)
    robot.runAllMoves()
    
    return robot.board.sumBoxes()



import os

def readFile(fileName):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )
    with open(os.path.join(__location__, fileName), "r") as inputFile:
        inputText = inputFile.read()
    return inputText

inputText = readFile("einput.txt")
print("Example partB", partB(inputText))

inputText = readFile("einput2.txt")
print("Example partB", partB(inputText))

inputText = readFile("input.txt")
print("partB", partB(inputText))
