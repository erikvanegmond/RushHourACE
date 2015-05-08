from car import *
import copy as cp
from collections import deque

class Board():
    """docstring for Board"""

    width = 6
    height = 6

    exitCoord = (0,0)

    cars = []
    numCars = 1 #initial carID, increases with each car.

    parent = None

    # variables for aStar
    gCost = 0
    hCost = 0

    path = deque()

    winCarID = 0
    grid = []

    def getGCost(self):
        return self.gCost

    def getHCost(self):
        car = self.cars[self.winCarID - 1]
        distance = self.width - car.xCoord - car.length
        self.hCost = distance
        return self.hCost

    def getHCost2(self):
        car = self.cars[self.winCarID - 1]
        distance = self.width - car.xCoord - car.length
        self.hCost = distance + self.blockingCars()
        return self.hCost

    def getFCost(self):
        return self.gCost + self.getHCost2()

    def setParent(self, board):
        self.parent = board

    def getParent(self):
        return self.parent

    def __init__(self, width = 6, height = 6):
        self.width = width
        self.height = height
        self.grid = [[0 for x in range(width)] for x in range(height)]
        self.cars = []
        self.numCars = 1

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getCars(self):
        return self.cars

    def addCar(self, coords, length, direction, color=0, isWinCar=False):
        carID = self.numCars
        car = Car(coords[0], coords[1], length, direction, carID, color, isWinCar)
        if self.roomForACarBySettings(coords, direction, length):
            self.cars.append(car)
            self.addNumbers(car)
            if isWinCar:
                self.setWinCarID(carID)
            self.numCars += 1
        else:
            print "can not add this car!", car

    def moveCarByID(self, carID, distance):
        car = self.cars[carID-1]
        self.addZeros(car)
        car.move(distance)
        self.path.appendleft((carID, distance))
        self.addNumbers(car)


    def roomForACar(self, car):
        coords = car.getCoords()
        direction = car.getDirection()
        length = car.getLength()

        for i in range(0,length):
            if (direction and self.grid[coords[1]][coords[0]+i]) or (not direction and self.grid[coords[1]+i][coords[0]]):
                return False
        return True


    def roomForACarBySettings(self, coords, direction, length):
        yCoord1 = coords[1]
        xCoord2 = coords[0]
        for i in range(0,length):
            xCoord1 = coords[0]+i
            yCoord2 = coords[1]+i
            if (direction and (not (0 <= yCoord1 < self.height and 0 <= xCoord1 < self.width ))):
                return False

            if not direction and (not ( 0 <= yCoord2 < self.height and 0 <= xCoord2 < self.width)):
                return False
            if (direction and self.grid[yCoord1][xCoord1]) or (not direction and self.grid[yCoord2][xCoord2]):
                return False
        return True

    def blockingCars(self):
        car = self.cars[self.winCarID - 1]
        yCoord = car.getYCoord()
        numCars = 0
        for i in range(car.getXCoord() + car.getLength(), self.width):
            if self.grid[yCoord][i]:
                numCars += 1
        return numCars

    def setCarsMovable(self):
        cars = self.getCarsToUpdate()

        for car in cars:
            self.setCarMovable(car)

    def setCarMovable(self, car):
        coords = car.getCoords()
        direction = car.getDirection()
        length = car.getLength()

        if direction:
            if (coords[0]-1 >= 0 and not self.grid[coords[1]][coords[0]-1]) or (coords[0]+length < self.width and not self.grid[coords[1]][coords[0]+length]):
                car.setCanMove(True)
                return
        else:
            if (coords[1]-1 >= 0 and not self.grid[coords[1]-1][coords[0]]) or (coords[1]+length < self.height and not self.grid[coords[1]+length][coords[0]]):
                car.setCanMove(True)
                return

        car.setCanMove(False)

    def carCanMoveForward(self, car):
        coords = car.getCoords()
        direction = car.getDirection()
        length = car.getLength()

        if direction:
            if (coords[0]+length < self.width and not self.grid[coords[1]][coords[0]+length]):
                return True
        else:
            if (coords[1]+length < self.height and not self.grid[coords[1]+length][coords[0]]):
                return True
        return False

    def carCanMoveBackward(self, car):
        coords = car.getCoords()
        direction = car.getDirection()

        if direction:
            if (coords[0]-1 >= 0 and not self.grid[coords[1]][coords[0]-1]):
                return True
        else:
            if (coords[1]-1 >= 0 and not self.grid[coords[1]-1][coords[0]]):
                return True
        return False

    def checkPossibleMoves(self):
        cars = self.getCarsToUpdate()
        movableCars = []
        for car in cars:
            if car.getCanMove():
                movableCars.append( car )


        possibleMoves = set()

        for car in movableCars:
            coords = car.getCoords()
            horizontal = car.getDirection()
            length = car.getLength()
            carID = car.getCarID()
            self.addZeros(car)
            x = 0
            y = 1

            if horizontal:
                # for distance in range(-self.width+1, self.width):
                #     if not self.width - 1 > distance + coords[x] + length > 0:
                #         continue
                #     elif coords[x] + length < self.width and not self.grid[coords[y]][coords[x] + length + distance]:
                #         if self.roomForACarBySettings((coords[x] + distance, coords[y]), horizontal, length):
                #             possibleMoves.append((carID, distance))
                tempCoords = list(coords)
                while tempCoords[x] < self.width:
                    if self.roomForACarBySettings(tempCoords, horizontal, length):
                        distance = tempCoords[x] - coords[x]
                        if distance:
                            possibleMoves.add((carID, distance))
                    else:
                        break
                    tempCoords[x] += 1

                tempCoords = list(coords)
                while tempCoords[x] >= 0:
                    if self.roomForACarBySettings(tempCoords, horizontal, length):
                        distance = tempCoords[x] - coords[x]
                        if distance:
                            possibleMoves.add((carID, distance))
                    else:
                        break
                    tempCoords[x] -= 1
            else:
                tempCoords = list(coords)
                while tempCoords[y] < self.height:
                    if self.roomForACarBySettings(tempCoords, horizontal, length):
                        distance = tempCoords[y] - coords[y]
                        if distance:
                            possibleMoves.add((carID, distance))
                    else:
                        break
                    tempCoords[y] += 1

                tempCoords = list(coords)
                while tempCoords[y] >= 0:
                    if self.roomForACarBySettings(tempCoords, horizontal, length):
                        distance = tempCoords[y] - coords[y]
                        if distance:
                            possibleMoves.add((carID, distance))
                    else:
                        break
                    tempCoords[y] -= 1

                # for distance in range(-self.height+1, self.height):


                    # if not  self.height - 1 > coords[y] + distance + length > 0:
                    #     continue
                    # elif coords[y] + length < self.height and not self.grid[coords[y] + length + distance][x]:
                    #     if self.roomForACarBySettings((coords[x], coords[y] + distance), horizontal, length):
                    #         possibleMoves.append((carID, distance))
            self.addNumbers(car)

        return possibleMoves

    def getCarsToUpdate(self):
        # laatste move in het pad ophalen --> self.path.appendleft((carID, distance))
        cars = list()
        
        if self.path: 
            lastchange = self.path[0][0]
            
            changedcar = self.cars[lastchange - 1]

            carids = set()

            if changedcar.getDirection():
                y = changedcar.getYCoord()
                carids.update(self.grid[y])
                if y :
                    carids.update(self.grid[y - 1])
                if y+1 < self.height:
                    carids.update(self.grid[y + 1])
            else:
                for row in self.grid:
                    x = changedcar.getXCoord()
                    if x:
                        carids.add(row[x-1])
                    carids.add(row[x])
                    if x+1<self.width:
                        carids.add(row[x+1])

            if self.path:
                carids = list(carids)
                if 0 in carids:
                    carids.remove(0)

                for carid in carids:
                    cars.append(self.cars[carid - 1])

        else:
            cars = self.cars
        return cars
    def setExitCoord(self, exitCoord):
        self.exitCoord = exitCoord

    def getExitCoord(self):
        return self.exitCoord

    def setWinCarID(self, ID):
        self.winCarID = ID

    def getMoveToNewState(self, newStateString):
        grid = range(0, self.width)
        for i in range(0,self.width):
            grid[i] = range(0,self.height)
            for j in range(0,self.height):
                grid[i][j] = int(newStateString[(i*self.width)+j])

        for x in grid:
            for y in x:
                print y, " ",
            print ""
        print " "
        print self.printGrid()

        for i,x in enumerate(self.grid):
            for j,y in enumerate(x):
                if grid[i][j] == y:
                    continue
                else:
                    print y, grid[i][j], i, j
                    id = y if y else grid[i][j]
                    if id:
                        print self.cars[id -1]

                    else:
                        print "huh?"
                        return    
                    exit()



    def checkForWin(self):
        car = self.cars[self.winCarID - 1]
        if car.getXCoord() + car.getLength() - 1 == self.exitCoord[0]:
            # print 'Game won!'
            # self.printGrid()
            return True
        return False

    def addNumbers(self, car):
        coords = car.getCoords()
        direction = car.getDirection()
        length = car.getLength()
        carID = car.getCarID()

        for i in range(0,length):
            if direction:
                self.grid[coords[1]][coords[0]+i] = carID
            else:
                self.grid[coords[1]+i][coords[0]] = carID

    def addZeros(self, car):
        coords = car.getCoords()
        direction = car.getDirection()
        length = car.getLength()

        for i in range(0,length):
            if direction:
                self.grid[coords[1]][coords[0]+i] = 0
            else:
                self.grid[coords[1]+i][coords[0]] = 0

    def printGrid(self):
        for x in self.grid:
            for y in x:
                print y, " ",
            print ""

        print " "



    def toString(self):
        result = ''
        for x in self.grid:
            result += "".join(map(str, x))
            # for y in x:
            #     result += str(y)
        return result

    def __str__(self):
        return 'board'

    def copy(self):
        copy = Board(self.width, self.height)
        for car in self.cars:
            copy.addCar(car.getCoords(), car.getLength(), car.getDirection(), car.getColor(), car.isWinCar)
        copy.setExitCoord(self.getExitCoord())
        copy.path = cp.deepcopy(self.path)

        return copy






