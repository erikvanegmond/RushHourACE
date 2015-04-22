import pygame, sys
from board import *
import screen as sc
from pygame.locals import *
import random
from Queue import *
import copy
from configurations import *

class Game(object):

    board = None
    screen = None

    windowWidth = 300
    windowHeight = 300

    winState = False

    visitedStates = set()
    statesToVisit = Queue()

    priorityQueue = PriorityQueue()

    chosenMoves = []

    solveMethod = "astar" # random,  breadthfirst, astar

    moveCounter = 0

    """docstring for Game"""
    def __init__(self):
        pygame.init()

        loadGame3()
        self.board.setCarsMovable()

        print self.board.printGrid()
        print self.board.checkPossibleMoves()

        if self.solveMethod is "breadthfirst":
            self.statesToVisit.put(self.board)
        if self.solveMethod is "astar":
            self.priorityQueue.put((self.board.getFCost(),self.board))

        self.screen = sc.Screen(self.windowWidth, self.windowHeight)

        self.last = pygame.time.get_ticks()
        self.msPerStep = 0#100000

        self.runGame()


    def runGame(self):

        while not self.winState:
            mouseClicked = False
            mouseMove = False

            for event in pygame.event.get():
                # Event that should close the game.
                if event.type == QUIT \
                     or (event.type == KEYUP and event.key == K_ESCAPE):
                    self.quitGame()
                 # A click event, recognize a click when the button is released.
                elif event.type == MOUSEBUTTONUP:
                    mouseX, mouseY = event.pos
                    mouseCoords = []
                    mouseClicked = True
                    mouseDown = False

                # Start drag event, start drag when mouse button is pressed.
                elif event.type == MOUSEBUTTONDOWN:
                    mouseX, mouseY = event.pos
                    mouseCoords = [mouseX, mouseY]
                    mouseDown = True


            now = pygame.time.get_ticks()
            self.screen.drawScreen(self.board)
            if now - self.last >= self.msPerStep or mouseClicked:
                self.last = now

                if self.solveMethod == "random":
                    self.randomMove()
                elif self.solveMethod == "breadthfirst":
                    if self.breadthfirstMove() == -1:
                        message = "Draw"
                        self.winState = True
                elif self.solveMethod == "astar":
                    self.aStarMove()
                else:
                    self.randomMove()

                if self.board.checkForWin():
                    message = "Game Won"
                    self.winState = True
                    print self.board.path
                    print "Number of moves:", len(self.board.path)

                # Update the screen
            pygame.display.update()

        while True:
            for event in pygame.event.get():
                    # Event that should close the game.
                    if event.type == QUIT \
                         or (event.type == KEYUP and event.key == K_ESCAPE):
                        self.quitGame()
            self.screen.drawScreen(self.board)
            self.screen.drawMessage(message)
            pygame.display.update()


    def randomMove(self):
        movableCars = []
        for car in self.board.getCars():
            if car.getCanMove():
                movableCars.append( car )
        moved = False
        while not moved:
            car = movableCars[random.randint(0,len(movableCars)-1)]
            direction = 1 if random.random()>0.5 else -1
            if car.getCanMove() and ((direction == -1 and self.board.carCanMoveBackward(car)) or (direction == 1 and self.board.carCanMoveForward(car))):
                carID = car.getCarID()
                self.board.moveCarByID(carID, direction)

                self.board.setCarsMovable()
                moved = True
                self.moveCounter += 1
                print self.moveCounter

    def breadthfirstMove(self):
        if self.statesToVisit.empty():
            print "no more possibleMoves"
            return -1
        self.board = self.statesToVisit.get()
        if self.board.toString() in self.visitedStates:
            return
        self.visitedStates.add(self.board.toString())
        possibleMoves = self.board.checkPossibleMoves()
        for move in possibleMoves:
            newBoard = self.board.copy()
            newBoard.moveCarByID(move[0],move[1])
            newBoard.setCarsMovable()
            if not newBoard.toString() in self.visitedStates:
                self.statesToVisit.put(newBoard)
                self.moveCounter += 1
                print self.moveCounter
            else:
                continue

    def aStarMove(self):
        if self.priorityQueue.empty():
            print "no possible moves"
            return

        newState = self.priorityQueue.get()
        self.board = newState[1]

        if self.board.toString() in self.visitedStates:
            print 'skip state'
            return

        self.visitedStates.add(self.board.toString())

        possibleMoves = self.board.checkPossibleMoves()

        for move in possibleMoves:
            newBoard = self.board.copy()
            newBoard.moveCarByID(move[0],move[1])
            newBoard.gCost = self.board.getGCost() + move[1]
            newBoard.setCarsMovable()

            if not newBoard.toString() in self.visitedStates:
                self.priorityQueue.put((newBoard.getFCost(), newBoard))
                self.moveCounter += 1
                print self.moveCounter
            else:
                continue

            if newBoard.checkForWin():
                self.board = newBoard
                return



    # Quit the game
    def quitGame(self):
        pygame.quit()
        sys.exit()

    def checkVisitedStates(self, state):
        return state in self.visitedStates

    def addVisitedStates(self, state):
        self.visitedStates.add(state)



if __name__ == '__main__':
    Game()