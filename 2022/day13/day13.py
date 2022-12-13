'''

'''


def partA(inputText):

    def compare(a, b, debug=True):
        #if(debug and not ((type(a) == int and type(b) == int))): print(a,b, compare(a, b, False))

        if(type(a) == int and type(b) == int):
            if(a != b):
                return a < b
        elif(type(a) == list and type(b) == list):
            for x, y in zip(a,b):
                if(compare(x,y) is not None):
                    return compare(x,y)
            if(len(a) > len(b)):
                return False
            if(len(a) < len(b)):
                return True
        elif(type(a) == int and type(b) == list):
            return compare([a], b)
        elif(type(a) == list and type(b) == int):
            return compare(a, [b])

        return None

    total = 0
    pairs = inputText.split("\n\n")
    for i, pair in enumerate(pairs, start = 1):
        a, b = pair.split("\n")
        a = eval(a)
        b = eval(b)
        #print(a,b,compare(a,b))
        if(compare(a, b, True)):
            total += i

    return total

def partB(inputText):
    def compare(a, b, debug=True):
        if(type(a) == int and type(b) == int):
            if(a != b):
                return a < b
        elif(type(a) == list and type(b) == list):
            for x, y in zip(a,b):
                if(compare(x,y) is not None):
                    return compare(x,y)
            if(len(a) > len(b)):
                return False
            if(len(a) < len(b)):
                return True
        elif(type(a) == int and type(b) == list):
            return compare([a], b)
        elif(type(a) == list and type(b) == int):
            return compare(a, [b])

        return None


    packets = [eval(packet) for packet in inputText.split("\n") if packet != ""]

    packets += [ [[2]], [[6]] ]

    #bubble sort
    isSorted = False
    while(not isSorted):
        isSorted = True
        for i in range(len(packets)-1):
            if(compare(packets[i], packets[i+1]) == False):
                packets[i], packets[i+1] = packets[i+1], packets[i] #swap
                isSorted = False

    #for p in packets:print(p)

    return (packets.index([[2]])+1) * (packets.index([[6]])+1)



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
