'''

'''


def partA(inputText):
    lines=inputText.split("\n")
    signalStrength = 0
    
    acc = 1
    cycle = 1
    for line in lines:
        splitLine = line.split()
        if(splitLine[0] == "noop"):
            cycle += 1
            if(cycle > 1 and (cycle - 20) % 40 == 0):
                signalStrength += acc * cycle

        elif(splitLine[0] == "addx"):
            arg = int(splitLine[1])
            cycle += 1
            if(cycle > 1 and (cycle - 20) % 40 == 0):
                signalStrength += acc * cycle

            acc += arg
            cycle += 1

            if(cycle > 1 and (cycle - 20) % 40 == 0):
                signalStrength += acc * cycle

    return signalStrength

def partA_alternate(inputText):
    lines=inputText.split("\n")
    signalStrength = 0
    
    acc = 1
    cycle = 1
    stage = 0
    i = 0
    arg = 0
    while(i in range(len(lines))):
        splitLine = lines[i].split()
        if(stage == 1):
            acc += arg
            i+=1
            stage = 0
        elif(splitLine[0] == "noop"):
            i+=1
        elif(splitLine[0] == "addx"):
            arg = int(splitLine[1])
            stage = 1

        cycle += 1

        if(cycle > 1 and (cycle - 20) % 40 == 0):
            signalStrength += acc * cycle

    return signalStrength

def partB(inputText):
    lines=inputText.split("\n")
    
    acc = 1
    cycle = 1
    stage = 0
    i = 0
    arg = 0
    screen = ""
    screen += ".#"[abs(cycle%40 - acc) <= 1]
    while(i in range(len(lines))):
        splitLine = lines[i].split()
        if(stage == 1):
            acc += arg
            i+=1
            stage = 0
        elif(splitLine[0] == "noop"):
            i+=1
        elif(splitLine[0] == "addx"):
            arg = int(splitLine[1])
            stage = 1

        cycle += 1

        screen += ".#"[abs((cycle-1)%40 - acc) <= 1]

    #insert newlines
    finalScreen = ""
    for i in range(6):
        finalScreen += screen[i*40:i*40+39] + "\n"

    return finalScreen

import os

def readFile(fileName):
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, fileName), "r") as inputFile:
        inputText = inputFile.read()
    return inputText

inputText = readFile("einput.txt")
print("Example partA", partA(inputText))
print("Example partB")
print(partB(inputText))

inputText = readFile("input.txt")
print("partA", partA(inputText))
print("partB")
print(partB(inputText))
