'''

'''

def parse(inputText):
    line = inputText.split("\n")[0]
    return list(map(int, line.split()))

def partA(inputText):
    stones = parse(inputText)

    for i in range(25):
        newStones = []
        for stone in stones:
            if stone == 0:
                newStones += [1]
            elif len(str(stone)) % 2 == 0:
                strStone = str(stone)
                halfway = len(strStone)//2
                
                newStones += [int(strStone[:halfway]), int(strStone[halfway:])]
            else:
                newStones += [stone * 2024]

        stones = newStones

    return len(stones)

def addCount(d, stone, count):
    if stone in d:
        d[stone] += count
    else:
        d[stone] = count


#Optimisation for part B:
# a dict is used to store the number of times each value appears in the list
def partB(inputText):
    stones = parse(inputText)

    stonesDict = {stone: 1 for stone in stones}

    for i in range(75):
        newStones = {}
        for stone, count in stonesDict.items():
            if stone == 0:
                addCount(newStones, 1, count)
            elif len(str(stone)) % 2 == 0:
                strStone = str(stone)
                halfway = len(strStone)//2

                addCount(newStones, int(strStone[:halfway]), count)
                addCount(newStones, int(strStone[halfway:]), count)
            else:
                addCount(newStones, stone * 2024, count)

        stonesDict = newStones

    return sum(stonesDict.values())



import os

def readFile(fileName):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )
    with open(os.path.join(__location__, fileName), "r") as inputFile:
        inputText = inputFile.read()
    return inputText

inputText = readFile("einput.txt")
print("Example partA", partA(inputText)) #55312
print("Example partB", partB(inputText))

inputText = readFile("input.txt")
print("partA", partA(inputText)) #197357
print("partB", partB(inputText)) #234568186890978