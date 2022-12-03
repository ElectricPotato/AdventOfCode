'''

'''
import string
def partA(inputText):
    total = 0
    lines=inputText.split("\n")
    for line in lines:
        a, b = line[:len(line)//2], line[len(line)//2:]
        common = list(set(a).intersection(set(b)))[0]
        priority = string.ascii_lowercase + string.ascii_uppercase
        p = priority.find(common) + 1
        total+= p

    return total

def partB(inputText):
    total = 0
    lines=inputText.split("\n")
    for lineA, lineB, lineC in zip(lines[0::3], lines[1::3], lines[2::3]):
        common = list(set(lineA).intersection(set(lineB)).intersection(set(lineC)))[0]
        priority = string.ascii_lowercase + string.ascii_uppercase
        p = priority.find(common) + 1
        total+= p

    return total



import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
inputFile = open(os.path.join(__location__, "input.txt"), "r")
inputText = inputFile.read()

print("partA", partA(inputText))
print("partB", partB(inputText))