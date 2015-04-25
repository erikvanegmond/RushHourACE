try:
    import pygame, sys
    import screen as sc
    from pygame.locals import *
except ImportError:
    print "Didn't import pygame"

from board import *
import random
from Queue import *
import copy
from configurations import *
import argparse
import time

class Game(object):

    board = None
    screen = None

    windowWidth = 300
    windowHeight = 300

    winState = False

    visitedStates = set()
    visitedDict = dict()
    statesToVisit = Queue()

    priorityQueue = PriorityQueue()

    moveCounter = 0

    startTime = 0

    """docstring for Game"""
    def __init__(self):
        parser = argparse.ArgumentParser(description='Solve Rush Hour')

        parser.add_argument('--alg', type=str, choices =['random', 'breadthfirst', 'astar'], default = 'astar', 
            help='random, breadthfirst or astar')

        parser.add_argument('--game', type=int, choices =[1, 2, 3, 4, 5, 6, 7, -1, -2, -3, -4], default = '3', 
            help='load a game from 1 to 7, test game form -1, -2 or -3')

        parser.add_argument('--visual', type = bool, default = 0, help = 'true or false for visualization')
        args = parser.parse_args()

        argdict = vars(args) # converts namespace with all arguments to a dictionary
      
        self.solveMethod = argdict.get('alg')
        self.configuration = argdict.get('game')
        self.visualize = argdict.get('visual')
        
        self.startGame()


    def startGame(self):
        
        loadGame(self, self.configuration)
        self.board.setCarsMovable()

        print self.board.printGrid()
        print self.board.checkPossibleMoves()

        if self.solveMethod == "breadthfirst":
            self.statesToVisit.put(self.board)
        if self.solveMethod == "astar":
            self.priorityQueue.put((self.board.getFCost(),self.board))

        if self.visualize:
            pygame.init()

            self.screen = sc.Screen(self.windowWidth, self.windowHeight)

            self.last = pygame.time.get_ticks()
            self.msPerStep = 0#100000

            self.startTime = pygame.time.get_ticks()

            self.runGame()
        else:
            self.runWithoutVisual()

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
                    print "Time taken: %f seconds" % ( float(float(pygame.time.get_ticks() - self.startTime) /float(1000) ))
                    
            # Update the screen
            pygame.display.update()

        self.visualizeSolution(self.board.path)

##        while True:
##            for event in pygame.event.get():
##                    # Event that should close the game.
##                    if event.type == QUIT \
##                         or (event.type == KEYUP and event.key == K_ESCAPE):
##                        self.quitGame()
##            self.screen.drawScreen(self.board)
##            self.screen.drawMessage(message)
##            pygame.display.update()

    def runWithoutVisual(self):

        while not self.winState:
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

            self.board.printGrid()

            if self.board.checkForWin():
                print "Game Won"
                print self.board.path
                print "Number of moves:", len(self.board.path)
                self.winState = True
                self.showSolution(self.board.path)

    def visualizeSolution(self, path):
        print "called function"
        loadGame(self, self.configuration)
        self.board.setCarsMovable()

        pathList = list()

        while len(path) != 0:
            pathList.append(path.pop())

        print pathList

        pygame.display.update()

        for move in pathList:
            carID = move[0]
            distance = move[1]
            
            self.screen.drawScreen(self.board)
            self.board.moveCarByID(carID, distance)
            time.sleep(1)
            pygame.display.update()
            self.screen.drawScreen(self.board)

        while True:
            for event in pygame.event.get():
                    # Event that should close the game.
                    if event.type == QUIT \
                         or (event.type == KEYUP and event.key == K_ESCAPE):
                        self.quitGame()
            self.screen.drawScreen(self.board)
            pygame.display.update()
            
    def showSolution(self, path):

        loadGame(self, self.configuration)
        self.board.setCarsMovable()

        pathList = list()

        while len(path) != 0:
            pathList.append(path.pop())

        print "Start:"
        self.board.printGrid()

        for move in pathList:
            carID = move[0]
            distance = move[1]
            self.board.moveCarByID(carID, distance)
            print "Move:", move
            self.board.printGrid()

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

        possibleMoves = self.board.checkPossibleMoves()

        for move in possibleMoves:
            newBoard = self.board.copy()
            newBoard.moveCarByID(move[0],move[1])
            newBoard.gCost = self.board.getGCost() + 1 # + move[1] 
            newBoard.setCarsMovable()

            if not (newBoard.toString() in self.visitedDict) or newBoard.getGCost() < self.visitedDict[newBoard.toString()]:
                self.priorityQueue.put((newBoard.getFCost(), newBoard))
                self.visitedDict[newBoard.toString()] = newBoard.getGCost()
                self.moveCounter += 1
                # print self.moveCounter
            else:
                continue

            if newBoard.checkForWin():
                self.board = newBoard
                return

        # print 'qlen', self.priorityQueue.qsize()

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
