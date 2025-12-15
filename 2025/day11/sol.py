def parseA(filename):
    with open(filename) as file:
        lines = file.readlines()

    lines = [line.replace("\n","") for line in lines]

    devices = dict()

    for line in lines:
        device, *to = line.split()
        devices[device[:-1]] = to

    return devices

def partA_recurse(devices, device_from):
    if device_from == "out":
        return 1
    
    return sum(partA_recurse(devices, device_to) for device_to in devices[device_from])

def partA(devices):
    return partA_recurse(devices, "you")

def partB(parsed):

    return None

def main():
    parsedA_example = parseA("einput.txt")
    result = partA(parsedA_example)
    print(result)
    assert result == 5

    parsedA = parseA("input.txt")
    result = partA(parsedA)
    print(result)
    assert result == 477

    result = partB(parsedA_example)
    print(result)
    assert result == 2
    
    result = partB(parsedA)
    print(result)
    #assert result == 

    


if __name__ == '__main__':
    main()