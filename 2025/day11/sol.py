def parseA(filename):
    with open(filename) as file:
        lines = file.readlines()

    lines = [line.replace("\n","") for line in lines]

    devices = dict()

    for line in lines:
        device, *to = line.split()
        devices[device[:-1]] = to

    return devices

def partA_recurse(devices, device_from, destination):
    if device_from == destination:
        return 1
    elif device_from == "out":
        return 0
    
    return sum(partA_recurse(devices, device_to, destination) for device_to in devices[device_from])

def partA(devices):
    return partA_recurse(devices, "you", "out")

def partB(devices):
    #find number of paths svr to fft
    #find number of paths fft to dac
    #find number of paths dac to out

    a = partA_recurse(devices, "svr", "fft")
    print(a)
    b = partA_recurse(devices, "fft", "dac")
    print(b)
    c = partA_recurse(devices, "dac", "out")
    print(c)

    return a * b * c

def main():
    parsedA_example = parseA("einput.txt")
    result = partA(parsedA_example)
    print(result)
    assert result == 5

    parsedA = parseA("input.txt")
    result = partA(parsedA)
    print(result)
    assert result == 477

    print("part b example")
    parsedB_example = parseA("einputB.txt")
    result = partB(parsedB_example)
    print(result)
    assert result == 2
    
    print("part b")
    result = partB(parsedA)
    print(result)
    #assert result == 

    


if __name__ == '__main__':
    main()