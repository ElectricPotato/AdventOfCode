from sol import *

#this version avoids using a linear search by having another list which shows which circuit a box belongs to
#it doesn't make it much faster through my testing
#1.692s -> 1.537s
def partA_faster(boxes, n_connections):

    pairs = []
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            pairs.append((i, j, sq_dist(boxes[i], boxes[j])))

    pairs.sort(key = lambda x: x[2])

    circuits = [[i] for i in range(len(boxes))]
    box_circuit = [i for i in range(len(boxes))] # list of which circuit each box belongs to

    for pair_idx in range(n_connections):
        i, j, _ = pairs[pair_idx]

        i_circuit_idx = box_circuit[i]
        j_circuit_idx = box_circuit[j]
        
        if i_circuit_idx != j_circuit_idx:
            circuits[i_circuit_idx] += circuits[j_circuit_idx]
            for b in circuits[j_circuit_idx]:
                box_circuit[b] = i_circuit_idx
            circuits[j_circuit_idx] = []

    circuits_len = list(map(len, circuits))
    circuits_len.sort(reverse = True)


    return product(circuits_len[:3])

def partB_faster(boxes):
    pairs = []
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            pairs.append((i, j, sq_dist(boxes[i], boxes[j])))

    pairs.sort(key = lambda x: x[2])

    circuits = [[i] for i in range(len(boxes))]
    box_circuit = [i for i in range(len(boxes))] # list of which circuit each box belongs to

    pair_idx = 0
    n_circuits = len(circuits)
    while(n_circuits > 1):
        i, j, _ = pairs[pair_idx]

        i_circuit_idx = box_circuit[i]
        j_circuit_idx = box_circuit[j]
        
        if i_circuit_idx != j_circuit_idx:
            circuits[i_circuit_idx] += circuits[j_circuit_idx]
            for b in circuits[j_circuit_idx]:
                box_circuit[b] = i_circuit_idx
            circuits[j_circuit_idx] = []
            n_circuits -= 1

        pair_idx += 1

    return boxes[i][0] * boxes[j][0]

def main_faster():
    parsedA_example = parseA("einput.txt")
    result = partA_faster(parsedA_example, 10)
    print(result)
    assert result == 40

    parsedA = parseA("input.txt")
    result = partA_faster(parsedA, 1000)
    print(result)
    assert result == 66640

    result = partB_faster(parsedA_example)
    print(result)
    assert result == 25272
    
    result = partB_faster(parsedA)
    print(result)
    assert result == 78894156


if __name__ == '__main__':
    main_faster()