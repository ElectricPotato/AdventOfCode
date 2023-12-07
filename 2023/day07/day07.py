'''

'''

def parse(inputText):
    parsed = []
    for line in inputText.split("\n"):
        hand, bid = line.split()
        parsed += [(hand, int(bid))]

    return parsed


def groupCards(hand):
    groups = {}
    for card in hand:
        if card in groups:
            groups[card] += 1
        else:
            groups[card] = 1

    return groups

def getHandType(hand):
    groupSizes = sorted(groupCards(hand).values())

    handType = 0
    if(5 in groupSizes):
        handType = 6
    elif(4 in groupSizes):
        handType = 5
    elif(3 in groupSizes and 2 in groupSizes):
        handType = 4
    elif(3 in groupSizes):
        handType = 3
    elif(sum(g == 2 for g in groupSizes) == 2):
        handType = 2
    elif(2 in groupSizes):
        handType = 1
    else:
        handType = 0

    return handType

def cardValues(hand):
    return ["23456789TJQKA".index(c) for c in hand]


def partA(inputText):
    hands = parse(inputText)

    hands.sort(key=lambda x: (getHandType(x[0]), cardValues(x[0])))    

    total = 0
    for i, (hand, bid) in enumerate(hands, start = 1):
        total += i * bid

    return total


def cardValuesB(hand):
    return ["J23456789TQKA".index(c) for c in hand]

def mostCommonCard(hand): #apart from 'J'
    cards = groupCards(hand).items()
    cards = [card for card in cards if card[0] != 'J'] #filter out joker
    #filter out cards not tied for most common
    cards = [card for card in cards if card[1] == max(cards, key = lambda x: x[1])[1]]
    if(len(cards) == 0):
        maxValueCard = 'A'
    else:
        maxValueCard = max(cards, key = lambda x: cardValuesB(x[0]))[0]
    
    return maxValueCard
    
def replaceJoker(hand):
    return hand.replace('J', mostCommonCard(hand))

def partB(inputText):
    hands = parse(inputText)

    for hand, bid in hands:
        #if('J' in hand):print(hand, replaceJoker(hand))
        if('J' in hand and hand != 'JJJJJ'):
            assert(getHandType(replaceJoker(hand)) > getHandType(hand))

    hands.sort(key=lambda x: (getHandType(replaceJoker(x[0])), cardValuesB(x[0])))    

    total = 0
    for i, (hand, bid) in enumerate(hands, start = 1):
        total += i * bid

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

#A 248179786
#B 247885995