def parseA(filename):
    with open(filename) as file:
        lines = file.read().splitlines()

    result = []

    for line in lines:
        result.append(list(map(int, line)))

    return result

def partA(parsed):
    total = 0
    for line in parsed:
        first_digit = max(line[:-1])
        line = line[line.index(first_digit) + 1:]

        second_digit = max(line)

        total += first_digit * 10 + second_digit
            
    return total

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