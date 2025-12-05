def parseA(filename):
    with open(filename) as file:
        lines = file.read().splitlines()

    result = []

    for line in lines:
        result.append(list(map(int, line)))

    return result

def partA_one_line(line):
    first_digit = max(line[:-1])
    line = line[line.index(first_digit) + 1:]

    second_digit = max(line)

    return first_digit * 10 + second_digit

def partA(parsed):
    return sum(partA_one_line(line) for line in parsed)

def partB_one_line(line):
    total_digits = 12

    result = 0
    for digit_idx in range(total_digits):
        remaining_digits = total_digits - digit_idx

        current_digit = max(line[:len(line) - remaining_digits + 1])
        line = line[line.index(current_digit) + 1:]

        result = result * 10 + current_digit #append new digit to result

    return result

def partB(parsed):
    return sum(partB_one_line(line) for line in parsed)

#another solution, which requires only reading in one character at a time
def partB_serial_one_line(line):
    total_digits = 12

    buffer = [0] * total_digits
    while len(line) > 0:
        for digit_idx in range(total_digits):
            if digit_idx == total_digits - 1 or buffer[digit_idx] < buffer[digit_idx + 1]:
                buffer.pop(digit_idx)
                break

        buffer.append(line.pop(0))

    result = 0
    for digit_idx in range(total_digits):
        result = result * 10 + buffer[digit_idx]

    return result

def partB_serial(parsed):
    return sum(partB_serial_one_line(line) for line in parsed)

def compare_partB_serial(parsed):
    for line_idx, line in enumerate(parsed):
        normal = partB_one_line(line)
        serial = partB_serial_one_line(line)
        if serial != normal:
            print(f"{serial}, should be {normal}, line number {line_idx + 1}")
            #assert False

def main():
    parsedA_example = parseA("einput.txt")
    result = partA(parsedA_example)
    print(result)
    assert result == 357

    parsedA = parseA("input.txt")
    result = partA(parsedA)
    print(result)
    assert result == 17087

    assert partB_one_line(list(map(int,"987654321111111"))) == 987654321111
    assert partB_one_line(list(map(int,"811111111111119"))) == 811111111119
    assert partB_one_line(list(map(int,"234234234234278"))) == 434234234278
    assert partB_one_line(list(map(int,"818181911112111"))) == 888911112111

    result = partB(parsedA_example)
    print(result)
    assert result == 3121910778619
    
    result = partB(parsedA)
    print(result)
    assert result == 169019504359949

    compare_partB_serial(parsedA)
    compare_partB_serial(parsedA_example)


if __name__ == '__main__':
    main()