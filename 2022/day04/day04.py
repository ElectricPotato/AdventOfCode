'''

'''


def partA(inputText):
    lines=inputText.split("\n")
    total=0

    for line in lines:
        ab, cd = line.split(",")
        a, b = ab.split("-")
        c, d = cd.split("-")
        a,b,c,d = int(a),int(b),int(c),int(d)
        if((max(a,b) >= max(c,d) and min(a,b) <= min(c,d)) or (max(c,d) >= max(a,b) and min(c,d) <= min(a,b))):
            total+=1

    return total

def partB(inputText):
    lines=inputText.split("\n")
    total=0

    for line in lines:
        ab, cd = line.split(",")
        a, b = ab.split("-")
        c, d = cd.split("-")
        a,b,c,d = int(a),int(b),int(c),int(d)

        if(len(set(range(a,b+1)).intersection(set(range(c,d+1)))) > 0 or len(set(range(c,d+1)).intersection(set(range(a,b+1)))) > 0):
            total+=1

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