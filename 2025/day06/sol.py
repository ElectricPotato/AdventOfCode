
#transpose a list of lists
def transpose(ll):
    return [[row[i] for row in ll] for i in range(len(ll[0]))]

def parseA(filename):
    with open(filename) as file:
        lines = file.readlines()

    lines_split = [line.split() for line in lines]

    number_lists = lines_split[:-1]
    operation_list = lines_split[-1]

    number_lists = [list(map(int,number_list)) for number_list in number_lists]

    return list(zip(transpose(number_lists), operation_list))

def product(ns):
    p = 1
    for n in ns:
        p *= n

    return p

def partA(parsed):
    total = 0
    for number_list, operation in parsed:
        if operation == '*':
            total += product(number_list)
        else:
            total += sum(number_list)

    return total

def split_list(l, delimmer):
    current_group = []
    result = []
    for i in l:
        if i == delimmer:
            result.append(current_group)
            current_group = []
        else:
            current_group.append(i)

    result.append(current_group)

    return result


#it is assumed all the lines are the same length
def parseB(filename):
    with open(filename) as file:
        lines = file.readlines()

    lines = [line.replace("\n","") for line in lines]

    number_lines = lines[:-1]
    operation_line = lines[-1].split()[::-1] #read right-to-left

    #[::-1] to reverse the lines - read right-to-left
    number_lines = [''.join(column).strip() for column in transpose(number_lines)[::-1]]
    number_lines = split_list(number_lines, "")
    number_lines = [list(map(int, ns)) for ns in number_lines]
    
    return list(zip(number_lines, operation_line))

#the problem is solved the same way for part B as for part A, after it is parsed differently
partB = partA

def main():
    parsedA_example = parseA("einput.txt")
    result = partA(parsedA_example)
    print(result)
    assert result == 4277556

    parsedA = parseA("input.txt")
    result = partA(parsedA)
    print(result)
    assert result == 4951502530386

    parsedB_example = parseB("einput.txt")
    result = partB(parsedB_example)
    print(result)
    assert result == 3263827
    
    parsedB = parseB("input.txt")
    result = partB(parsedB)
    print(result)
    assert result == 8486156119946

    


if __name__ == '__main__':
    main()