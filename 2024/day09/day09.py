'''

'''

BLOCK_EMPTY = -1

def partA(inputText):
    parsed=list(map(int, inputText.split("\n")[0]))
    if len(parsed) % 2 == 1:
        parsed += [0] #add a number of spaces to make everything pairs of (file size + space size)
    
    disk = []
    for fileID, (fileSize, spaceSize) in enumerate(zip(parsed[::2], parsed[1::2])):
        disk += [fileID] * fileSize
        disk += [BLOCK_EMPTY] * spaceSize

    #print(''.join(str(x) if x >= 0 else '.' for x in disk))
    print(f"length of disk: {len(disk)}")
    

    startPointer = 0
    endPointer = len(disk) - 1

    while startPointer < endPointer:
        if disk[startPointer] != BLOCK_EMPTY:
            startPointer += 1
            continue

        if disk[endPointer] == BLOCK_EMPTY:
            endPointer -= 1
            continue

        disk[startPointer] = disk[endPointer]
        disk[endPointer] = BLOCK_EMPTY
        startPointer += 1
        endPointer -= 1

        #print(''.join(str(x) if x >= 0 else '.' for x in disk))

    #checksum
    checkSum = 0
    for blockIdx, fileID in enumerate(disk):
        if fileID == -1:
            break
        checkSum += blockIdx * fileID

    return checkSum

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
print("Example partA", partA(inputText)) #1928
#print("Example partB", partB(inputText))

inputText = readFile("input.txt")
print("partA", partA(inputText)) #6519155389266
#print("partB", partB(inputText))
