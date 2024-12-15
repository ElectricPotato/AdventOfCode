'''

'''

import parse

def parseRobots(inputText):
    lines=inputText[:-1].split("\n")
    
    parsed = []
    for line in lines:
        lineFormat = "p={:d},{:d} v={:d},{:d}"
        px, py, vx, vy = parse.parse(lineFormat, line).fixed
        parsed += [((px, py), (vx, vy))]

    return parsed

def partA(inputText, example = False):
    robots = parseRobots(inputText)

    if example:
        width, height = 11, 7
    else:
        width, height = 101, 103

    #calulate position of each robot 100 steps in the future
    futurePositions = []
    for (px, py), (vx, vy) in robots:
        for t in range(100):
            px = (px + vx) % width
            py = (py + vy) % height

        futurePositions += [(px, py)]

    #count robot in each quadrant
    quadrants = [0] * 4
    midX = (width - 1) / 2
    midY = (height - 1) / 2
    for x, y in futurePositions:
        if x > midX:
            if y > midY:
                quadrants[0] += 1
            elif y < midY:
                quadrants[1] += 1
        elif x < midX:
            if y > midY:
                quadrants[2] += 1
            elif y < midY:
                quadrants[3] += 1

    return quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3] 

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
print("Example partA", partA(inputText, example=True))
#print("Example partB", partB(inputText, example=True))

inputText = readFile("input.txt")
print("partA", partA(inputText))
#print("partB", partB(inputText))
