import copy

def parseA(filename):
    with open(filename) as file:
        fresh_ranges, ingredients = file.read().split("\n\n")

    fresh_ranges = [list(map(int, line.split("-"))) for line in fresh_ranges.split()]
    ingredients = [int(line) for line in ingredients.split()]

    return (fresh_ranges, ingredients)

def partA(parsed):
    fresh_ranges, ingredients = parsed

    count = 0
    for i in ingredients:
        fresh = False
        for a, b in fresh_ranges:
            if a <= i <= b:
                fresh = True
                count += 1
                break

    return count

# boolean union of two ranges a and b
def range_overlap(a, b):
    assert a[0] <= a[1] and b[0] <= b[1]

    if range_overlap_check(a, b):
        return [min(a[0], b[0]), max(a[1], b[1])]
    else:
        return None
    
# true if ranges (a1, b1) and (a2, b2) overlap or are next to each other
def range_overlap_check(a, b):
    return a[0] <= b[0] <= a[1] or a[0] <= b[1] <= a[1] \
        or b[0] <= a[0] <= b[1] or b[0] <= a[1] <= b[1] \
        or abs(a[0] - b[1]) == 1 or abs(a[1] - b[0]) == 1
    
def range_size(a):
    return a[1] - a[0] + 1

def find_overlap(fresh_ranges):
    for idx1 in range(len(fresh_ranges)):
        for idx2 in range(idx1 + 1, len(fresh_ranges)):
            if range_overlap_check(fresh_ranges[idx1], fresh_ranges[idx2]):
                return (idx1, idx2)
    return None

def partB(ranges_in):
    fresh_ranges = copy.deepcopy(ranges_in)

    #union all ranges
    # this could be made more efficient: https://stackoverflow.com/questions/15273693/union-of-multiple-ranges
    while True:
        overlap = find_overlap(fresh_ranges)
        if overlap == None:
            break

        idx1, idx2 = overlap
        fresh_ranges[idx1] = range_overlap(fresh_ranges[idx1], fresh_ranges[idx2])
        fresh_ranges.pop(idx2)

    return sum(range_size(i) for i in fresh_ranges)

def main():
    parsedA_example = parseA("einput.txt")
    result = partA(parsedA_example)
    print(result)
    assert result == 3

    parsedA = parseA("input.txt")
    result = partA(parsedA)
    print(result)

    result = partB(parsedA_example[0])
    print(result)
    assert result == 14
    
    result = partB(parsedA[0])
    print(result)
    assert result == 347338785050515

if __name__ == '__main__':
    main()