'''

'''

def parse(inputText):
    lines=inputText.split("\n")[:-1]
    width = len(lines[0])
    height = len(lines)

    antennas = dict()

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == '.':
                continue

            if c in antennas:
                antennas[c] += [(x, y)]
            else:
                antennas[c] = [(x, y)]

    return antennas, width, height


def partA(inputText):
    antennas, width, height = parse(inputText)
    antinodes = set()

    for positions in antennas.values():
        for i in range(len(positions)):
            for j in range(i):
                x1, y1 = positions[i]
                x2, y2 = positions[j]
                dx, dy = x2 - x1, y2 - y1
                xNew1, yNew1 = x1 - dx, y1 - dy
                xNew2, yNew2 = x2 + dx, y2 + dy

                if(0 <= xNew1 < width and 0 <= yNew1 < height):
                    antinodes.add((xNew1, yNew1))

                if(0 <= xNew2 < width and 0 <= yNew2 < height):
                    antinodes.add((xNew2, yNew2))

    return len(antinodes)


from math import gcd

def partB(inputText):
    antennas, width, height = parse(inputText)
    antinodes = set()

    for positions in antennas.values():
        for i in range(len(positions)):
            for j in range(i):
                x1, y1 = positions[i]
                x2, y2 = positions[j]
                dx, dy = x2 - x1, y2 - y1

                #reduce fraction
                g = gcd(dx, dy)
                dx, dy = dx // g, dy // g

                for n in range(-1000, 1000): #TODO: better limits
                    xNew, yNew = x1 + n * dx, y1 + n * dy

                    if(0 <= xNew < width and 0 <= yNew < height):
                        antinodes.add((xNew, yNew))

    #show
    lines=list(map(list, inputText.split("\n")[:-1]))
    for x, y in antinodes:
        lines[y][x] = "#"
    for line in lines:
        print(''.join(line))

    return len(antinodes)



import os

def readFile(fileName):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )
    with open(os.path.join(__location__, fileName), "r") as inputFile:
        inputText = inputFile.read()
    return inputText

inputText = readFile("einput.txt")
#print("Example partA", partA(inputText)) #14
print("Example partB", partB(inputText)) #34

inputText = readFile("input.txt")
print("partA", partA(inputText)) #320
print("partB", partB(inputText)) #1157
