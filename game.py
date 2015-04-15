import pygame, sys
from board import *
import screen as sc
from pygame.locals import *
import random
from Queue import *

class Game(object):

    board = None
    screen = None

    windowWidth = 300
    windowHeight = 300

    winState = False

    visitedStates = set()
    statesToVisit = Queue()

    """docstring for Game"""
    def __init__(self):
        pygame.init()

        self.loadGame4()
        self.board.setCarsMovable()

        print self.board.printGrid()

        self.screen = sc.Screen(self.windowWidth, self.windowHeight)

        self.last = pygame.time.get_ticks()
        self.msPerStep = 1

        print self.board.checkPossibleMoves()
        self.runGame()


    def runGame(self):

        while not self.winState:
            now = pygame.time.get_ticks()
            if now - self.last >= self.msPerStep:
                self.last = now
                for event in pygame.event.get():
                    # Event that should close the game.
                    if event.type == QUIT \
                         or (event.type == KEYUP and event.key == K_ESCAPE):
                        self.quitGame()

                self.screen.drawScreen(self.board)
                self.move()
                self.winState = self.board.checkForWin()

                # print self.board.printGrid()
                # Update the screen
                pygame.display.update()
        while True:
            for event in pygame.event.get():
                    # Event that should close the game.
                    if event.type == QUIT \
                         or (event.type == KEYUP and event.key == K_ESCAPE):
                        self.quitGame()
            self.screen.drawScreen(self.board)
            self.screen.drawMessage("Game Won!")
            pygame.display.update()


    def move(self):
        movableCars = []
        for car in self.board.getCars():
            if car.getCanMove():
                movableCars.append( car )

        car = movableCars[random.randint(0,len(movableCars)-1)]
        direction = 1 if random.random()>0.5 else -1
        if car.getCanMove() and ((direction == -1 and self.board.carCanMoveBackward(car)) or (direction == 1 and self.board.carCanMoveForward(car))):
            carID = car.getCarID()
            self.board.moveCarByID(carID, direction)

            self.board.setCarsMovable()


    # Quit the game
    def quitGame(self):
        pygame.quit()
        sys.exit()

    def checkVisitedStates(self, state):
        return state in self.visitedStates

    def addVisitedStates(self, state):
        self.visitedStates.add(state)

    def loadGame1(self):
        width = 6
        height = 6
        self.board = Board(width,height)
        self.board.setExitCoord((5,2))
        self.windowWidth = width * 50
        self.windowHeight = height * 50
        self.board.addCar((3,2),2,1, 0, True)
        self.board.addCar((2,0),3,0, 9)
        self.board.addCar((3,0),2,1, 7)
        self.board.addCar((5,0),3,0, 2)
        self.board.addCar((3,3),3,0, 1)
        self.board.addCar((4,3),2,1, 3)
        self.board.addCar((0,4),2,0, 1)
        self.board.addCar((1,4),2,1, 7)
        self.board.addCar((4,5),2,1, 5)


    def loadGame2(self):
        width = 6
        height = 6
        self.board = Board(width,height)
        self.board.setExitCoord((5,2))
        self.windowWidth = width * 50
        self.windowHeight = height * 50
        self.board.addCar((2,2),2,1, 0, True)
        self.board.addCar((2,0),2,1, 8)
        self.board.addCar((4,0),2,1, 1)
        self.board.addCar((1,1),2,1, 1)
        self.board.addCar((3,1),2,1, 5)
        self.board.addCar((5,1),3,0, 2)
        self.board.addCar((4,2),2,0, 6)
        self.board.addCar((0,3),2,1, 5)
        self.board.addCar((2,3),2,1, 8)
        self.board.addCar((0,4),2,0, 1)
        self.board.addCar((3,4),2,0, 6)
        self.board.addCar((4,4),2,1, 5)
        self.board.addCar((4,5),2,1, 2)

    def loadGame4(self):
        width = 9
        height = 9
        self.board = Board(width,height)
        self.board.setExitCoord((8,4))
        self.windowWidth = width * 50
        self.windowHeight = height * 50
        self.board.addCar((1,4),2,1, 0, True)
        self.board.addCar((0,0),2,0, 5)
        self.board.addCar((1,0),3,1, 2)
        self.board.addCar((5,0),3,0, 11)
        self.board.addCar((3,1),3,0, 9)
        self.board.addCar((6,1),3,1, 9)
        self.board.addCar((8,2),3,0, 2)
        self.board.addCar((0,3),2,1, 7)
        self.board.addCar((5,3),3,1, 2)
        self.board.addCar((0,4),2,0, 3)
        self.board.addCar((3,4),2,0, 4)
        self.board.addCar((2,5),3,0, 2)
        self.board.addCar((5,5),3,1, 10)
        self.board.addCar((8,5),3,0, 2)
        self.board.addCar((0,6),2,1, 1)
        self.board.addCar((3,6),2,0, 8)
        self.board.addCar((4,6),2,1, 4)
        self.board.addCar((0,7),2,0, 8)
        self.board.addCar((4,7),2,0, 1)
        self.board.addCar((1,8),3,1, 11)
        self.board.addCar((5,8),2,1, 6)
        self.board.addCar((7,8),2,1, 4)

    def loadTestGame1(self):
        width = 6
        height = 6
        self.board = Board(width,height)
        self.board.setExitCoord((5,2))
        self.windowWidth = width * 50
        self.windowHeight = height * 50
        self.board.addCar((0,2),2,1, 0, True)
        self.board.addCar((4,2),2,0, 4)

    def loadTestGame2(self):
        width = 6
        height = 6
        self.board = Board(width,height)
        self.board.setExitCoord((5,2))
        self.windowWidth = width * 50
        self.windowHeight = height * 50
        self.board.addCar((0,2),2,1, 0, True)
        self.board.addCar((4,2),3,0, 2)
        self.board.addCar((3,5),2,1, 4)

if __name__ == '__main__':
    Game()