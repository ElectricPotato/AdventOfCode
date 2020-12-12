'''

'''

def partA(inputText):
    prog = [(instr[0], int(instr[1:])) for instr in inputText.split()]
    facing = 1 #N=0,E=1,S=2,W=3
    xPos, yPos = 0, 0
    for instr, arg in prog:
        if(instr=="N"):
            yPos += arg
        elif(instr=="E"):
            xPos += arg
        elif(instr=="S"):
            yPos -= arg
        elif(instr=="W"):
            xPos -= arg
        elif(instr=="L"):
            facing = (facing - arg//90) % 4
        elif(instr=="R"):
            facing = (facing + arg//90) % 4
        elif(instr=="F"):
            if(facing==0):
                yPos += arg
            elif(facing==1):
                xPos += arg
            elif(facing==2):
                yPos -= arg
            elif(facing==3):
                xPos -= arg
        #print(xPos,yPos,facing)
    return abs(xPos) + abs(yPos)

def partB(inputText):
    prog = [(instr[0], int(instr[1:])) for instr in inputText.split()]
    shipXPos, shipYPos = 0, 0
    waypointXPos, waypointYPos = 10, 1 #relative to ship
    for instr, arg in prog:
        if(instr=="N"):
            waypointYPos += arg
        elif(instr=="E"):
            waypointXPos += arg
        elif(instr=="S"):
            waypointYPos -= arg
        elif(instr=="W"):
            waypointXPos -= arg
        elif(instr=="R"):
            for i in range(arg//90):
                waypointXPos, waypointYPos = waypointYPos, -waypointXPos
        elif(instr=="L"):
            for i in range(arg//90):
                waypointXPos, waypointYPos = -waypointYPos, waypointXPos
        elif(instr=="F"):
            shipXPos += waypointXPos * arg
            shipYPos += waypointYPos * arg
        print(f"S({shipXPos}, {shipYPos}), WP({waypointXPos}, {waypointYPos})")
    return abs(shipXPos) + abs(shipYPos)



inputFile = open("input.txt", "r")
#inputFile = open("inputEx.txt", "r")
inputText = inputFile.read()

print("partA", partA(inputText))
print("partB", partB(inputText))