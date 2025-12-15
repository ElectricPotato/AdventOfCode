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

#recursive solution
def partA_one(buttons, joltage):
    if len(joltage) > 1:
        pass #recurse
    else:
        valid_buttons_values = [button[0][0] for button in buttons if joltage[0] % button[0][0] == 0]
        if len(valid_buttons_values) == 0:
            return None
        else:
            return joltage[0] // max(valid_buttons_values)

def partB(parsed):
    return sum(partA_one(buttons, joltage) for _, buttons, joltage in parsed)

def main():
    parsedA_example = parseA("einput.txt")
    result = partA(parsedA_example)
    print(result)
    assert result == 7

    parsedA = parseA("input.txt")
    result = partA(parsedA)
    print(result)
    assert result == 436

    result = partB(parsedA_example)
    print(result)
    assert result == 33
    
    result = partB(parsedA)
    print(result)
    #assert result == 

    


if __name__ == '__main__':
    main()