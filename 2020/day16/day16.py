'''

'''

def partA(inputText):
    fieldText, myTicketText, otherTicketText = inputText.split("\n\n")[:3]
    
    validNos = set.union(*[set(range(min,max+1))])

def partB(inputText):
    return None



inputFile = open("input.txt", "r")
inputText = inputFile.read()

print("partA", partA(inputText))
print("partB", partB(inputText))