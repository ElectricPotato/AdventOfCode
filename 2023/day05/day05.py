'''

seed, soil, fertilizer, water, light, temperature, location

'''

#note all ranges in this program are inclusive on both sides - (1,3) means 1, 2, 3

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


def rangeOverlap(rangeA_start, rangeA_end, rangeB_start, rangeB_end):
    start = max(rangeA_start, rangeB_start)
    end = min(rangeA_end, rangeB_end)
    if(end < start):
        return None
    else:
        return (start, end)
    
#subtract range B from range A, A - B
def rangeSubtract(rangeA_start, rangeA_end, rangeB_start, rangeB_end):
    # A is completely inside B
    #     AAAA 
    # BBBBBBBBBBB
    if(rangeB_start <= rangeA_start and rangeA_end <= rangeB_end):
        return None
    
    # B is completely inside A
    # AAAAAAAAAAA
    #     BBBB
    # AAAA    AAA <- result
    if(rangeA_start < rangeB_start and rangeB_end < rangeA_end):
        return [(rangeA_start, rangeB_start - 1), (rangeB_end + 1, rangeA_end)]
    
    # B is on left of A
    # AAAAAAAA
    #     BBBBB
    # AAAA     <- result
    if(rangeA_start < rangeB_start <= rangeA_end and rangeA_end < rangeB_end):
        return [(rangeA_start, rangeB_start - 1)]

    # B is on right of A
    #  AAAAAAA
    # BBBBB
    #      AAA <- result
    if(rangeB_start < rangeA_start and rangeA_start <= rangeB_end < rangeA_end):
        return [(rangeB_end + 1, rangeA_end)]

    #not overlapping
    #      AA
    # BBBB
    #      AA <- result
    return [(rangeA_start, rangeA_end)]

def subtractRanges(rangeA, rangesB):
    ranges = [rangeA]
    nextRanges = []
    for rangeB_start, rangeB_end in rangesB:
        for rangeA_start, rangeA_end in ranges:
            newRanges = rangeSubtract()
    rangeA_start, rangeA_end = rangeA

def partB(inputText):
    seeds, maps = parse(inputText)
    seedRanges = [(seeds[i], seeds[i] + seeds[i+1] - 1) for i in range(0, len(seeds), 2)]
    for seedRange in seedRanges:

        traceRanges = [seedRange]
        nextRanges = []
        for currentMap in maps:
            for traceRangeStart, traceRangeEnd in traceRanges:
                for rangeAStart, rangeAEnd, increment in currentMap:
                    overlap = rangeOverlap(rangeAStart, rangeAEnd, traceRangeStart, traceRangeEnd)
                    if(overlap == None):
                        continue
                    overlapStart, overlapEnd = overlap
                    nextRanges += [(overlapStart + increment, overlapEnd + increment)]
            traceRanges = list(nextRanges)
            nextRanges = []
            print(traceRanges)
        print("---")



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
