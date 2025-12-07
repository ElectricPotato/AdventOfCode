
#transpose a list of lists

def parseA(filename):
    with open(filename) as file:
        lines = file.readlines()

    lines = [line.replace("\n","") for line in lines]

    return lines

def partA(parsed):

    return None

def partB(parsed):

    return None

def main():
    parsedA_example = parseA("einput.txt")
    result = partA(parsedA_example)
    print(result)
    assert result == None

    parsedA = parseA("input.txt")
    result = partA(parsedA)
    print(result)
    #assert result == 

    result = partB(parsedA_example)
    print(result)
    assert result == None
    
    result = partB(parsedA)
    print(result)
    #assert result == 

    


if __name__ == '__main__':
    main()