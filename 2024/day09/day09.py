'''

'''

BLOCK_EMPTY = -1

def parse(inputText):
    nums=list(map(int, inputText.split("\n")[0]))
    if len(nums) % 2 == 1:
        nums += [0] #add a number of spaces to make everything pairs of (file size + space size)
    
    maxFileID = len(nums) // 2 - 1
    diskChunks = []
    for fileID, (fileSize, spaceSize) in enumerate(zip(nums[::2], nums[1::2])):
        if fileSize > 0:
            diskChunks += [(fileID, fileSize)]
    
        if spaceSize > 0:
            diskChunks += [(BLOCK_EMPTY, spaceSize)]

    return diskChunks, maxFileID

def printDisk(disk):
    print(''.join(str(x) if x >= 0 else '.' for x in disk))

def checksumDisk(disk):
    #checksum
    checksum = 0
    for blockIdx, fileID in enumerate(disk):
        if fileID == -1:
            break
        checksum += blockIdx * fileID

    return checksum

def partA(inputText, debug = False):
    diskChunks, _ = parse(inputText)

    disk = []
    for fileID,fileSize in diskChunks:
        disk += [fileID] * fileSize

    if debug:
        printDisk(disk)
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

        if debug: printDisk(disk)

    return checksumDisk(disk)


def printDiskChunks(diskChunks):
    print(''.join((str(fileID) if fileID >= 0 else '.') * fileSize for fileID, fileSize in diskChunks))

def checksumDiskChunks(diskChunks):
    checksum = 0
    blockIdx = 0
    for fileID, fileSize in diskChunks:
        if fileID == BLOCK_EMPTY:
            blockIdx += fileSize
            continue

        for _ in range(fileSize): #Note: could be optimized with triangular number formula
            checksum += fileID * blockIdx
            blockIdx += 1

    return checksum

def partB(inputText, debug = False):
    diskChunks, maxFileID = parse(inputText)

    firstSpace = 0

    if debug:
        print("initial")
        printDiskChunks(diskChunks)

    filePointer = len(diskChunks) - 1
    for relocateFileID in range(maxFileID, -1, -1):
        print(f"{relocateFileID} / {maxFileID}")

        #get the next file to relocate
        while diskChunks[filePointer][0] != relocateFileID:
            filePointer -= 1
        _, fileSize = diskChunks[filePointer]

        if debug:printDiskChunks(diskChunks)
        #for each file, find a suitable space

        #get first space
        spacePointer = firstSpace
        while diskChunks[spacePointer][0] != BLOCK_EMPTY:
            spacePointer += 1
            if spacePointer > len(diskChunks) - 1:
                break
        if spacePointer > len(diskChunks) - 1:
            break

        firstSpace = spacePointer #optimisation: position of first space only moves forward

        while True:
            #check each space for relocation
            if spacePointer >= filePointer: break
            
            #print(f"attempting to relocate {relocateFileID}")
            _, spaceSize = diskChunks[spacePointer]
            if spaceSize >= fileSize:
                #print("relocating")
                #sufficient space - relocate file
                if spaceSize != fileSize: #space left over
                    diskChunks[spacePointer] = (BLOCK_EMPTY, spaceSize - fileSize)
                    diskChunks.insert(spacePointer, (relocateFileID, fileSize))
                    if filePointer >= spacePointer:
                        filePointer += 1
                    spacePointer += 1
                else: #no space left over
                    diskChunks[spacePointer] = (relocateFileID, fileSize)
                diskChunks[filePointer] = (BLOCK_EMPTY, fileSize)
                #printDiskChunks(diskChunks)
                break

            #get next space
            spacePointer += 1
            if spacePointer > len(diskChunks) - 1:
                break
            while diskChunks[spacePointer][0] != BLOCK_EMPTY:
                spacePointer += 1
                if spacePointer > len(diskChunks) - 1:
                    break

            if spacePointer > len(diskChunks) - 1:
                break

            if spacePointer >= filePointer: break

    if debug:
        print("finished")
        printDiskChunks(diskChunks)

    return checksumDiskChunks(diskChunks)



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
print("Example partB", partB(inputText)) #2858

inputText = readFile("input.txt")
#print("partA", partA(inputText)) #6519155389266
print("partB", partB(inputText)) #6547228115826
