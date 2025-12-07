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

import math

def clog2(n):
    return math.ceil(math.log2(n))

#find the width of a number written in binary
def bitwidth(n):
    return clog2(n + 1)
    #also equivalent to floor(log2(n)) + 1

#round up to the next power of 2
def round_up_to_power2(n):
    return 2 ** clog2(n)

#calculate the number of bits needed for each part
#(for a possible hardware implementation)
def partAB_find_bitwidth(lines):
    start_pos = lines[0].index("S")

    n_splits = 0

    timelines = [0] * len(lines[0])
    timelines[start_pos] = 1

    maxval = 0

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

        maxval = max(maxval, max(timelines))

    timeline_sum = sum(timelines)

    print("timelines list:")
    print(f" max value {maxval}")
    print(f" length {len(timelines)}")
    print(f" need: {len(timelines)}x {bitwidth(maxval)}bit registers (round to {round_up_to_power2(bitwidth(maxval))} bit)")

    print("registers for answers")
    print(f"total, value {timeline_sum}, {bitwidth(timeline_sum)} bits (round to {round_up_to_power2(bitwidth(timeline_sum))} bit)")
    print(f"total splits, value {n_splits}, {bitwidth(n_splits)} bits (round to {round_up_to_power2(bitwidth(n_splits))} bit)")
    

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

    print()
    print("example")
    partAB_find_bitwidth(parsedA_example)
    print()
    print("real input")
    partAB_find_bitwidth(parsedA)

    


if __name__ == '__main__':
    main()