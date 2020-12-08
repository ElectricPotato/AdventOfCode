'''

'''

def parseText(inputText):
    inputText = inputText.replace(" bags","").replace(" bag","").replace(".","")
    fullDict = {}
    for line in inputText.split("\n"):
        subject, relationText = line.split(" contain ")
        relationList = []
        for item in relationText.split(", "):
            words = item.split()
            if(words[0] != "no"):
                quantity = int(words[0])
                colour = words[1] + " " + words[2]
                relationList.append((quantity,colour))
        fullDict[subject] = relationList
    return fullDict


def reverseGraph(inputDict):
    #split relations
    relationList = []
    for key in inputDict.keys():
        val = inputDict[key]
        for item in val:
            relationList.append((key,item[1]))
    #recombine
    newDict = {}
    for relation in relationList:
        if(relation[1] in newDict):
            newDict[relation[1]] += [relation[0]]
        else:
            newDict[relation[1]] = [relation[0]]

    return newDict

def getColours(graphDict, currentColour):
    if(currentColour in graphDict):
        return {currentColour}.union(*[getColours(graphDict, colour) for colour in graphDict[currentColour]])
    else:
        return {currentColour}


def countBags(graphDict, currentColour):
    s = 1
    for quantity, colour in graphDict[currentColour]:
        s += quantity * countBags(graphDict, colour)
    return s

def partA(inputText):
    relationDict = parseText(inputText)
    reverseDict = reverseGraph(relationDict)
    #traverse graph recursively
    return len(getColours(reverseDict, "shiny gold") - {"shiny gold"})


def partB(inputText):
    relationDict = parseText(inputText)
    return countBags(relationDict, "shiny gold") - 1



inputFile = open("input.txt", "r")
inputText = inputFile.read()

#print("partA", partA(inputText))
print("partB", partB(inputText))