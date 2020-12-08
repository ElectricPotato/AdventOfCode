'''

'''

def partA(inputText):
    return max(
        [int( line.replace("R","1").replace("L","0").replace("F","0").replace("B","1") ,2)
        for line in inputText.split()]
    )

def partB(inputText):
    numbers = set(
        [int( line.replace("R","1").replace("L","0").replace("F","0").replace("B","1") ,2)
         for line in inputText.split()]
    )
    return (set([n-1 for n in numbers]) & set([n+1 for n in numbers])) - numbers
    #return (set(map(lambda n: n-1, numbers)) & set(map(lambda n: n+1, numbers))) - numbers



inputFile = open("input.txt", "r")
inputText = inputFile.read()

print("partA", partA(inputText))
print("partB", partB(inputText))