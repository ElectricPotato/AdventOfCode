def parseA(filename):
    with open(filename) as file:
        lines = list(map(list,file.read().splitlines()))

    return lines

def neighbours(grid, x, y):
    diff = [(dx, dy) for dx in range(-1, 1 + 1) for dy in range(-1, 1 + 1) if not ((dx, dy) == (0,0))]

    count = 0
    for (dx, dy) in diff:
        if not (0 <= x + dx < len(grid[0]) and 0 <= y + dy < len(grid)):
            continue

        if grid[y + dy][x + dx] == "@":
            count += 1

    return count

def partA(grid):

    count = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            #print(neighbours(grid, x, y), end="")
            if grid[y][x] == "@" and neighbours(grid, x, y) < 4:
                count += 1
        #print()
    return count

def partB(grid):
    return None

def main():
    parsedA_example = parseA("einput.txt")
    result = partA(parsedA_example)
    print(result)
    assert result == 13

    parsedA = parseA("input.txt")
    result = partA(parsedA)
    print(result)
    assert result == 1344

    result = partB(parsedA_example)
    print(result)
    assert result == None
    
    result = partB(parsedA)
    print(result)
    #assert result == 

    


if __name__ == '__main__':
    main()