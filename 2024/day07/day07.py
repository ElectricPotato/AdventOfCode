'''

'''

def parse(inputText):
    lines=inputText.split("\n")[:-1]

    parsed = []
    for line in lines:
        resultText, argsText = line.split(": ")
        result = int(resultText)
        args = list(map(int, argsText.split()))

        parsed += [(result, args)]

    return parsed

def partA(inputText):
    cases = parse(inputText)

    total = 0
    for result, args in cases:

        found = False
        for n in range(2**(len(args) - 1)):
            accumulator = args[0]
            for i, arg in enumerate(args[1:]):
                if n & (1<<i):
                    accumulator += arg
                else:
                    accumulator *= arg

            if accumulator == result:
                found = True
                break

        if found:
            total += accumulator

    return total

def partB(inputText):
    cases = parse(inputText)

    total = 0
    for caseI, (result, args) in enumerate(cases):
        print(caseI)

        found = False
        for n in range(3**(len(args) - 1)):
            accumulator = args[0]
            for i, arg in enumerate(args[1:]):
                op = (n // (3**i)) % 3
                if op == 0:
                    accumulator += arg
                elif op == 1:
                    accumulator *= arg
                elif op == 2:
                    accumulator = int(str(accumulator) + str(arg))
                    
            if accumulator == result:
                found = True
                break

        if found:
            total += accumulator

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
print("Example partB", partB(inputText))

inputText = readFile("input.txt")
#print("partA", partA(inputText))
print("partB", partB(inputText))
