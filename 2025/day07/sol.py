
#transpose a list of lists

def parseA(filename):
    with open(filename) as file:
        lines = file.readlines()

    lines = [line.replace("\n","") for line in lines]

    return lines

def partA(lines):
    start_pos = lines[0].index("S")
    beams = set([start_pos])

    total_splits = 0

    for line in lines[1:]:
        active_splitters = [i for i in range(len(line)) if line[i] == "^" and i in beams]

        total_splits += len(active_splitters)

        for p in active_splitters:
            beams.remove(p)

        for p in active_splitters:
            beams.add(p + 1)
            beams.add(p - 1)

    return total_splits

def dict_add(d, key, value):
    if key in d:
        d[key] += value
    else:
        d[key] = value

def partB(lines):
    start_pos = lines[0].index("S")
    beams = {start_pos: 1}

    for line in lines[1:]:
        active_splitters = [i for i in range(len(line)) if line[i] == "^" and i in beams]

        next_beams = dict(beams)

        for p in active_splitters:
            next_beams.pop(p)

        for p in active_splitters:
            dict_add(next_beams, p + 1, beams[p])
            dict_add(next_beams, p - 1, beams[p])

        beams = next_beams

    return sum(beams.values())

def main():
    parsedA_example = parseA("einput.txt")
    result = partA(parsedA_example)
    print(result)
    assert result == 21

    parsedA = parseA("input.txt")
    result = partA(parsedA)
    print(result)
    assert result == 1635

    result = partB(parsedA_example)
    print(result)
    assert result == 40
    
    result = partB(parsedA)
    print(result)
    assert result == 58097428661390

    


if __name__ == '__main__':
    main()