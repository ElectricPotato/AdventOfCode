'''

'''

def sgn(x):
    if(x>0):return 1
    if(x<0):return -1
    return 0

def partA(inputText):
    lines=inputText.split("\n")
    x, y = 0, 0
    tailx, taily = 0, 0
    allTailPositions = [(tailx, taily)]
    for line in lines:
        dir, n = line.split()
        n=int(n)
        xDir, yDir = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}[dir]
        for i in range(n):
            x += xDir
            y += yDir

            #update tail pos
            if( abs(x - tailx) > 1 or abs(y - taily) > 1 ):
                    tailx += sgn(x - tailx)
                    taily += sgn(y - taily)

            if((tailx, taily) not in allTailPositions):
                allTailPositions += [(tailx, taily)]

            #print( (x,y), (tailx, taily))

    return len(allTailPositions)

def partB(inputText):
    lines=inputText.split("\n")
    rope = [[0,0] for i in range(10)]
    allTailPositions = [[rope[-1][0], rope[-1][1]]]
    for line in lines:
        dir, n = line.split()
        n=int(n)
        xDir, yDir = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}[dir]
        for i in range(n):
            rope[0][0] += xDir
            rope[0][1] += yDir

            for i in range(1, len(rope)):
                if( abs(rope[i-1][0] - rope[i][0]) > 1 or abs(rope[i-1][1] - rope[i][1]) > 1 ):
                    rope[i][0] += sgn(rope[i-1][0] - rope[i][0])
                    rope[i][1] += sgn(rope[i-1][1] - rope[i][1])

            if([rope[-1][0], rope[-1][1]] not in allTailPositions):
                allTailPositions += [[rope[-1][0], rope[-1][1]]]

            #print( (x,y), (tailx, taily), allTailPositions)
            #print(rope)

    return len(allTailPositions)



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
