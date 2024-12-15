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

dirs = [
    ( 0, -1), #up
    (+1,  0), #right
    ( 0, +1), #down
    (-1,  0), #left
]
class Robots:
    def __init__(self, inputText, example = False):
        self.robots = parseRobots(inputText)

        if example:
            self.width, self.height = 11, 7
        else:
            self.width, self.height = 101, 103

        #unzip position/velocity
        self.robotsPos = []
        self.robotsVel = []
        for (px, py), (vx, vy) in self.robots:
            self.robotsPos+= [(px, py)]
            self.robotsVel += [(vx, vy)]
    
    #simulate 1 step
    def simulate(self):
        for i in range(len(self.robotsPos)):
            px, py = self.robotsPos[i]
            vx, vy = self.robotsVel[i]
            px = (px + vx) % self.width
            py = (py + vy) % self.height
            self.robotsPos[i] = (px, py)

    def show(self):
        printStr = ""
        for y in range(self.height):
            for x in range(self.width):
                count = self.robotsPos.count((x, y))

                if count == 0:
                    countStr = "."
                elif count > 9:
                    countStr = "X"
                else:
                    countStr = str(count)

                printStr += countStr
            printStr += "\n"

        print(printStr[:-1])

    def hasOverlap(self):
        return len(self.robotsPos) != len(set(self.robotsPos))
    
    def nBorderingSquares(self):
        count = 0
        for x, y in self.robotsPos:
            for dx, dy in dirs:
                if (x + dx, y + dy) in self.robotsPos:
                    count += 1

        return count


#strategies:
# simulate until no overlap - assume the tree picture was drawn with no overlapping bots
# look for large contigious areas:
#  I noticed that nBorderingSquares returned a score of over 200 for generations 97 + 101 * N,
#   and 50 + 103 * N, where N is an integer
#  (possible optimisation could have been to simulate 103 steps in one go instead of one at a time)
#  (another possible optimisation would have been to keep track of the max border score and only display when a new maximum has been found)

# first, I looked at the patterns in cases when the nBorderingSquares score was >200
#   there was a horizontal pattern visible in steps seperated by multiples of 101 (this proved irelevant later)
#   there was a vertical pattern visible in steps seperated by multiples of 103
#     e.g. I noted down 4376, 4685, 5097, 5200, 5652 which I though looked interesting,
#          the time step differences were 309, 412, 103, 452,
#          which were multiples of 103 (except the last one, which was disregarded)
#          with an offset of 50 (4376 % 103 = 50)
# then I started printing out just the steps that can be written in the form 50 + 103 * N
# manually looking through a couple, I found the tree

def partB(inputText, example = False):
    robots = Robots(inputText, example)

    #robots.show()
    #print()
    for i in range(1, 10000):
        robots.simulate()

        if i % 103 == 50 and not robots.hasOverlap():
            count = robots.nBorderingSquares()
            print(i, count)
            robots.show()

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
#print("Example partA", partA(inputText, example=True))
#print("Example partB", partB(inputText, example=True))

inputText = readFile("input.txt")
#print("partA", partA(inputText))
print("partB", partB(inputText))
