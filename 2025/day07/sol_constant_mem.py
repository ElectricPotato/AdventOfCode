#this solution does not use a python dictionary

from sol import parseA

def partAB_constant_mem(lines):
    start_pos = lines[0].index("S")

    n_splits = 0

    timelines = [0] * len(lines[0])
    timelines[start_pos] = 1

    for line in lines[1:]:
        active_splitters = [i for i in range(len(line)) if line[i] == "^"]

        next_timelines = list(timelines)

        for p in active_splitters:
            if timelines[p] != 0: #part A
                n_splits += 1

            next_timelines[p] = 0

        for p in active_splitters:
            next_timelines[p + 1] += timelines[p]
            next_timelines[p - 1] += timelines[p]

        timelines = next_timelines

    return (n_splits, sum(timelines))

def main():
    parsedA_example = parseA("einput.txt")
    parsedA = parseA("input.txt")

    result_a_example, result_b_example = partAB_constant_mem(parsedA_example)
    print("example part A", result_a_example)
    print("example part B", result_b_example)
    assert result_a_example == 21
    assert result_b_example == 40
    
    result_a, result_b = partAB_constant_mem(parsedA)
    print("part A", result_a)
    print("part B", result_b)
    assert result_a == 1635
    assert result_b == 58097428661390

    


if __name__ == '__main__':
    main()