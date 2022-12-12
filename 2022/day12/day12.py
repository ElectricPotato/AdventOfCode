'''

'''

#I dont know dijkstra lol
from dijkstar import Graph, find_path
from dijkstar.algorithm import single_source_shortest_paths


def partA(inputText):
    grid=inputText.split("\n")
    graph = Graph()
    xR = range(len(grid[0]))
    yR = range(len(grid))
    def coordToN(x, y):
        return x + y * len(grid[0])

    def asciiToHeight(l):
        if(l == "S"): return asciiToHeight("a")
        if(l == "E"): return asciiToHeight("z")
        return ord(l)-ord("a")

    startN = None
    endN = None
    for y in yR:
        for x in xR:
            if(grid[y][x] == "S"):startN = coordToN(x, y)
            if(grid[y][x] == "E"):endN = coordToN(x, y)
            for xDir, yDir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if(x+xDir in xR and y+yDir in yR):
                    if(asciiToHeight(grid[y+yDir][x+xDir]) <= asciiToHeight(grid[y][x])+1):
                        graph.add_edge(coordToN(x, y), coordToN(x+xDir, y+yDir), 1)


    return find_path(graph, startN, endN).total_cost

def partB(inputText):
    grid=inputText.split("\n")
    reverseGraph = Graph()
    xR = range(len(grid[0]))
    yR = range(len(grid))
    def coordToN(x, y):
        return x + y * len(grid[0])

    def nToCoord(n):
        return (n%len(grid[0]), n//len(grid[0]))

    def asciiToHeight(l):
        if(l == "S"): return asciiToHeight("a")
        if(l == "E"): return asciiToHeight("z")
        return ord(l)-ord("a")

    startN = None
    endN = None
    for y in yR:
        for x in xR:
            if(grid[y][x] == "S"):startN = coordToN(x, y)
            if(grid[y][x] == "E"):endN = coordToN(x, y)
            for xDir, yDir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if(x+xDir in xR and y+yDir in yR):
                    if(asciiToHeight(grid[y+yDir][x+xDir]) <= asciiToHeight(grid[y][x])+1):
                        reverseGraph.add_edge(coordToN(x+xDir, y+yDir), coordToN(x, y), 1)

    #visitedSquares just so happens to contains the squares reachable from a the end square in order of distance from it
    visitedSquares = single_source_shortest_paths(reverseGraph, endN).keys()
    for sq in visitedSquares:
        x,y = nToCoord(sq)
        if grid[y][x] == "a":
            startN = sq
            break

    forwardGraph = Graph()
    for y in yR:
        for x in xR:
            for xDir, yDir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if(x+xDir in xR and y+yDir in yR):
                    if(asciiToHeight(grid[y+yDir][x+xDir]) <= asciiToHeight(grid[y][x])+1):
                        forwardGraph.add_edge(coordToN(x, y), coordToN(x+xDir, y+yDir), 1)


    return find_path(forwardGraph, startN, endN).total_cost



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
