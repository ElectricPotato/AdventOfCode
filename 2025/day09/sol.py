def parseA(filename):
    with open(filename) as file:
        lines = file.readlines()

    lines = [list(map(int, line.replace("\n","").split(","))) for line in lines]

    return lines

def area(a, b):
    return abs(a[0] - b[0] + 1) * abs(a[1] - b[1] + 1)

def partA(squares):
    rectangles = []
    for i in range(len(squares)):
        for j in range(i + 1, len(squares)):
            rectangles.append((i, j, area(squares[i], squares[j])))

    rectangles.sort(key=lambda x: x[2], reverse=True)

    return rectangles[0][2]

def partB(points):

    polygon_lines = list(zip(points, points[1:]))

    return None

def main():
    parsedA_example = parseA("einput.txt")
    result = partA(parsedA_example)
    print(result)
    assert result == 50

    parsedA = parseA("input.txt")
    result = partA(parsedA)
    print(result)
    assert result == 4774877510

    result = partB(parsedA_example)
    print(result)
    assert result == 24
    
    result = partB(parsedA)
    print(result)
    #assert result == 

    


if __name__ == '__main__':
    main()