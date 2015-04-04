from car import *

class Board():
    """docstring for Board"""

    width = 6
    height = 6

    exitCoords = (6,3) # (xCoord, yCoord)

    cars = []
    numCars = 1

    grid = [[0 for x in range(width)] for x in range(height)]

    def __init__(self):
        print "init board"

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getCars(self):
        return self.cars

    def addCar(self, coords, lenght, direction, color=0):
        carID = self.numCars
        car = Car(coords[0], coords[1], lenght, direction, carID, color)
        if self.roomForACar(car):
            self.cars.append(car)
            self.addNumbers(car)
            self.numCars += 1
        else:
            print "can not add this car!"

    def roomForACar(self, car):
        coords = car.getCoords()
        direction = car.getDirection()
        lenght = car.getLength()

        for i in range(0,lenght):
            if (direction and self.grid[coords[1]][coords[0]+i]) or (not direction and self.grid[coords[1]+i][coords[0]]):
                return False
        return True

    def setCarsMovable(self):
        for car in self.cars:
            self.setCarMovable(car)

    def setCarMovable(self, car):
        coords = car.getCoords()
        direction = car.getDirection()
        lenght = car.getLength()
        if direction:
            if (coords[0]-1 >= 0 and not self.grid[coords[1]][coords[0]-1]) or (coords[0]+lenght < self.width and not self.grid[coords[1]][coords[0]+lenght]):
                car.setCanMove(True)
                return
        else:
            if (coords[1]-1 >= 0 and not self.grid[coords[1]-1][coords[0]]) or (coords[1]+lenght < self.height and not self.grid[coords[1]+lenght][coords[0]]):
                car.setCanMove(True)
                return
        car.setCanMove(False)

    def carCanMoveForeward(self, car):
        coords = car.getCoords()
        direction = car.getDirection()
        lenght = car.getLength()
        if direction:
            if (coords[0]+lenght < self.width and not self.grid[coords[1]][coords[0]+lenght]):
                return True
        else:
            if (coords[1]+lenght < self.height and not self.grid[coords[1]+lenght][coords[0]]):
                return True
        return False

    def carCanMoveBackward(self, car):
        coords = car.getCoords()
        direction = car.getDirection()
        lenght = car.getLength()
        if direction:
            if (coords[0]-1 >= 0 and not self.grid[coords[1]][coords[0]-1]):
                return True
        else:
            if (coords[1]-1 >= 0 and not self.grid[coords[1]-1][coords[0]]):
                return True
        return False


    def setExitCoord(self, exitCoord):
        self.exitCoord = exitCoord

    def addNumbers(self, car):
        coords = car.getCoords()
        direction = car.getDirection()
        lenght = car.getLength()
        carID = car.getCarID()

        for i in range(0,lenght):
            if direction:
                self.grid[coords[1]][coords[0]+i] = carID
            else:
                self.grid[coords[1]+i][coords[0]] = carID

    def addZeros(self, car):
        coords = car.getCoords()
        direction = car.getDirection()
        lenght = car.getLength()

        for i in range(0,lenght):
            if direction:
                self.grid[coords[1]][coords[0]+i] = 0
            else:
                self.grid[coords[1]+i][coords[0]] = 0

    def printGrid(self):

        for x in self.grid:
            for y in x:
                print y, " ",
            print ""
