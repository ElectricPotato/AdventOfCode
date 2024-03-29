'''

'''


def partA(stack, moves):
    for line in moves.split("\n"):
        for i in ["move ", " from", " to"]:
            line=line.replace(i,"")
        n, fromStack, toStack = map(int, line.split())

        fromStack-=1
        toStack-=1

        stack[toStack] = stack[fromStack][:n][::-1] + stack[toStack]
        stack[fromStack] = stack[fromStack][n:]
        
    return "".join(s[0] for s in stack)

def partB(stack, moves):
    for line in moves.split("\n"):
        for i in ["move ", " from", " to"]:
            line=line.replace(i,"")
        n, fromStack, toStack = map(int, line.split())

        fromStack-=1
        toStack-=1

        stack[toStack] = stack[fromStack][:n] + stack[toStack]
        stack[fromStack] = stack[fromStack][n:]

    return "".join(s[0] for s in stack)




import os

def readFile(fileName):
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, fileName), "r") as inputFile:
        inputText = inputFile.read()
    return inputText

inpStack = [
    "NZ",
    "DCM",
    "P"
]

inpMoves="""move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

print("Example partA", partA(list(inpStack), inpMoves))
print("Example partB", partB(list(inpStack), inpMoves))


inpStack = [
    "CFBLDPZS",
    "BWHPGVN",
    "GJBWF",
    "SCWLFNJG",
    "HSMPTLJW",
    "SFGWCB",
    "WBQMPTH",
    "TWSF",
    "RCN"
]

inpMoves="""move 2 from 5 to 9
move 3 from 1 to 7
move 2 from 3 to 9
move 6 from 9 to 5
move 2 from 3 to 8
move 9 from 7 to 8
move 15 from 8 to 9
move 3 from 1 to 6
move 6 from 4 to 2
move 6 from 5 to 6
move 1 from 4 to 2
move 14 from 6 to 2
move 2 from 1 to 5
move 1 from 7 to 3
move 1 from 4 to 8
move 2 from 5 to 6
move 25 from 2 to 4
move 2 from 6 to 4
move 1 from 8 to 1
move 2 from 9 to 1
move 1 from 6 to 1
move 2 from 1 to 7
move 1 from 7 to 3
move 2 from 1 to 8
move 1 from 2 to 6
move 1 from 3 to 8
move 4 from 5 to 6
move 1 from 5 to 3
move 1 from 9 to 6
move 2 from 3 to 4
move 1 from 2 to 6
move 12 from 9 to 7
move 1 from 9 to 1
move 1 from 5 to 8
move 1 from 3 to 8
move 28 from 4 to 5
move 1 from 4 to 3
move 1 from 2 to 6
move 1 from 3 to 9
move 12 from 7 to 2
move 1 from 9 to 6
move 6 from 6 to 4
move 1 from 7 to 4
move 1 from 1 to 2
move 28 from 5 to 1
move 2 from 2 to 8
move 3 from 8 to 2
move 7 from 4 to 1
move 4 from 8 to 6
move 9 from 2 to 8
move 7 from 6 to 5
move 3 from 5 to 9
move 1 from 9 to 7
move 1 from 7 to 1
move 5 from 8 to 4
move 4 from 1 to 9
move 6 from 9 to 4
move 5 from 1 to 5
move 5 from 2 to 3
move 4 from 8 to 2
move 5 from 1 to 4
move 4 from 5 to 9
move 9 from 4 to 9
move 10 from 9 to 8
move 1 from 9 to 1
move 2 from 2 to 8
move 4 from 3 to 8
move 1 from 2 to 3
move 2 from 9 to 2
move 1 from 2 to 6
move 4 from 4 to 3
move 3 from 5 to 1
move 12 from 1 to 4
move 1 from 5 to 3
move 1 from 5 to 3
move 5 from 8 to 5
move 7 from 8 to 5
move 8 from 3 to 4
move 1 from 5 to 1
move 1 from 6 to 7
move 2 from 1 to 6
move 8 from 5 to 9
move 2 from 5 to 1
move 9 from 1 to 4
move 20 from 4 to 2
move 1 from 5 to 2
move 4 from 4 to 2
move 5 from 9 to 2
move 2 from 8 to 9
move 23 from 2 to 4
move 2 from 2 to 5
move 5 from 1 to 2
move 28 from 4 to 3
move 2 from 8 to 1
move 2 from 5 to 7
move 1 from 6 to 9
move 1 from 4 to 8
move 1 from 8 to 9
move 1 from 4 to 6
move 2 from 7 to 2
move 13 from 3 to 4
move 5 from 9 to 7
move 1 from 9 to 6
move 14 from 2 to 6
move 1 from 4 to 1
move 10 from 3 to 2
move 1 from 6 to 9
move 2 from 3 to 2
move 3 from 1 to 9
move 1 from 3 to 5
move 3 from 9 to 3
move 6 from 7 to 4
move 1 from 9 to 4
move 1 from 9 to 2
move 1 from 5 to 3
move 5 from 3 to 1
move 17 from 4 to 7
move 2 from 2 to 8
move 1 from 3 to 9
move 1 from 8 to 2
move 1 from 9 to 6
move 4 from 6 to 2
move 10 from 6 to 5
move 4 from 1 to 5
move 15 from 2 to 9
move 1 from 8 to 6
move 1 from 2 to 8
move 6 from 9 to 2
move 3 from 4 to 8
move 11 from 7 to 1
move 6 from 9 to 6
move 1 from 6 to 2
move 3 from 9 to 3
move 6 from 2 to 7
move 6 from 7 to 8
move 7 from 1 to 9
move 4 from 1 to 6
move 2 from 1 to 2
move 4 from 6 to 7
move 1 from 2 to 9
move 1 from 2 to 3
move 1 from 2 to 1
move 6 from 8 to 4
move 2 from 6 to 7
move 13 from 5 to 9
move 1 from 5 to 4
move 3 from 4 to 7
move 1 from 1 to 7
move 14 from 9 to 2
move 2 from 9 to 3
move 3 from 8 to 5
move 4 from 3 to 4
move 8 from 4 to 1
move 7 from 1 to 9
move 5 from 6 to 9
move 4 from 9 to 2
move 1 from 1 to 9
move 17 from 2 to 4
move 1 from 6 to 3
move 4 from 7 to 5
move 5 from 7 to 5
move 1 from 6 to 4
move 1 from 8 to 3
move 5 from 7 to 1
move 2 from 7 to 6
move 2 from 3 to 6
move 1 from 2 to 9
move 7 from 9 to 6
move 2 from 3 to 7
move 8 from 6 to 4
move 3 from 9 to 2
move 1 from 6 to 4
move 26 from 4 to 8
move 2 from 7 to 8
move 5 from 5 to 9
move 2 from 6 to 7
move 4 from 9 to 1
move 2 from 7 to 5
move 14 from 8 to 6
move 3 from 2 to 8
move 3 from 6 to 8
move 3 from 6 to 1
move 10 from 8 to 4
move 5 from 9 to 4
move 3 from 8 to 5
move 1 from 8 to 2
move 12 from 4 to 8
move 1 from 9 to 3
move 6 from 6 to 4
move 6 from 8 to 2
move 1 from 3 to 8
move 1 from 8 to 4
move 10 from 1 to 9
move 2 from 1 to 3
move 7 from 4 to 9
move 1 from 2 to 1
move 11 from 8 to 9
move 1 from 3 to 9
move 2 from 2 to 7
move 1 from 3 to 6
move 2 from 7 to 9
move 2 from 4 to 6
move 4 from 6 to 4
move 2 from 2 to 8
move 2 from 8 to 4
move 1 from 1 to 7
move 2 from 2 to 8
move 9 from 5 to 2
move 3 from 5 to 9
move 1 from 8 to 3
move 30 from 9 to 7
move 1 from 6 to 2
move 7 from 4 to 8
move 13 from 7 to 2
move 8 from 7 to 4
move 2 from 4 to 8
move 8 from 8 to 1
move 1 from 8 to 3
move 2 from 8 to 9
move 1 from 3 to 7
move 5 from 7 to 6
move 1 from 3 to 1
move 7 from 4 to 8
move 20 from 2 to 6
move 2 from 2 to 7
move 1 from 9 to 5
move 4 from 7 to 6
move 3 from 7 to 8
move 1 from 7 to 2
move 7 from 8 to 6
move 3 from 6 to 7
move 4 from 9 to 1
move 1 from 2 to 6
move 1 from 9 to 7
move 1 from 2 to 8
move 1 from 7 to 6
move 3 from 6 to 3
move 4 from 8 to 1
move 8 from 6 to 4
move 3 from 7 to 2
move 1 from 3 to 2
move 1 from 4 to 5
move 2 from 3 to 5
move 1 from 4 to 6
move 4 from 1 to 5
move 4 from 2 to 9
move 2 from 1 to 6
move 4 from 9 to 2
move 3 from 2 to 8
move 2 from 8 to 4
move 13 from 6 to 1
move 4 from 5 to 2
move 14 from 6 to 3
move 1 from 2 to 7
move 2 from 2 to 4
move 1 from 8 to 6
move 1 from 6 to 3
move 1 from 7 to 4
move 1 from 2 to 3
move 1 from 2 to 6
move 11 from 4 to 6
move 2 from 5 to 4
move 1 from 5 to 6
move 12 from 3 to 6
move 1 from 3 to 7
move 1 from 5 to 7
move 3 from 3 to 6
move 2 from 7 to 5
move 2 from 5 to 2
move 8 from 6 to 7
move 24 from 1 to 3
move 1 from 4 to 6
move 10 from 3 to 1
move 6 from 1 to 8
move 1 from 6 to 3
move 1 from 4 to 2
move 1 from 3 to 1
move 2 from 2 to 1
move 1 from 7 to 6
move 2 from 7 to 5
move 4 from 3 to 7
move 1 from 2 to 3
move 6 from 1 to 6
move 3 from 7 to 5
move 4 from 7 to 8
move 1 from 1 to 2
move 1 from 2 to 7
move 8 from 3 to 4
move 3 from 4 to 7
move 6 from 8 to 6
move 2 from 3 to 2
move 1 from 3 to 9
move 5 from 5 to 1
move 2 from 8 to 2
move 1 from 9 to 2
move 4 from 1 to 3
move 3 from 2 to 9
move 1 from 1 to 2
move 2 from 9 to 7
move 2 from 2 to 9
move 8 from 7 to 5
move 33 from 6 to 5
move 20 from 5 to 9
move 21 from 5 to 7
move 17 from 7 to 6
move 10 from 6 to 9
move 5 from 4 to 7
move 2 from 3 to 9
move 1 from 2 to 3
move 2 from 7 to 3
move 3 from 9 to 5
move 23 from 9 to 7
move 8 from 9 to 6
move 1 from 9 to 1
move 1 from 5 to 3
move 1 from 8 to 9
move 5 from 6 to 8
move 1 from 9 to 6
move 18 from 7 to 2
move 6 from 7 to 4
move 6 from 4 to 8
move 5 from 7 to 4
move 6 from 6 to 3
move 1 from 4 to 2
move 10 from 2 to 1
move 1 from 2 to 4
move 7 from 1 to 6
move 1 from 7 to 1
move 11 from 6 to 2
move 1 from 6 to 8
move 12 from 3 to 1
move 8 from 1 to 8
move 2 from 5 to 2
move 12 from 8 to 6
move 15 from 2 to 4
move 7 from 4 to 5
move 4 from 5 to 9
move 4 from 9 to 4
move 5 from 4 to 6
move 2 from 5 to 2
move 1 from 2 to 5
move 2 from 5 to 4
move 2 from 1 to 3
move 4 from 1 to 5
move 2 from 8 to 4
move 5 from 2 to 9
move 17 from 6 to 8
move 1 from 3 to 2
move 2 from 5 to 4
move 1 from 3 to 8
move 1 from 1 to 6
move 2 from 5 to 6
move 3 from 9 to 5
move 1 from 5 to 1
move 3 from 1 to 8
move 26 from 8 to 4
move 1 from 5 to 3
move 3 from 2 to 7
move 1 from 5 to 7
move 21 from 4 to 9
move 19 from 4 to 5
move 3 from 4 to 3
move 2 from 7 to 5
move 1 from 8 to 2
move 1 from 6 to 2
move 1 from 8 to 9
move 1 from 6 to 7
move 1 from 2 to 4
move 1 from 4 to 7
move 1 from 2 to 7
move 1 from 7 to 1
move 1 from 1 to 6
move 1 from 3 to 5
move 2 from 6 to 3
move 13 from 5 to 8
move 1 from 4 to 2
move 3 from 5 to 4
move 5 from 5 to 4
move 5 from 8 to 9
move 9 from 9 to 3
move 2 from 7 to 1
move 6 from 4 to 2
move 8 from 9 to 4
move 1 from 2 to 7
move 12 from 9 to 8
move 1 from 4 to 2
move 3 from 7 to 3
move 11 from 8 to 5
move 5 from 8 to 6
move 3 from 6 to 5
move 2 from 4 to 1
move 13 from 5 to 3
move 1 from 1 to 7
move 2 from 1 to 8
move 3 from 4 to 9
move 1 from 1 to 7
move 1 from 2 to 4
move 2 from 7 to 3
move 1 from 5 to 3
move 4 from 4 to 2
move 1 from 4 to 9
move 30 from 3 to 2
move 1 from 9 to 7
move 6 from 8 to 6
move 1 from 7 to 6
move 1 from 5 to 1
move 1 from 3 to 5
move 30 from 2 to 3
move 1 from 1 to 9
move 2 from 9 to 2
move 9 from 6 to 9
move 2 from 2 to 9
move 1 from 5 to 1
move 5 from 9 to 7
move 8 from 2 to 5
move 1 from 1 to 9
move 3 from 9 to 1
move 5 from 3 to 6
move 8 from 5 to 9
move 13 from 3 to 9
move 3 from 1 to 7
move 5 from 7 to 9
move 17 from 9 to 6
move 1 from 7 to 6
move 6 from 3 to 9
move 1 from 2 to 1
move 2 from 7 to 1
move 1 from 2 to 5
move 21 from 9 to 2
move 4 from 3 to 6
move 6 from 6 to 5
move 7 from 5 to 9
move 2 from 3 to 8
move 3 from 1 to 3
move 4 from 6 to 5
move 1 from 8 to 1
move 1 from 8 to 2
move 4 from 5 to 2
move 4 from 9 to 1
move 4 from 3 to 5
move 2 from 1 to 7
move 1 from 7 to 4
move 3 from 9 to 5
move 25 from 2 to 9
move 18 from 9 to 1
move 1 from 4 to 5
move 1 from 3 to 8
move 4 from 5 to 6
move 2 from 9 to 3
move 17 from 1 to 5
move 1 from 2 to 7
move 2 from 3 to 5
move 3 from 1 to 8
move 5 from 9 to 2
move 4 from 8 to 9
move 12 from 5 to 2
move 1 from 1 to 8
move 3 from 9 to 5
move 1 from 8 to 2
move 2 from 7 to 2
move 1 from 9 to 5
move 9 from 5 to 2
move 6 from 6 to 2
move 15 from 6 to 2
move 5 from 5 to 9
move 1 from 5 to 9
move 3 from 9 to 2
move 3 from 9 to 1
move 1 from 1 to 9
move 1 from 9 to 1
move 19 from 2 to 8
move 2 from 1 to 9
move 33 from 2 to 6
move 4 from 6 to 4
move 1 from 2 to 6
move 1 from 9 to 8
move 3 from 4 to 8
move 18 from 8 to 3
move 1 from 4 to 9
move 10 from 3 to 9
move 1 from 1 to 4
move 24 from 6 to 3
move 1 from 4 to 3
move 2 from 8 to 7
move 8 from 9 to 3
move 5 from 6 to 7
move 35 from 3 to 2
move 7 from 7 to 1
move 3 from 1 to 3
move 33 from 2 to 6
move 6 from 3 to 7
move 5 from 7 to 3
move 1 from 1 to 4
move 1 from 7 to 8
move 1 from 4 to 8
move 1 from 3 to 2
move 30 from 6 to 5
move 2 from 1 to 6
move 5 from 8 to 1
move 1 from 9 to 2
move 2 from 6 to 4
move 4 from 1 to 7
move 21 from 5 to 8"""

print("partA", partA(list(inpStack), inpMoves))
print("partB", partB(list(inpStack), inpMoves))