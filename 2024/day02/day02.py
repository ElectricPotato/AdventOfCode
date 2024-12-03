'''

'''


def partA(inputText):
    lines=inputText.split("\n")

    total = 0
    for line in lines:
        parsed = list(map(int, line.split()))
        if parsed == []:
            continue
        
        
        safe = True
        increasing = parsed[0] < parsed[1]
        for a, b in zip(parsed, parsed[1:]):
            if (increasing and (a > b)) \
                or (not increasing and (a < b)) \
                or not (1 <= abs(a - b) <= 3): #difference at least 1, at most 3
                safe = False
                break
        
        if safe:
            total += 1

    return total

def findFault(parsed):
    increasing = parsed[0] < parsed[1]
    for i, (a, b) in enumerate(zip(parsed, parsed[1:])):
        if (increasing and (a > b)) \
            or (not increasing and (a < b)) \
            or not (1 <= abs(a - b) <= 3): #difference at least 1, at most 3
            return i
    return -1

def partB(inputText):
    lines=inputText.split("\n")

    total = 0
    for line in lines:
        parsed = list(map(int, line.split()))
        if parsed == []:
            continue
        
        safe = True
        fault = findFault(parsed)
        if fault == -1:
            safe = True
        else:
            safe = False
            for i in range(-1, 2):
                if (fault + i) >= len(parsed): continue
                if (fault + i) < 0: continue
                newParsed = list(parsed)
                newParsed.pop(fault + i)
                if findFault(newParsed) == -1:
                    safe = True
                    break
            

        
        if safe:
            total += 1

    return total



import os

def readFile(fileName):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )
    with open(os.path.join(__location__, fileName), "r") as inputFile:
        inputText = inputFile.read()
    return inputText

inputText = readFile("einput.txt")
print("Example partA", partA(inputText)) #2
print("Example partB", partB(inputText)) #4

inputText = readFile("input.txt")
print("partA", partA(inputText)) #407
print("partB", partB(inputText)) #459
