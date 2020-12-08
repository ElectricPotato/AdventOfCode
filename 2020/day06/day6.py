'''

'''

def partA(inputText):
    return sum(
        [len(set(group.replace("\n","")))
         for group in inputText.split("\n\n")]
    )

def partB(inputText):
    #print([group.split("\n") for group in inputText.split("\n\n")][-5:])
    #return None
    return sum(
        [len(set.intersection(*
            [set(line)
                for line in group.split("\n")]))
                    for group in inputText.split("\n\n")
        ]
    )



inputFile = open("input.txt", "r")
inputText = inputFile.read()

print("partA", partA(inputText))
print("partB", partB(inputText))