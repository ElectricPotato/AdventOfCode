'''
Note:
ax * an + bx * bn = px
ay * an + by * bn = py

Matrix form:
  ax bx  *  an  =  px
  ay by     bn     py
'''

import parse
from typing import Optional

#solution can be bruteforced, the number of presses of a button is 100 or less
def findCost(ax, ay, bx, by, px, py) -> Optional[int]:
    aPrice, bPrice = 3, 1

    #A button is more expensive, start with 0 A presses
    found = False
    for an in range(px // ax):
        if (px - an * ax) % bx != 0:
            continue

        bn = (px - an * ax) // bx
        if ay * an + by * bn == py:
            return aPrice * an + bPrice * bn
        
    return None

def partA(inputText):
    cases=inputText.split("\n\n")[:-1]

    total = 0
    for case in cases:
        caseFormat = "Button A: X{:d}, Y{:d}\nButton B: X{:d}, Y{:d}\nPrize: X={:d}, Y={:d}"
        ax, ay, bx, by, px, py = parse.parse(caseFormat, case).fixed

        cost = findCost(ax, ay, bx, by, px, py)

        if cost is not None:
            total += cost
    
    return total
        
        

def partB(inputText):
    lines=inputText.split("\n")
    for line in lines:
        pass

    return 1



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
print("Example partB", partB(inputText))

inputText = readFile("input.txt")
print("partA", partA(inputText))
#print("partB", partB(inputText))
