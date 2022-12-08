'''

'''


def partA(inputText):
    lines=inputText.split("\n")
    total=0

    grid=[]
    for line in lines:
        grid += [list(map(int,line))]

    for x in range(len(grid[0])):
        for y in range(len(grid)):

            visible = False
            height = grid[y][x]
            
            for xDir, yDir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                newX, newY = x, y
                sideVisible = True
                newX += xDir
                newY += yDir

                while(newX in range(len(grid[0])) and newY in range(len(grid))):
                    if(grid[newY][newX] >= height):
                        sideVisible = False
                        break
                    newX += xDir
                    newY += yDir
                if(sideVisible):
                    visible = True
                    break
            if(visible):
                total += 1


    return total

def partB(inputText):
    lines=inputText.split("\n")
    maxScenicScore=0

    grid=[]
    for line in lines:
        grid += [list(map(int,line))]

    for x in range(len(grid[0])):
        for y in range(len(grid)):

            visible = False
            height = grid[y][x]
            sidesVisible = []
            
            for xDir, yDir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                newX, newY = x, y
                newX += xDir
                newY += yDir

                rayLength = 0
                while(newX in range(len(grid[0])) and newY in range(len(grid))):
                    rayLength += 1
                    if(grid[newY][newX] >= height):
                        break
                    newX += xDir
                    newY += yDir
                sidesVisible.append(rayLength)

            scenicScore = sidesVisible[0] * sidesVisible[1] * sidesVisible[2] * sidesVisible[3]
            maxScenicScore = max(maxScenicScore, scenicScore)


    return maxScenicScore



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
