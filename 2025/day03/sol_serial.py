from sol import parseA, partB_one_line

#another solution, which requires only reading in one character at a time
def partB_serial_one_line(line):
    total_digits = 12

    buffer = [0] * total_digits
    while len(line) > 0:
        line_digit = line.pop(0)
        for digit_idx in range(total_digits):
            if digit_idx != total_digits - 1:
                next_buffer_value = buffer[digit_idx + 1]
            else:
                next_buffer_value = line_digit

            if buffer[digit_idx] < next_buffer_value:
                buffer.pop(digit_idx)
                buffer.append(line_digit)
                break

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
            assert False

    print("ok")


def main():
    parsedA_example = parseA("einput.txt")
    parsedA = parseA("input.txt")

    compare_partB_serial(parsedA_example)
    compare_partB_serial(parsedA)

if __name__ == '__main__':
    main()