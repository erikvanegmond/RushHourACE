import car

class Board():
    """docstring for Board"""

    width = 6
    height = 6

    exitCoords = (6,3) # (xCoord, yCoord)

    cars = []

    def __init__(self):
        print "init board"

    def getWidth(self):
        return self.width

    def getHeight(self):
        return None

    def getCars(self):
        return None

    def addCar(self, coords, lenght, direction):
        car = Car()
        return None

    def setExitCoord(self, exitCoord):
        self.exitCoord = exitCoord
