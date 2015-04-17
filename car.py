class Car(object):
    """docstring for Car"""

    xCoord = 0
    yCoord = 0
    length = 1
    direction = 1 # 0 for vertical, 1 for horizontal
    color = 0
    carID = 0

    canMove = False

    isWinCar = False

    def __init__(self, xCoord, yCoord, length, direction, carID, color=0, isWinCar=False):
        self.setXCoord(xCoord)
        self.setYCoord(yCoord)
        self.setLength(length)
        self.setDirection(direction)
        self.setColor(color)
        self.setCarID(carID)
        self.isWinCar = isWinCar

    def getXCoord(self):
        return self.xCoord

    def setXCoord(self, x):
        self.xCoord = x

    def getYCoord(self):
        return self.yCoord

    def setYCoord(self, y):
        self.yCoord = y

    def getCoords(self):
        return (self.xCoord, self.yCoord)

    def setCoords(self, coords):
        self.xCoord = coords[0]
        self.yCoord = coords[1]

    def getLength(self):
        return self.length

    def setLength(self, length):
        self.length = length

    def getDirection(self):
        return self.direction

    def setDirection(self, d):
        self.direction = d

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def move(self, distance):
        if self.getDirection():
            self.xCoord =  self.xCoord + distance
        else:
            self.yCoord = self.yCoord + distance

    def getCanMove(self):
        return self.canMove

    def setCanMove(self, canMove):
        self.canMove = canMove

    def setCarID(self, carID):
        self.carID = carID

    def getCarID(self):
        return self.carID

    def __str__(self):
        return "carID:%d, Coords: (%d, %d), len: %d, direction: %d" % (self.getCarID(), self.getXCoord(), self.getYCoord(), self.getLength(), self.getDirection())