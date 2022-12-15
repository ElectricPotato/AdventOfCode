'''

'''

def overlapOrTouching(minA, maxA, minB, maxB): #
    return (max(minA,maxA) <= min(maxA,maxB)) \
        or (minA == minB) or (minA == maxB) \
        or (maxA == minB) or (maxA == maxB)

def overlap(minA, maxA, minB, maxB):
    return (max(minA,maxA) <= min(maxA,maxB))

def combine(minA, maxA, minB, maxB): #boolean or
    return min(minA, minB), max(maxA, maxB)

def dist(xa, ya, xb, yb):
    return abs(xa-xb)+abs(ya-yb)

def addToGroup(rangeMin, rangeMax, allRanges):
    newRanges = []
    allOverlappingRanges = []
    for (rMin, rMax) in allRanges:
        if(overlapOrTouching(rangeMin, rangeMax, rMin, rMax)):
            allOverlappingRanges += [(rMin, rMax)]
        else:
            newRanges += [(rMin, rMax)]

    #increase range of (rangeMin, rangeMax) to overlap all the other ranges
    for (rMin, rMax) in allOverlappingRanges:
        rangeMin, rangeMax = combine(rangeMin, rangeMax, rMin, rMax)

    newRanges += [(rangeMin, rangeMax)]

    return newRanges

def rangeAnd(minA, maxA, minB, maxB): #boolean and
    if(not overlap(minA, maxA, minB, maxB)):
        return None

    return max(minA, minB), min(maxA, maxB)
    


def rangeLen(minA, maxA):
    return maxA - minA + 1

def partA(inputText, targetY):
    lines=inputText.split("\n")
    allRanges = []

    parsed = []
    for line in lines:
        line = line.replace("Sensor at x=","")
        line = line.replace(", y="," ")
        line = line.replace(": closest beacon is at x="," ")
        line = line.replace(", y="," ")
        xs, ys, xb, yb = [int(i) for i in line.split()]
        parsed += [(xs, ys, xb, yb)]

    allRanges = []
    for (xs, ys, xb, yb) in parsed:
        beaconDist = dist(xs, ys, xb, yb)

        dx = beaconDist - abs(targetY - ys)
        if(dx > 0):
            rMin, rMax = xs - dx, xs + dx
            allRanges += [(rMin, rMax)]

    allRangesCombined = []
    allRangesCombined += [allRanges[0]]
    for (rMin, rMax) in allRanges[1:]:
        allRangesCombined = addToGroup(rMin, rMax, allRangesCombined)

    uniqueBeacons = set((xb, yb) for (xs, ys, xb, yb) in parsed)
    beaconsAtTargetY = 0
    for (xb, yb) in uniqueBeacons:
        if(yb == targetY):beaconsAtTargetY+=1

    print()
    return sum(rangeLen(rMin, rMax) for (rMin, rMax) in allRangesCombined) - beaconsAtTargetY

def partB(inputText, maxXY):
    lines=inputText.split("\n")
    allRanges = []

    parsed = []
    for line in lines:
        line = line.replace("Sensor at x=","")
        line = line.replace(", y="," ")
        line = line.replace(": closest beacon is at x="," ")
        line = line.replace(", y="," ")
        xs, ys, xb, yb = [int(i) for i in line.split()]
        parsed += [(xs, ys, xb, yb)]

    #frequency = y + 4000000 * x
    #return frequency



import os

def readFile(fileName):
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, fileName), "r") as inputFile:
        inputText = inputFile.read()
    return inputText

inputText = readFile("einput.txt")
print("Example partA", partA(inputText, 10))
print("Example partB", partB(inputText, 20))

inputText = readFile("input.txt")
print("partA", partA(inputText, 2000000))
print("partB", partB(inputText, 4000000))


#A not 5316354