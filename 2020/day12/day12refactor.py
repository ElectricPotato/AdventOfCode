
#based on https://gist.github.com/mcleonard/5351452
class Vector(object):
    def __init__(self, *args):
        #Create a vector, example: v = Vector(1,2)
        if len(args)==0: self.values = (0,0)
        else: self.values = args

    def manhattanDist(self):
        return sum(map(abs, self.values))

    def rotateCW(self, deg):
        dir = (deg//90) % 4
        x, y = self.values
        if(dir==1):
            self.values = (y, -x) #90 deg CW
        elif(dir==2):
            self.values = (-x, -y) #180 deg CW
        elif(dir==3):
            self.values = (-y, x) #90 degrees CCW

    def rotateCCW(self, deg):
        self.rotateCW(-deg)

    def __mul__(self, other):
        #only scalar multiplication supported
        if isinstance(other, (int, float)):
            product = tuple( a * other for a in self )
            return self.__class__(*product)
        else:
            raise ValueError("Addition with type {} not supported (only scalar multiplication supported)".format(type(other)))
    
    def __rmul__(self, other):
        """ Called if 4 * self for instance """
        return self.__mul__(other)
    
    def __add__(self, other):
        """ Returns the vector addition of self and other """
        if isinstance(other, Vector):
            added = tuple( a + b for a, b in zip(self, other) )
        else:
            raise ValueError("Addition with type {} not supported".format(type(other)))
        
        return self.__class__(*added)

    def __radd__(self, other):
        """ Called if 4 + self for instance """
        return self.__add__(other)
    
    def __sub__(self, other):
        """ Returns the vector difference of self and other """
        if isinstance(other, Vector):
            subbed = tuple( a - b for a, b in zip(self, other) )
        else:
            raise ValueError("Subtraction with type {} not supported".format(type(other)))
        
        return self.__class__(*subbed)
    
    def __rsub__(self, other):
        """ Called if 4 - self for instance """
        return self.__sub__(other)

    def __repr__(self):
        return str(self.values)

    def __iter__(self):
        return self.values.__iter__()


dirVect = {"N":Vector(0,1), "E":Vector(1,0), "S":Vector(0,-1), "W":Vector(-1,0)}

def parseInstr(inputText):
    return [(instr[0], int(instr[1:])) for instr in inputText.split()]

def partA(inputText):
    prog = parseInstr(inputText)
    fwdVect = dirVect["E"] * 1 #multiplying by 1 copies the vector instead of using the same object
    shipPos = Vector(0,0)
    for instr, arg in prog:
        if(instr in dirVect):
            shipPos += dirVect[instr] * arg
        elif(instr=="R"):
            fwdVect.rotateCW(arg)
        elif(instr=="L"):
            fwdVect.rotateCCW(arg)
        elif(instr=="F"):
            shipPos += fwdVect * arg
        #print(shipPos, fwdVect, instr, arg)
    return shipPos.manhattanDist()

def partB(inputText):
    prog = parseInstr(inputText)
    shipPos = Vector(0,0)
    waypointPos = Vector(10, 1) #relative to ship
    for instr, arg in prog:
        if(instr in dirVect):
            waypointPos += dirVect[instr] * arg
        elif(instr=="R"):
            waypointPos.rotateCW(arg)
        elif(instr=="L"):
            waypointPos.rotateCCW(arg)
        elif(instr=="F"):
            shipPos += waypointPos * arg
        #print(shipPos, waypointPos)
    return shipPos.manhattanDist()



inputFile = open("input.txt", "r")
#inputFile = open("inputEx2.txt", "r")
inputText = inputFile.read()

print("partA", partA(inputText))
print("partB", partB(inputText))

#partA 962
#partB 56135