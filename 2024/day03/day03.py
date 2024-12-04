'''

'''
import re

def partA(inputText):
    lines=inputText.split("\n")

    pattern = re.compile(r'mul\((\d*),(\d*)\)')
    total = 0
    for line in lines:
        matches = pattern.finditer(line)
        for match in matches:
            n1, n2 = map(int, match.groups())
            total += n1 * n2

    return total

def partB(inputText):
    lines=inputText.split("\n")

    instrPatterns = [
        r'do\(\)',
        r'mul\((\d*),(\d*)\)',
        r'don\'t\(\)'
    ]

    pattern = re.compile('|'.join(instrPatterns))
    total = 0

    enabled = True
    for line in lines:
        matches = pattern.finditer(line)
        for match in matches:
            print(match.group())
            if match.group() == "do()":
                enabled = True
            elif match.group() == "don't()":
                enabled = False
            elif match.group()[:3] == "mul":
                if enabled:
                    n1, n2 = map(int, match.groups())
                    total += n1 * n2

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
print("Example partA", partA(inputText))
inputText = readFile("einputB.txt")
print("Example partB", partB(inputText))

inputText = readFile("input.txt")
print("partA", partA(inputText))
print("partB", partB(inputText))
