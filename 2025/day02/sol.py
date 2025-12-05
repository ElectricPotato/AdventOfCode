import math

def parseA(filename):
    with open(filename) as file:
        content = file.read()
    content = content.strip("\n\r")
    
    return [[int(i) for i in pair.split("-")] for pair in content.split(",")]


'''
repeating digits
11 - 99, multiples of 11, 1 to 9
1010 - 9999, multiples of 101, 10 to 99
100100 - 999999, multiples of 1001, 100 to 999
'''

#sum of numbers in the range a to b, inclusive
def tri_sum(a, b):
    return (b * (b + 1) // 2) - ((a - 1) * a // 2)

def n_digits(n):
    return math.floor(math.log10(n)) + 1

def one_rangeA(start, end):
    total = 0
    
    #get the number of digits to start with
    start_ndigits = n_digits(start)

    #round up to nearest even number
    if start_ndigits % 2 != 0: start_ndigits += 1
    start_half_ndigits = start_ndigits // 2

    while True:
        current_range_multiples = 10 ** start_half_ndigits + 1
        current_range_multiplier_start = 10 ** (start_half_ndigits - 1)
        current_range_multiplier_end = 10 ** start_half_ndigits - 1

        multiplier_start = max(math.ceil(start / current_range_multiples), current_range_multiplier_start)

        multiplier_end = min(math.floor(end / current_range_multiples), current_range_multiplier_end)

        #if the range doesnt include any valid numbers, then stop
        if multiplier_end < multiplier_start:
            break

        #check if the range include at least one valid number, otherwise stop
        if multiplier_start == multiplier_end:
            if not (start <= (current_range_multiples * multiplier_start) <= end):
                break

        total += current_range_multiples * tri_sum(multiplier_start, multiplier_end)

        #check if to go into the next range
        if end > current_range_multiples * current_range_multiplier_end:
            start_half_ndigits += 1
        else:
            break

        
    return total

def partA(parsed):
    return sum(one_rangeA(start, end) for start, end in parsed)

'''
repeating digits
2 digits:
  1 digit pattern x2: 11 - 99, multiples of 11, 1 to 9

3 digits:
  1 digit pattern x3: 111 - 999, multiples of 111, 1 to 9

4 digits:
  1 digit pattern x4: 1111 - 9999, multiples of 1111,  1 to  9
  2 digit pattern x2: 1010 - 9999, multiples of  101, 10 to 99, (this overlaps with d1 completely)

  2d,1d

5 digits:
  1 digit pattern x5
  
6 digits:
  1d x6: 111111 - 999999, multiples of 111111, range   1 to   9
  2d x3: 101010 - 999999, multiples of  10101, range  10 to  99, (this overlaps with d1 completely)
    not including multiples of 11,22,...,99 i.e. 11 * (1 to 9)
  3d x2: 100100 - 999999, multiples of   1001, range 100 to 999, (this overlaps with d1 completely)
    not including multiples of 111,222,...,999 i.e. 111 * (1 to 9)

  3d,1d 2d,1d  -1d

7 digits:
  1d x7

8 digits:
  1d x8: multiples of 11111111, range    1 to    9
  2d x4: multiples of  1010101, range   10 to   99, (this overlaps with d1 completely)
    not including multiples of 11,22,...,99 i.e. 11 * (1 to 9)
  4d x2: multiples of    10001, range 1000 to 9999, (this overlaps with d1 and d2 completely)
    not including multiples of 101,202,...,9999 i.e. 101 * (10 to 99)

  4d,2d,1d

12d:

  6d,3d,2d,1d  4d,2d,1d  -2d,-1d

30d:

  15d,5d,3d,1d  10d,5d,2d,1d  6d,3d,2d,1d  (5d skip) (3d skip) (2d skip) (1d skip)


'''

def factors(n):
    return [n//i for i in range(1, n + 1) if n % i == 0]

def pattern_features(pattern_length, pattern_repeats):
    multiple = 1
    for i in range(pattern_repeats - 1):
        multiple = multiple * 10 ** pattern_length + 1

    range_start = 10 ** (pattern_length - 1)
    range_end   = 10 ** pattern_length - 1

    return (multiple, range_start, range_end)

# boolean union of two ranges (a1, b1) and (a2, b2)
def range_overlap(a1, b1, a2, b2):
    assert a1 <= b1 and a2 <= b2

    if a1 <= a2 <= b1 or a1 <= b2 <= b1:
        return (max(a1, a2), min(b1, b2))
    else:
        return None

def sum_pattern(pattern_length, ndigits, start, end):
    multiple, range_start, range_end = pattern_features(pattern_length, ndigits // pattern_length)

    defined_range_start = math.ceil(start/multiple)
    defined_range_end = math.floor(end/multiple)

    if defined_range_start > defined_range_end:
        return 0
    
    overlap = range_overlap(range_start, range_end, defined_range_start, defined_range_end)
    if overlap == None:
        return 0
    
    overlap_start, overlap_end = overlap
    return multiple * tri_sum(overlap_start, overlap_end)

def one_rangeB(start, end):
    total = 0
    for ndigits in range(n_digits(start), n_digits(end) + 1):
        pattern_lengths_covered = {}

        #go from longest pattern to shortest

        #this can be done better using linear algebra (vector divided by matrix?)
        #matrix of factors of each length * vector with the "need" values for each length = vector of all 1s
        for pattern_length in factors(ndigits)[1:]:
            if pattern_length not in pattern_lengths_covered:
                need = 1
            else:
                need = 1 - pattern_lengths_covered[pattern_length]

            if need == 0:
                continue

            for factor in factors(pattern_length):
                if factor not in pattern_lengths_covered:
                    pattern_lengths_covered[factor] = need
                else:
                    pattern_lengths_covered[factor] += need

            total += need * sum_pattern(pattern_length, ndigits, start, end)

    return total

def partB(parsed):
    return sum(one_rangeB(start, end) for start, end in parsed)

def main():
    parsedA_example = parseA("einput.txt")
    result = partA(parsedA_example)
    print(result)
    assert result == 1227775554

    parsedA = parseA("input.txt")
    result = partA(parsedA)
    print(result)

    result = partB(parsedA_example)
    print(result)
    assert result == 4174379265
    
    result = partB(parsedA)
    print(result)

    


if __name__ == '__main__':
    main()