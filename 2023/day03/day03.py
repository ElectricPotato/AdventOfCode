'''

'''

def findParts(inputText):
    lines=inputText.split("\n")
    height = len(lines)
    width = len(lines[0])
    
    #find the coordinates of digits 1 space away from position (x,y), including diagonals 
    def findAdjacentDigits(x, y):
        convolutionDirections = \
            [(dx, dy) for dx in range(-1, 2) for dy in range(-1, 2) if not (dx == 0 and dy == 0)]
        
        adjacentDigitCoords = []
        for dx, dy in convolutionDirections:
            if(0 <= x + dx < width \
               and 0 <= y + dy < height \
               and lines[y+dy][x+dx].isdigit()):
                adjacentDigitCoords += [(x + dx, y + dy)]
        return adjacentDigitCoords
    
    #finds adjecent digits and combines them into a number
    def findNumber(x, y):
        xMin = x
        xMax = x
        while(0 <= xMin - 1 and lines[y][xMin - 1].isdigit()):
            xMin -= 1

        while(xMax + 1 < width and lines[y][xMax + 1].isdigit()):
            xMax += 1

        number = int(lines[y][xMin:xMax + 1])
        coords = [(xa, y) for xa in range(xMin, xMax + 1)]

        return (number, coords)

    parts = []
    for y in range(height):
        for x in range(width):
            char = lines[y][x]
            
            if(char == '.' or char.isdigit()):
                continue

            foundCoords = []
            numbers = []
            for adjX, adjY in findAdjacentDigits(x, y):
                if(adjX, adjY) in foundCoords:
                    continue

                number, coords = findNumber(adjX, adjY)
                foundCoords += coords

                numbers += [number]
            parts += [(char, numbers)]

    return parts

def partA(inputText):
    parts = findParts(inputText)
    return sum([sum(part[1]) for part in parts])

def partB(inputText):
    parts = findParts(inputText)
    return sum(
        partNumbers[0] * partNumbers[1]
        for partChar, partNumbers in parts
        if partChar == "*" and len(partNumbers) == 2
        )



import os

def readFile(fileName):
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, fileName), "r") as inputFile:
        inputText = inputFile.read()
    return inputText

inputText = readFile("einput.txt")
print("Example partA", partA(inputText))
print("Example partB", partB(inputText))

inputText = readFile("input.txt")
print("partA", partA(inputText))
print("partB", partB(inputText))
