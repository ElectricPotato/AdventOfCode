'''

'''

def parse(inputText):
    orderingRulesText, pageNoListsText = inputText.rstrip().split("\n\n")

    orderingRules = [list(map(int, ruleText.split("|"))) for ruleText in orderingRulesText.split("\n")]
    pageNoLists = [list(map(int, listText.split(","))) for listText in pageNoListsText.split("\n")]

    return (orderingRules, pageNoLists)

def isOrdered(pageNoList, orderingRules):
    for pageA, pageB in orderingRules:
        if pageA in pageNoList and pageB in pageNoList:
            if pageNoList.index(pageA) > pageNoList.index(pageB):
                return False
    return True

def fixOrdering(pageNoList, orderingRules): #TODO
    relevantRules = [[pageA, pageB] for pageA, pageB in orderingRules if pageA in pageNoList and pageB in pageNoList]

    newPageNoList = []
    while len(relevantRules) > 0:
        pagesFrom, pagesTo = map(set, zip(*relevantRules)) #make a list of unique pages that appear in the from/to sections of all rules
        #get the page that no other page points to (it only appears in pagesFrom, but not pagesTo)
        nextPage = list(pagesFrom - pagesTo)[0]
        assert len(list(pagesFrom - pagesTo)) == 1
        
        #remove rules with startPage in the 'from' field
        relevantRules = [[pageFrom, pageTo] for pageFrom, pageTo in relevantRules if pageFrom != nextPage]

        newPageNoList += [nextPage]
    
    return newPageNoList

def partA(inputText):
    orderingRules, pageNoLists = parse(inputText)

    total = 0
    for pageNoList in pageNoLists:
        if isOrdered(pageNoList, orderingRules):
            #add middle page
            total += pageNoList[len(pageNoList) // 2]

    return total

def partB(inputText):
    orderingRules, pageNoLists = parse(inputText)

    total = 0
    for pageNoList in pageNoLists:
        if not isOrdered(pageNoList, orderingRules):
            pageNoList = fixOrdering(pageNoList, orderingRules)

            assert isOrdered(pageNoList, orderingRules), "ordering not corrected"
            total += pageNoList[len(pageNoList) // 2]

    return total



import os

def readFile(fileName):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )
    with open(os.path.join(__location__, fileName), "r") as inputFile:
        inputText = inputFile.read()
    return inputText

inputTextExample = readFile("einput.txt")
inputText = readFile("input.txt")

resultA = partA(inputTextExample)
print("Example partA", resultA)
assert resultA == 143

print("partA", partA(inputText))


resultB = partB(inputTextExample)
print("Example partB", resultB)
assert resultB == 123

print("partB", partB(inputText))
