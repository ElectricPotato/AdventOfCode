def parseA(filename):
    with open(filename) as file:
        lines = file.readlines()

    lines = [line.replace("\n","") for line in lines]

    shapes = []

    while lines[0][-1] == ":":
        lines.pop(0) #remove the shape numbering

        shape = []
        while "#" in lines[0] or "." in lines[0]:
            shape += [[c == "#" for c in lines[0]]]
            lines.pop(0)

        lines.pop(0) #remove the blank line

        shapes.append(shape)

    cases = []
    for line in lines:
        dimentions, shape_numbers = line.split(": ")
        dimentions = list(map(int, dimentions.split("x")))
        shape_numbers = list(map(int, shape_numbers.split(" ")))

        cases.append((dimentions, shape_numbers))

    return (shapes, cases)

def partA(parsed):
    print(parsed)

    return None

def partB(parsed):

    return None

def main():
    parsedA_example = parseA("einput.txt")
    result = partA(parsedA_example)
    print(result)
    assert result == 2

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