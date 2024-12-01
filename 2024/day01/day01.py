'''

'''

def parseA(inputText):
    lines = inputText.split("\n")[:-1]
    parsed = [map(int, line.split()) for line in lines]
    unzipped = [list(t) for t in zip(*parsed)]

    return unzipped

def partA(inputText):
    leftList, rightList = map(sorted, parseA(inputText))
    distances = [abs(l - r) for l, r in zip(leftList, rightList)]

    return sum(distances)

def frequencyTable(l):
    freqDict = {}
    for i in l:
        if i in freqDict:
            freqDict[i] += 1
        else:
            freqDict[i] = 1

    return freqDict

def dictLookup(d, i):
    if i not in d: return 0
    return d[i]

def partB(inputText):
    leftList, rightList = map(sorted, parseA(inputText))
    freqDict = frequencyTable(rightList)

    return sum([i * dictLookup(freqDict, i) for i in leftList])



import os

def readFile(fileName):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )
    with open(os.path.join(__location__, fileName), "r") as inputFile:
        inputText = inputFile.read()
    return inputText

inputText = readFile("einput.txt")
print("Example partA", partA(inputText))
print("Example partB", partB(inputText))

inputText = readFile("input.txt")
print("partA", partA(inputText))
print("partB", partB(inputText))
