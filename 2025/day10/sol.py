from typing import List

def parseA(filename):
    with open(filename) as file:
        lines = file.readlines()

    lines = [line.replace("\n","") for line in lines]

    parsed = []
    for line in lines:
        parts = line.split(" ")

        lights = parts[0]
        buttons = parts[1:-1]
        joltage = parts[-1]

        lights = [l == "#" for l in lights[1:-1]]
        buttons = [list(map(int, b[1:-1].split(","))) for b in buttons]
        joltage = list(map(int, joltage[1:-1].split(",")))

        parsed.append((lights, buttons, joltage))

    return parsed

def popcount(n):
    count = 0
    while n > 0:
        count += n & 1
        n = n >> 1

    return count

#brute force solution
#(it could be made more efficient by using bitfields and XOR)
def partA_one(machine):
    lights, buttons, _ = machine
    min_presses = len(buttons)

    for i in range(2 ** len(buttons)): #each combination of button presses
        current_lights = [False] * len(lights)
        for button_idx in range(len(buttons)):
            if not (i & 1 << button_idx):
                continue #button not pressed

            for light_toggle in buttons[button_idx]:
                current_lights[light_toggle] = not current_lights[light_toggle]

        if current_lights == lights:
            #valid solution
            min_presses = min(min_presses, popcount(i))

    return min_presses

def partA(parsed):
    return sum(partA_one(machine) for machine in parsed)

def new_matrix(n_rows, n_cols):
    return [[0] * n_cols for _ in range(n_rows)]

def row_leading_zeros(row):
    count = 0
    for element in row:
        if element != 0:
            break
        count += 1

    return count

#row_a -= row_b * n
def sub_row(m, row_a, row_b, n):
    for i in range(len(m[0])):
        m[row_a][i] -= m[row_b][i] * n

#row_i *= n
def divide_row(m, row_i, n):
    for i in range(len(m[0])):
        #assert m[row_i][i] % n == 0, "a non-integer division has happened"
        #if(m[row_i][i] % n != 0): print(f"non integer {m[row_i][i]}/{n}")
        m[row_i][i] /= n

#turn into Row Echelon Form
def matrix_ref(m: List[List[int]]):

    row_n = 0
    col_n = 0
    m.sort(key = row_leading_zeros)

    while True:
        divide_row(m, row_n, m[row_n][col_n]) #normalise row
        for row_idx in range(row_n + 1, len(m)):
            sub_row(m, row_idx, row_n, m[row_idx][col_n])

        m.sort(key = row_leading_zeros) #sort after row operations

        #find the next pivot (non zero value)
        row_n += 1
        col_n += 1
        if row_n >= len(m) or col_n >= len(m[0]) - 1:
            break

        while m[row_n][col_n] == 0:
            col_n += 1

            if col_n >= len(m[0]) - 1:
                break

        if col_n >= len(m[0]) - 1:
                break

#turn into Row Echelon Form
#(reduce as much as possible)
def matrix_rref(m: List[List[int]]):
    row_n = 0
    col_n = 0

    while True:
        for row_i in range(len(m)):
            if row_i == row_n:
                continue
            sub_row(m, row_i, row_n, m[row_i][col_n])

        #find the next pivot (non zero value)
        row_n += 1
        col_n += 1
        if row_n >= len(m) or col_n >= len(m[0]) - 1:
            break

        while m[row_n][col_n] == 0:
            col_n += 1

            if col_n >= len(m[0]) - 1:
                break

        if col_n >= len(m[0]) - 1:
                break

def remove_zero_rows(m):
    row_idx = 0
    while row_idx < len(m):
        if all(e == 0 for e in m[row_idx]):
            m.pop(row_idx)
        else:
            row_idx += 1


def show_matrix(m):
    for row in m:
        print('\t'.join(list(map(str, row))))

#Linear algebra solution
def partA_one(buttons, joltages):

    #augmented matrix
    button_matrix = new_matrix(len(joltages), len(buttons) + 1)

    #populate matrix
    for button_idx, button in enumerate(buttons):
        for joltage_idx in button:
            button_matrix[joltage_idx][button_idx] = 1

    for joltage_idx, joltage in enumerate(joltages):
        button_matrix[joltage_idx][len(buttons)] = joltage

    #turn into Row Echelon Form
    matrix_ref(button_matrix)

    #turn into (somewhat) Reduced Row Echelon Form
    matrix_rref(button_matrix)

    remove_zero_rows(button_matrix)

    #print()
    #show_matrix(button_matrix)
    free_var = len(button_matrix[0]) - 1 - len(button_matrix)
    print("free variables", )
    if free_var <= 0:
        show_matrix(button_matrix)
    print()

    return 0

def partB(parsed):
    return sum(partA_one(buttons, joltage) for _, buttons, joltage in parsed)

def main():
    parsedA_example = parseA("einput.txt")
    #result = partA(parsedA_example)
    #print(result)
    #assert result == 7

    parsedA = parseA("input.txt")
    #result = partA(parsedA)
    #print(result)
    #assert result == 436

    result = partB(parsedA_example)
    #print(result)
    #assert result == 33
    
    result = partB(parsedA)
    #print(result)
    #assert result == 

    


if __name__ == '__main__':
    main()