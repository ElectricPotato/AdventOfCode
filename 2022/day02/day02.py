'''

'''

def partA(inputText):
    lines=inputText.split("\n")
    s = 0
    for line in lines:
        line = line.replace("A", "R").replace("B", "P").replace("C", "S") \
                   .replace("X", "R").replace("Y", "P").replace("Z", "S")
        a, b = line.split()

        s += {"R":1, "P":2, "S":3}[b]
        if(a == b):
            s += 3 #draw
        elif( (a, b) in [("R", "P"), ("P", "S"), ("S", "R")]):
            s += 6 #win
        else:
            s += 0 #loose
    return s

def partB(inputText):
    lines=inputText.split("\n")
    lines=inputText.split("\n")
    s = 0
    for line in lines:
        line = line.replace("A", "R").replace("B", "P").replace("C", "S")
        a, b = line.split()

        s += {"X":0, "Y":3, "Z":6}[b]
        if(b == "Y"):
            play = a
        elif(b == "X"): #loose
            play = {"R": "S", "P": "R", "S": "P"}[a]
        else: #win
            play = {"R": "P", "P": "S", "S": "R"}[a]

        s += {"R":1, "P":2, "S":3}[play]
    return s



inputFile = open("input.txt", "r")
inputText = inputFile.read()

print("partA", partA(inputText))
print("partB", partB(inputText))