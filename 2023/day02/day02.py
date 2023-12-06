'''

'''


def partA(inputText):
    posibleSet = {"red": 12, "green": 13, "blue": 14}

    total = 0
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

    #print(parsedList)

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
    lines=inputText.split("\n")
    for line in lines:
        pass

    return 1



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
#print("partB", partB(inputText))
