'''

'''

def parse(inputText):
    timeStr, distStr = inputText.split("\n")
    return list(zip(
        map(int,timeStr.split()[1:]),
        map(int,distStr.split()[1:])
        ))

def partA(inputText):
    races = parse(inputText)

    product = 1
    for time, dist in races:
        product *= sum((time - buttonTime) * buttonTime > dist for buttonTime in range(time + 1))

    return product

def parseB(inputText):
    timeStr, distStr = inputText.split("\n")
    time = int(timeStr.split(":")[1].replace(" ", ""))
    dist = int(distStr.split(":")[1].replace(" ", ""))
    return (time, dist)


'''
t = total time, x = button time, d = distance
(t - x)x = d
tx - x^2 = d
tx - x^2 - d = 0
-x^2 + tx - d = 0

quadratic formula
format: ax^2 + bx + c = 0
        a = -1, b = t, c = -d
x = (-b +- sqrt(b^2 - 4ac)) / (2a)
x = (-t +- sqrt(t^2 - 4(-1)(-d))) / (2(-1))
x = (t +- sqrt(t^2 - 4d)) / 2
'''

import math
def partB(inputText):
    time, dist = parseB(inputText)
    buttonTime1 = (time - (time ** 2 - 4 * dist) ** 0.5) / 2
    buttonTime2 = (time + (time ** 2 - 4 * dist) ** 0.5) / 2

    return math.floor(buttonTime2) - math.ceil(buttonTime1) + 1



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
