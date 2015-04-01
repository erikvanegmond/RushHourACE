class Car(object):
    """docstring for Car"""

    xCoord = 0
    yCoord = 0
    lenght = 1
    direction = 1 # 0 for vertical, 1 for horizontal
    color = ''

    def __init__(self, xCoord, yCoord, lenght, direction, color="yellow"):
        return None

    def getXCoord(self):
        return self.xCoord

    def getYCoord(self):
        return self.yCoord

    def getLenght(self):
        return self.lenght

    def getDirection(self):
        return self.direction

    def setColor(self, color):
        self.color = color

    def move(self, distance):
        pass

    def checkMove(self, distance):
        return True