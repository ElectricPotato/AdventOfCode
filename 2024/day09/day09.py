'''

'''

BLOCK_EMPTY = -1

def partA(inputText):
    nums=list(map(int, inputText.split("\n")[0]))
    if len(nums) % 2 == 1:
        nums += [0] #add a number of spaces to make everything pairs of (file size + space size)
    
    disk = []
    for fileID, (fileSize, spaceSize) in enumerate(zip(nums[::2], nums[1::2])):
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
    checksum = 0
    for blockIdx, fileID in enumerate(disk):
        if fileID == -1:
            break
        checksum += blockIdx * fileID

    return checksum

#TODO: add print function
#TODO: tidy code, put stuff into functions

def printChunks(diskChunks):
    print(''.join((str(fileID) if fileID >= 0 else '.') * fileSize for fileID, fileSize in diskChunks))

def partB(inputText):
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

    print("initial")
    #printChunks(diskChunks)

    filePointer = len(diskChunks) - 1
    #get first file
    while diskChunks[filePointer][0] == BLOCK_EMPTY:
        filePointer -= 1
        if filePointer < 0:
            break

    for relocateFileID in range(maxFileID, -1, -1):
        print(f"{relocateFileID} / {maxFileID}")
        for i, (cId, cSize) in enumerate(diskChunks):
            if cId == relocateFileID:
                fileSize = cSize
                filePointer = i
                break
        #printChunks(diskChunks)
        #for each file, find a suitable space

        #get first space
        spacePointer = 0
        while diskChunks[spacePointer][0] != BLOCK_EMPTY:
            spacePointer += 1
            if spacePointer > len(diskChunks) - 1:
                break
        if spacePointer > len(diskChunks) - 1:
            break

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
                #printChunks(diskChunks)
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

    print("finished")
    #printChunks(diskChunks)
    #checksum
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



import os

def readFile(fileName):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )
    with open(os.path.join(__location__, fileName), "r") as inputFile:
        inputText = inputFile.read()
    return inputText

inputText = readFile("einput.txt")
#print("Example partA", partA(inputText)) #1928
print("Example partB", partB(inputText)) #2858

inputText = readFile("input.txt")
#print("partA", partA(inputText)) #6519155389266
print("partB", partB(inputText)) #6547228115826
