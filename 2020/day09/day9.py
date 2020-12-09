'''

'''

def partA(inputText):
    numbers = [int(n) for n in inputText.split()]
    preamble = 25
    for i in range(preamble,len(numbers)):
        if(not sum([numbers[i]-j in numbers[i-preamble:i] and numbers[i] != j for j in numbers[i-preamble:i]])):
            return numbers[i]


def partB(inputText):
    numbers = [int(n) for n in inputText.split()]
    goalSum = partA(inputText)
    for starti in range(0,len(numbers)-1):
        for endi in range(starti+2,len(numbers)+1):
            if(sum(numbers[starti:endi]) == goalSum):
                return min(numbers[starti:endi])+max(numbers[starti:endi])



#inputFile = open("inputExample.txt", "r")
inputFile = open("input.txt", "r")
inputText = inputFile.read()

print("partA", partA(inputText))
print("partB", partB(inputText))