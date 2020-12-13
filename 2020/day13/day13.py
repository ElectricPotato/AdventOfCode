'''

'''

def partA(inputText):
    timestamp, busList = inputText.split()
    timestamp = int(timestamp)
    busList = [int(bus) for bus in busList.split(",") if bus != "x"]
    timeUntil = [-timestamp%bus for bus in busList]
    earliestBus = min(zip(timeUntil,busList), key = lambda a: a[0])
    return earliestBus[0] * earliestBus[1]

#TODO
def partB(inputText):
    _, busList = inputText.split()
    busList = enumerate(busList.split(","))
    busList = [(busPos%int(busN), int(busN)) for busPos, busN in busList if busN != "x"]

    #unzip
    busN = [i[1] for i in busList]
    busPos = [i[0] for i in busList]

    #confirm busN are coprime
    from sympy.ntheory import factorint
    factorized = [factorint(i) for i in busN]
    print(busN, busPos, factorized)
    return None



inputFile = open("input.txt", "r")
#inputFile = open("inputEx.txt", "r")
inputText = inputFile.read()

#print("partA", partA(inputText))
print("partB", partB(inputText))