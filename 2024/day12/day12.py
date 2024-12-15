SQ_OUT_OF_BOUNDS = "."

class Board:
    def __init__(self, inputText) -> None:
        self.contents = inputText.split("\n")[:-1]

        self.width = len(self.contents[0])
        self.height = len(self.contents)

    def getChar(self, x, y):
        if (0 <= x < self.width) and \
           (0 <= y < self.height):
            return self.contents[y][x]
        return SQ_OUT_OF_BOUNDS

dirs = [
    ( 0, -1), #up
    (+1,  0), #right
    ( 0, +1), #down
    (-1,  0), #left
]

def getRegions(board):
    visited = set() #set of coordinates already assigned to a region
    regions = []
    for startY in range(board.height):
        for startX in range(board.width):
            if (startX, startY) in visited: #this square is in a region that's already been written down, skip it
                continue

            #new region, explore it with BFS
            regionLetter = board.getChar(startX, startY)
            regionCoords = set()

            explore = set()
            explore.add((startX, startY))
            regionCoords.add((startX, startY))
            visited.add((startX, startY))
            regionArea = 1
            regionPerimiter = 0

            while len(explore) > 0:

                #all available squares from the currently visited ones
                nextExplore = set()
                for exploreX, exploreY in explore:
                    for dx, dy in dirs:
                        newX, newY = exploreX + dx, exploreY + dy
                        if (newX, newY) in regionCoords:
                            continue

                        if board.getChar(newX, newY) == regionLetter:
                            nextExplore.add((newX, newY))
                            regionCoords.add((newX, newY))
                            visited.add((newX, newY))

                            regionArea += 1
                        else:
                            regionPerimiter += 1

                explore = nextExplore

            regions += [(regionLetter, regionCoords, regionArea, regionPerimiter)]
    return regions

def partA(inputText):
    board = Board(inputText)
    
    regions = getRegions(board)

    total = 0
    for regionLetter, regionCoords, regionArea, regionPerimiter in regions:
        total += regionArea * regionPerimiter

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
print("Example partA", partA(inputText)) #1930
#print("Example partB", partB(inputText))

inputText = readFile("input.txt")
print("partA", partA(inputText)) #1359028
#print("partB", partB(inputText))
