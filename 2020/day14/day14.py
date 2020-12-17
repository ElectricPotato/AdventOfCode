'''

'''

def partA(inputText):
    lines = inputText.splitlines()
    andMask = 0
    orMask = 0
    mem = {}
    for line in lines:
        destination, literal = line.split(" = ")
        if(destination=="mask"):
            andMask = int(literal.replace("X","1"),2)
            orMask  = int(literal.replace("X","0"),2)
            #print(orMask,andMask)
        elif(destination[:4] == "mem["):
            address = int(destination[4:-1])
            translatedN = (int(literal) & andMask) | orMask
            mem[address] = translatedN
            #print(mem)

    return sum(mem.values())

def partB(inputText):
    lines = inputText.splitlines()
    orMask = 0
    mem = {}
    for line in lines:
        destination, literal = line.split(" = ")
        if(destination=="mask"):
            xIndices = [pos for pos,char in enumerate(literal) if char=="X"]
            noAddresses = 2**len(xIndices)
            orMask = int(literal.replace("X","0"),2)
        elif(destination[:4] == "mem["):
            address = f'{(int(destination[4:-1]) | orMask):0>36b}'
            translatedN = int(literal)
            #print( f'{orMask:0>36b}')
            for n in range(noAddresses):
                nBin = f'{n:0>36b}'
                newAddress = list(address)
                for i in range(len(xIndices)):
                    newAddress[xIndices[i]] = nBin[-i-1]
                newAddress=int(''.join(newAddress),2)
                mem[newAddress] = translatedN
                #print(newAddress)
            #print(mem)

    return sum(mem.values())



inputFile = open("input.txt", "r")
#inputFile = open("inputEx.txt", "r")
#inputFile = open("inputEx2.txt", "r")
inputText = inputFile.read()

print("partA", partA(inputText))
print("partB", partB(inputText))