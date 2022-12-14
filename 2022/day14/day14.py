'''

'''
def printGrid(points, xSand, ySand):
    xMax = max(p[0] for p in points)
    xMin = min(p[0] for p in points)

    yMax = max(p[1] for p in points)
    yMin = min(p[1] for p in points)

    for y in range(yMin, yMax+1):
        line = ""
        for x in range(xMin, xMax+1):
            if([x,y] == [xSand, ySand]):
                line += "s"
            elif([x,y] in points):
                line += "#"
            else:
                line += "."
        print(line)


def sgn(x):
    if(x>0):return 1
    if(x<0):return -1
    return 0

def showPuzzle(inputText):
    points = []
    paths=inputText.split("\n")
    maxY = 0
    for path in paths:
        pathParsed = []
        for line in path.split(" -> "):
            x,y = line.split(",")
            x,y = int(x), int(y)
            pathParsed += [[x,y]]

            maxY = max(maxY, y)

        for pointA, pointB in zip(pathParsed, pathParsed[1:]):
            xA, yA = pointA
            xB, yB = pointB

            xDir, yDir = sgn(xB - xA), sgn(yB - yA)

            xCurr, yCurr = xA, yA
            points += [[xCurr, yCurr]]

            while(not(xCurr == xB and yCurr == yB)):
                xCurr, yCurr = xCurr + xDir, yCurr + yDir
                points += [[xCurr, yCurr]]

    points += [[500, 0]]
    printGrid(points, 500, 0)

def partA(inputText):
    points = []
    paths=inputText.split("\n")
    maxY = 0
    for path in paths:
        pathParsed = []
        for line in path.split(" -> "):
            x,y = line.split(",")
            x,y = int(x), int(y)
            pathParsed += [[x,y]]

            maxY = max(maxY, y)

        for pointA, pointB in zip(pathParsed, pathParsed[1:]):
            xA, yA = pointA
            xB, yB = pointB

            xDir, yDir = sgn(xB - xA), sgn(yB - yA)

            xCurr, yCurr = xA, yA
            points += [[xCurr, yCurr]]

            while(not(xCurr == xB and yCurr == yB)):
                xCurr, yCurr = xCurr + xDir, yCurr + yDir
                points += [[xCurr, yCurr]]

    sandGrains = 0
    sandHistory = [[500, 0]]
    while(True):
        xSand, ySand = sandHistory[-1]
        sandHistory = sandHistory[:-1]
        moved = True
        while(moved):
            moved = False
            for xDir, yDir in [[0,1], [-1,1], [1,1]]:
                if([xSand + xDir, ySand + yDir] not in points):
                    moved = True
                    sandHistory += [[xSand, ySand]]
                    xSand, ySand = xSand + xDir, ySand + yDir
                    break
            
            if(ySand > maxY):
                break
        
        if(moved == False):
            points += [[xSand, ySand]]
            sandGrains += 1
        else:
            break
    return sandGrains


def partB(inputText):
    points = set()
    paths=inputText.split("\n")
    maxY = 0
    for path in paths:
        pathParsed = []
        for line in path.split(" -> "):
            x,y = line.split(",")
            x,y = int(x), int(y)
            pathParsed += [[x,y]]

            maxY = max(maxY, y)

        for pointA, pointB in zip(pathParsed, pathParsed[1:]):
            xA, yA = pointA
            xB, yB = pointB

            xDir, yDir = sgn(xB - xA), sgn(yB - yA)

            xCurr, yCurr = xA, yA
            points.add((xCurr, yCurr))

            while(not(xCurr == xB and yCurr == yB)):
                xCurr, yCurr = xCurr + xDir, yCurr + yDir
                points.add((xCurr, yCurr))

    sandGrains = 0
    sandHistory = [[500, 0]] # previous position of sand grain before it stops moving
    while(True):
        xSand, ySand = sandHistory[-1]
        sandHistory = sandHistory[:-1]
        while(True):
            moved = False
            for xDir, yDir in [[0,1], [-1,1], [1,1]]:
                if((xSand + xDir, ySand + yDir) not in points):
                    moved = True
                    sandHistory += [(xSand, ySand)]
                    xSand, ySand = xSand + xDir, ySand + yDir
                    break

            if(not moved): break
            if(ySand == maxY + 1): break
        
        points.add((xSand, ySand))
        sandGrains += 1
        #if(sandGrains%100 == 0):print(sandGrains)

        
        if((xSand, ySand) == (500,0)):
            break

    #printGrid(points, xSand, ySand)

    return sandGrains



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
#showPuzzle(inputText)


inputText = readFile("input.txt")
print("partA", partA(inputText))
print("partB", partB(inputText)) #answer 29076
#showPuzzle(inputText)