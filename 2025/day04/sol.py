import copy

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

def print_grid(grid):
    for line in grid:
        print(''.join(line))

def partB(grid):
    current_grid = copy.deepcopy(grid)
    count = 0

    while True:
        next_grid = copy.deepcopy(current_grid)
        current_count = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if current_grid[y][x] == "@" and neighbours(current_grid, x, y) < 4:
                    next_grid[y][x] = "."
                    current_count += 1
                    count += 1

        current_grid = copy.deepcopy(next_grid)

        if current_count == 0:
            break

    print_grid(current_grid)
    return count

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
    assert result == 43
    
    result = partB(parsedA)
    print(result)
    assert result == 33832678380

    


if __name__ == '__main__':
    main()