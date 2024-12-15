'''
Solve simultaneous equations:
(1) ax * an + bx * bn = px
(2) ay * an + by * bn = py

Rearage eq 1:
 bn = (px - an * ax) / bx
Substiutute into 2:
 ay * an + by * ((px - an * ax) / bx) = py
Expand:
 ay * an + by * px / bx - by * an * ax / bx = py ok
Move an terms to one side:
 ay * an - by * an * ax / bx = py - by * px / bx
Collect an terms:
 an * (ay - by * ax / bx) = py - by * px / bx
Rearange for an:
 an = (py - by * px / bx) / (ay - by * ax / bx)

Remove division - this stops a floating point error I ran into,
                  by keeping the numerator and denominator as integers
 an = (bx * py - by * px) / (bx * ay - by * ax)

Matrix form:
  ax bx  *  an  =  px
  ay by     bn     py
'''

import parse
from typing import Optional

#solution can be bruteforced, the number of presses of a button is 100 or less
def findCostA(ax, ay, bx, by, px, py) -> Optional[int]:
    aPrice, bPrice = 3, 1

    #A button is more expensive, start with 0 A presses
    for an in range(px // ax):
        if (px - an * ax) % bx != 0:
            continue

        bn = (px - an * ax) // bx
        if ay * an + by * bn == py:
            return aPrice * an + bPrice * bn
        
    return None

def partA(inputText):
    cases=inputText[:-1].split("\n\n")

    total = 0
    for case in cases:
        caseFormat = "Button A: X{:d}, Y{:d}\nButton B: X{:d}, Y{:d}\nPrize: X={:d}, Y={:d}"
        ax, ay, bx, by, px, py = parse.parse(caseFormat, case).fixed

        cost = findCostA(ax, ay, bx, by, px, py)

        if cost is not None:
            total += cost
    
    return total
        
#part B cant be bruteforced, use formula instead
# (should always give the same answer as findCostA)
def findCostB(ax, ay, bx, by, px, py) -> Optional[int]:
    aPrice, bPrice = 3, 1

    if (bx * py - by * px) % (bx * ay - by * ax) != 0:
        return None
    
    an = (bx * py - by * px) // (bx * ay - by * ax)
    bn = (px - an * ax) // bx
    return aPrice * an + bPrice * bn

def partB(inputText):
    cases=inputText[:-1].split("\n\n")

    total = 0
    for case in cases:
        caseFormat = "Button A: X{:d}, Y{:d}\nButton B: X{:d}, Y{:d}\nPrize: X={:d}, Y={:d}"
        ax, ay, bx, by, px, py = parse.parse(caseFormat, case).fixed
        px += 10000000000000
        py += 10000000000000

        cost = findCostB(ax, ay, bx, by, px, py)

        if cost is not None:
            total += cost
    
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
print("Example partA", partA(inputText)) #480
print("Example partB", partB(inputText)) #2nd and 4th case are possible

inputText = readFile("input.txt")
print("partA", partA(inputText)) #40369
print("partB", partB(inputText)) #72587986598368