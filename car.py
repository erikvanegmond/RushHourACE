class Car(object):
    """docstring for Car"""

    xCoord = 0
    yCoord = 0
    length = 1
    direction = 1 # 0 for vertical, 1 for horizontal
    color = ''

    def __init__(self, xCoord, yCoord, length, direction, color="yellow"):
        return None

    def getXCoord(self):
        return self.xCoord

    def getYCoord(self):
        return self.yCoord

    def getLength(self):
        return self.length

    def getDirection(self):
        return self.direction

    def setColor(self, color):
        self.color = color

    def move(self, distance):
        pass

    def checkMove(self, distance):
        return True