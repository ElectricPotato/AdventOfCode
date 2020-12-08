'''

'''

def partA(inputText):
    #parse instructions
    instructions = inputText.split("\n")
    program = []
    for instruction in instructions:
        opcode, arg = instruction.split()
        program.append((opcode, int(arg)))

    #run program
    progCount = 0 #program counter
    acc = 0
    visitedLines = []
    while(progCount not in visitedLines):
        visitedLines.append(progCount)
        opcode, arg = program[progCount]
        if(opcode == "nop"):
            progCount += 1
        elif(opcode == "jmp"):
            progCount += arg
        elif(opcode == "acc"):
            acc += arg
            progCount += 1
        print(opcode, arg, acc,progCount)
    return acc

def partB(inputText):
    #parse instructions
    instructions = inputText.split("\n")
    program = []
    for instruction in instructions:
        opcode, arg = instruction.split()
        program.append((opcode, int(arg)))

    progLen = len(program)

    for i in range(progLen):
        #modify program
        newProgram = list(program)
        if(newProgram[i][0] == "nop"):
            newProgram[i] = ("jmp", newProgram[i][1])
        elif(newProgram[i][0] == "jmp"):
            newProgram[i] = ("nop", newProgram[i][1])
        else:
            continue
        #run program
        progCount = 0 #program counter
        acc = 0
        visitedLines = []
        while(progCount not in visitedLines and progCount < progLen):
            visitedLines.append(progCount)
            opcode, arg = newProgram[progCount]
            if(opcode == "nop"):
                progCount += 1
            elif(opcode == "jmp"):
                progCount += arg
            elif(opcode == "acc"):
                acc += arg
                progCount += 1
        if(progCount == progLen):
            return acc



inputFile = open("input.txt", "r")
#inputFile = open("inputExample.txt", "r")
inputText = inputFile.read()

print("partA", partA(inputText))
print("partB", partB(inputText))