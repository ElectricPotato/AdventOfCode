def parseA(filename):
    with open(filename) as file:
        lines = file.read().splitlines()

    result = []

    for line in lines:
        result.append(list(map(int, line)))

    return result

def partA_one_line(line):
    first_digit = max(line[:-1])
    line = line[line.index(first_digit) + 1:]

    second_digit = max(line)

    return first_digit * 10 + second_digit

def partA(parsed):
    return sum(partA_one_line(line) for line in parsed)

def partB(parsed):

    return None

def main():
    parsedA_example = parseA("einput.txt")
    result = partA(parsedA_example)
    print(result)
    assert result == 357

    parsedA = parseA("input.txt")
    result = partA(parsedA)
    print(result)
    assert result == 17087

    result = partB(parsedA_example)
    print(result)
    assert result == None
    
    result = partB(parsedA)
    print(result)
    #assert result ==

    


if __name__ == '__main__':
    main()