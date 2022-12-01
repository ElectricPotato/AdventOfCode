'''

'''

def partA(inputText):
    a=inputText.split("\n\n")
    return max(sum(map(int,elf.split())) for elf in a) 

def partB(inputText):
    a=inputText.split("\n\n")
    return sum(sorted(sum(map(int,elf.split())) for elf in a)[-3:])



inputFile = open("input.txt", "r")
inputText = inputFile.read()

print("partA", partA(inputText))
print("partB", partB(inputText))