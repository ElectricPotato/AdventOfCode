def parseA(filename):
    with open(filename) as file:
        lines = file.readlines()

    lines = [line.replace("\n","") for line in lines]

    return [list(map(int, line.split(","))) for line in lines]


#get the square of the distance between two points in 3D space
def sq_dist(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2

def product(ns):
    p = 1
    for n in ns:
        p *= n

    return p

def find_circuit(circuits, element):
    for i in range(len(circuits)):
        if element in circuits[i]:
            return i

def partA(boxes, n_connections):

    pairs = []
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            pairs.append((i, j, sq_dist(boxes[i], boxes[j])))

    pairs.sort(key = lambda x: x[2])

    circuits = [[i] for i in range(len(boxes))]

    for pair_idx in range(n_connections):
        i, j, _ = pairs[pair_idx]

        i_circuit_idx = find_circuit(circuits, i)
        j_circuit_idx = find_circuit(circuits, j)

        if i_circuit_idx != j_circuit_idx:
            circuits[i_circuit_idx] += circuits[j_circuit_idx]
            circuits.pop(j_circuit_idx)

    circuits_len = list(map(len, circuits))
    circuits_len.sort(reverse = True)


    return product(circuits_len[:3])

def partB(boxes):

    pairs = []
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            pairs.append((i, j, sq_dist(boxes[i], boxes[j])))

    pairs.sort(key = lambda x: x[2])

    circuits = [[i] for i in range(len(boxes))]

    pair_idx = 0
    while(len(circuits) > 1):
        i, j, _ = pairs[pair_idx]

        i_circuit_idx = find_circuit(circuits, i)
        j_circuit_idx = find_circuit(circuits, j)
        if i_circuit_idx != j_circuit_idx:
            circuits[i_circuit_idx] += circuits[j_circuit_idx]
            circuits.pop(j_circuit_idx)

        pair_idx += 1

    return boxes[i][0] * boxes[j][0]

def main():
    parsedA_example = parseA("einput.txt")
    result = partA(parsedA_example, 10)
    print(result)
    assert result == 40

    parsedA = parseA("input.txt")
    result = partA(parsedA, 1000)
    print(result)
    assert result == 66640

    result = partB(parsedA_example)
    print(result)
    assert result == 25272
    
    result = partB(parsedA)
    print(result)
    assert result == 78894156



if __name__ == '__main__':
    main()