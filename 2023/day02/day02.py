'''

'''

def parsePuzzleInput(inputText):
    lines=inputText.split("\n")

    parsedList = []
    for line in lines:
        gameStr, contentsStr = line.split(": ")
        gameN = int(gameStr[len("Game "):])

        turnsList = []
        for turn in contentsStr.split("; "):
            turnDict = {}
            for item in turn.split(", "):
                itemQuantityStr, itemColour = item.split()
                itemQuantityInt = int(itemQuantityStr)
                turnDict[itemColour] = itemQuantityInt

            turnsList += [turnDict]

        parsedList += [(gameN, turnsList)]

    return parsedList

def partA(inputText):
    posibleSet = {"red": 12, "green": 13, "blue": 14}

    parsedList = parsePuzzleInput(inputText)
    #print(parsedList)

    total = 0
    for gameN, turnsList in parsedList:
        possible = True
        for turn in turnsList:
            for item, itemQuantity in turn.items():
                if(posibleSet[item] < itemQuantity):
                    possible = False
                    break

            if(not possible):
                break

        if(possible):
            total += gameN

    return total

def partB(inputText):
    posibleSet = {"red": 12, "green": 13, "blue": 14}

    parsedList = parsePuzzleInput(inputText)

    total = 0
    for gameN, turnsList in parsedList:
        minimumSet = {colour: 0 for colour in posibleSet.keys()}

        for turn in turnsList:
            for colour, quantity in turn.items():
                minimumSet[colour] = max(minimumSet[colour], quantity)

        power = 1
        for colour, quantity in minimumSet.items():
            power *= quantity

        total += power

    return total



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
