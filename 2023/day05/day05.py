'''

seed, soil, fertilizer, water, light, temperature, location

'''
def parse(inputText):
    seedsStr, *maps = inputText.split("\n\n")
    seeds = list(map(int, seedsStr[len("seeds: "):].split()))

    parsedMaps = []
    for currentMap in maps:
        title, *lines = currentMap.split("\n")

        conversionRanges = []
        for line in lines:
            rangeBStart, rangeAStart, rangeLength = map(int, line.split())
            #conversionRange = (range A Start, range A End, amount to add to get from range A to range B)
            conversionRange = (rangeAStart, rangeAStart + rangeLength - 1, rangeBStart - rangeAStart)

            conversionRanges += [conversionRange]

        parsedMaps += [conversionRanges]

    return (seeds, parsedMaps)

def partA(inputText):
    seeds, maps = parse(inputText)
    
    locations = []
    for seed in seeds:
        trace = seed

        for currentMap in maps:
            for rangeAStart, rangeAEnd, increment in currentMap:
                if(rangeAStart <= trace <= rangeAEnd):
                    trace += increment
                    break

        locations += [trace]

    return min(locations)

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
