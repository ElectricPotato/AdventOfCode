'''

'''


def partA(inputText):
    for i in range(len(inputText)-3):
        if(len(set(inputText[i:i+4])) == 4):
            return i+4

def partB(inputText):
    for i in range(len(inputText)-13):
        if(len(set(inputText[i:i+14])) == 14):
            return i+14



import os

def readFile(fileName):
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, fileName), "r") as inputFile:
        inputText = inputFile.read()
    return inputText

inputText = readFile("einput.txt")
for line in inputText.split("\n"):
    print("Example partA", partA(line))

inputText = readFile("input.txt")
print("partA", partA(inputText)) 


inputText = readFile("einput.txt")
for line in inputText.split("\n"):
    print("Example partB", partB(line))

inputText = readFile("input.txt")
print("partB", partB(inputText)) 
