def parseA(filename):
    with open(filename) as file:
        lines = file.readlines()

    result = []

    for line in lines:
        sign = +1 if line[0] == "R" else -1
        result.append(sign * int(line[1:]))

    return result

def partA(parsed):
    rotation = 50
    total = 0
    for i in parsed:
        rotation = (rotation + i) % 100
        if rotation == 0:
            total += 1

    return total

def partB(parsed):
    rotation = 50
    total = 0
    for current_turn in parsed:
        sign = +1 if current_turn > 0 else -1
        for _ in range(abs(current_turn)):
            rotation = (rotation + sign) % 100
            if rotation == 0:
                total += 1

    return total

def main():
    parsedA_example = parseA("einput.txt")
    result = partA(parsedA_example)
    print(result)
    assert result == 3

    parsedA = parseA("input.txt")
    result = partA(parsedA)
    print(result)

    result = partB(parsedA_example)
    print(result)
    assert result == 6
    
    result = partB(parsedA)
    print(result)

    


if __name__ == '__main__':
    main()