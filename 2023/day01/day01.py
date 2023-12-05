'''

'''


def partA(inputText):
    lines=inputText.split("\n")

    total = 0
    for line in lines:
        first_digit = None
        last_digit = None
        for c in line:
            if(c.isdigit()):
                if(first_digit == None): first_digit = int(c)
                last_digit = int(c)
        total += first_digit * 10 + last_digit
        

    return total

import re

def partB(inputText):
    lines=inputText.split("\n")

    total = 0

    numbers = "one|two|three|four|five|six|seven|eight|nine".split("|")
    numbers_reversed = [n[::-1] for n in numbers]

    pattern = r"(one|two|three|four|five|six|seven|eight|nine|\d)"
    pattern_rev = "(" + "|".join(numbers_reversed) + r"|\d)"

    def digit_to_int(s):
        if(s.isdigit()):
            return int(s)
        else:
            return numbers.index(s) + 1

    for line in lines:
        first = re.search(pattern, line)[0]
        last = re.search(pattern_rev, line[::-1])[0][::-1]

        first_digit = digit_to_int(first)
        last_digit = digit_to_int(last)
        
        total += first_digit * 10 + last_digit

    return total



import os

def readFile(fileName):
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, fileName), "r") as inputFile:
        inputText = inputFile.read()
    return inputText

inputText = readFile("einput.txt")
print("Example partA", partA(inputText))
inputText = readFile("einput2.txt")
print("Example partB", partB(inputText))

inputText = readFile("input.txt")
print("partA", partA(inputText))
print("partB", partB(inputText))