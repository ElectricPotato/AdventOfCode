'''

'''

def parse(inputText):
    lines=inputText.split("\n")

    parsed = []
    for line in lines:
        cardNStr, contents = line.split(":")
        cardN = int(cardNStr[len("Card "):])
        winningNumbersStr, givenNumbersStr = contents.split(" | ")

        winningNumbers = list(map(int, winningNumbersStr.split()))
        givenNumbers = list(map(int, givenNumbersStr.split()))
        
        parsed += [(cardN, winningNumbers, givenNumbers)]

    return parsed

def partA(inputText):
    cards = parse(inputText)

    total = 0
    for cardN, winningNumbers, givenNumbers in cards:
        matchingNumbers = sum([1 for winningNumber in winningNumbers if winningNumber in givenNumbers])

        if(matchingNumbers > 0):
            total += 2 ** (matchingNumbers - 1)

    return total

def partB(inputText):
    cards = parse(inputText)
    cardQuantities = [1] * len(cards)

    total = 0
    for i, (cardN, winningNumbers, givenNumbers) in enumerate(cards):
        matchingNumbers = sum([1 for winningNumber in winningNumbers if winningNumber in givenNumbers])

        for j in range(1, matchingNumbers + 1):
            cardQuantities[i + j] += cardQuantities[i]

    return sum(cardQuantities)



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
