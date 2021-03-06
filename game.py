try:
    import pygame
    import screen as sc
    from pygame.locals import *
except ImportError:
    pass

try:
    import networkx as nx
    import matplotlib.pyplot as plt
except ImportError:
    pass

import sys
from board import *
import random
from Queue import *
import copy
from configurations import *
import argparse
import time
import statisticsLogger as sl

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

    playPath = list()

    randomStates = list()

    randomStatesIndex = list()

    moveCounter = 0

    startTime = 0

    LIMIT = 50

    stats = None

    stateSpace = None
    startNode = []
    winNodes = set()


    def __init__(self):
        parser = argparse.ArgumentParser(description='Solve Rush Hour')

        parser.add_argument('--alg', type=str, choices =['random', 'breadthfirst', 'astar', 'depthfirst'], default = 'astar',
            help='random, breadthfirst, astar, or depthfirst')

        parser.add_argument('--game', type=int, default = '3',
            help='load a game from 1 to 7, test game form -1, -2, -3, -4, -5 or -6')

        parser.add_argument('-visual', "--visual", action='store_true', default=False,
                    dest='visual',
                    help='If argument is present visualization will be shown')

        parser.add_argument('-showSolution', "--showSolution", action='store_true', default=False,
                    dest='showSolution',
                    help='If argument is present solution will be shown')

        parser.add_argument('-showEverything', "--showEverything", action='store_false', default=True,
                    dest='showEverything',
                    help='No ouput exept for statistics')

        parser.add_argument('-gatherStatistics', "--gatherStatistics", action='store_true', default=False,
                    dest='gatherStatistics',
                    help='Store statistics in a csv file')

        parser.add_argument('-storePath', "--storePath", action='store_true', default=False,
                    dest='storePath',
                    help='Store path in a text file')

        parser.add_argument('-drawStateSpace', "--drawStateSpace", action='store_true', default=False,
                    dest='drawStateSpace',
                    help='Draw the state space that is explored')

        parser.add_argument('-exploreAll', "--exploreAll", action='store_true', default=False,
                    dest='exploreAll',
                    help='Explore the entire statespace until all states are visited')

        parser.add_argument('-onlySmallSteps', "--onlySmallSteps", action='store_true', default=False,
                    dest='onlySmallSteps',
                    help='Allow only for moves that are one tile')

        args = parser.parse_args()

        argdict = vars(args) # converts namespace with all arguments to a dictionary

        self.solveMethod = argdict.get('alg')
        self.configuration = argdict.get('game')
        self.visualize = argdict.get('visual')
        self.showSolution = argdict.get('showSolution')
        self.onlyStatistics = argdict.get('showEverything')
        self.gatherStatistics = argdict.get('gatherStatistics')
        self.storePath = argdict.get('storePath')
        self.drawStateSpace = argdict.get('drawStateSpace')
        self.exploreAll = argdict.get('exploreAll')
        self.onlySmallSteps = argdict.get('onlySmallSteps')

        self.startGame()


    def startGame(self):
        self.board = loadGame(self.configuration)
        if self.drawStateSpace:
            self.stateSpace = nx.Graph()
            self.startNode.append(self.board.toString())

        if self.onlySmallSteps:
            self.board.smallSteps = True

        if len(self.playPath):
            self.solveMethod = "path"
            # print self.playPath
            # self.playPath = self.compressRandomMove(self.playPath)
            # print self.playPath


        self.board.setCarsMovable()

        if not self.onlyStatistics:
            print self.board.printGrid()
            print self.board.checkPossibleMoves()

        if self.solveMethod == "breadthfirst":
            self.statesToVisit.put(self.board)
            if self.gatherStatistics:
                self.stats = sl.StatisticsLogger(self.configuration, self.solveMethod, ["iterations", "time","visited boards","open set", "closed set", "shortestPath", "longestPath"])
        if self.solveMethod == "astar":
            self.priorityQueue.put((self.board.getFCost(),self.board))
            if self.gatherStatistics:
                self.stats = sl.StatisticsLogger(self.configuration, self.solveMethod, ["iterations", "time","visited boards","open set", "closed set", "shortestPath", "longestPath"])
        if self.solveMethod == "random":
            self.randomStates.append(self.board.toString())

        if self.visualize:
            pygame.init()

            self.screen = sc.Screen(self.windowWidth, self.windowHeight)

            self.last = pygame.time.get_ticks()
            self.msPerStep = 60000

            self.startTime = time.time()

            self.runGame()

        elif not self.visualize or self.onlyStatistics:
            self.startTime = time.time()
            if self.solveMethod == 'depthfirst':
                sys.setrecursionlimit(self.LIMIT + 50)
                self.depthFirstMove(self.board, 0)
            else:
                self.runWithoutVisual()

    def runGame(self):
        print len(self.playPath)
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
                    if self.aStarMove()  == -1:
                        message = "Draw"
                        self.winState = True
                elif self.solveMethod == "path":
                    self.pathMove()
                else:
                    self.randomMove()

                if self.board.checkForWin():
                    message = "Game Won"
                    self.winState = True
                    self.printStatistics()


            # Update the screen
            pygame.display.update()

        # if self.solveMethod == "random":
            # path = self.compressRandomMove(self.board.path)
            # print len(self.board.path),"--",len(path)
            # self.visualizeSolution(path)
            # print self.randomStatesIndex

        if self.showSolution:
            self.visualizeSolution(self.board.path)

        while True:
            for event in pygame.event.get():
                # Event that should close the game.
                if event.type == QUIT \
                    or (event.type == KEYUP and event.key == K_ESCAPE):
                    self.quitGame()
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

            self.screen.drawScreen(self.board)
            self.screen.drawMessage(message)
            pygame.display.update()
            if mouseClicked:
                self.visualizeSolution(self.board.path)

    def runWithoutVisual(self):
        if self.gatherStatistics:
            iterationCounter = 0

        while not self.winState:
            if self.solveMethod == "random":
                    self.randomMove()
            elif self.solveMethod == "breadthfirst":
                if self.breadthfirstMove() == -1:
                    message = "Draw"
                    self.winState = True
            elif self.solveMethod == "astar":
                if self.aStarMove()  == -1:
                    message = "Draw"
                    self.winState = True
            else:
                self.randomMove()
            if not self.onlyStatistics:
                self.board.printGrid()

            if self.gatherStatistics:
                iterationCounter += 1
                longestPath = 0
                shortestPath = 1000000
                if self.solveMethod == "astar":
                    for board in list(self.priorityQueue.queue):
                        l = len(board[1].path)
                        if l<shortestPath:
                            shortestPath = l
                        if l>longestPath:
                            longestPath = l
                    timePassed = time.time() - self.startTime
                    self.stats.log([iterationCounter, timePassed, self.moveCounter, self.priorityQueue.qsize(), len(self.visitedDict), shortestPath, longestPath])
                elif self.solveMethod =="breadthfirst":
                    for board in list(self.statesToVisit.queue):
                        l = len(board.path)
                        if l<shortestPath:
                            shortestPath = l
                        if l>longestPath:
                            longestPath = l
                    self.stats.log([iterationCounter, time.time()-self.startTime, self.moveCounter, self.statesToVisit.qsize(), len(self.visitedStates), shortestPath, longestPath])


            if self.board.checkForWin():
                self.winNodes.add(self.board.toString())

                if not self.exploreAll:
                    self.printStatistics()

                    self.winState = True


        if self.storePath:
            fname = "pathGame%s-%s.csv" %(str(self.configuration), str(self.solveMethod))
            f = open(fname, 'a')
            f.write(str(len(list(self.board.path)))+", "+str(list(self.board.path))+"\n")

        if self.drawStateSpace:
            print "drawing the state space"
            pos=nx.graphviz_layout(self.stateSpace,prog='neato')
            nx.draw(self.stateSpace,pos=pos,node_size=20)
            nx.draw_networkx_nodes(self.stateSpace,pos,
                           nodelist=self.startNode,
                           node_color='g',
                           node_size=100)
            nx.draw_networkx_nodes(self.stateSpace,pos,
                           nodelist=list(self.winNodes),
                           node_color='b',
                           node_size=100)

            plt.show()

        if self.solveMethod == "random":
            if self.gatherStatistics:
                fname = "statisticsGame%s-%s.csv" %(str(self.configuration), str(self.solveMethod))
                f = open(fname, 'a')
                f.write(str( time.time() - self.startTime)+","+str(len(self.board.path))+"\n")
            # print 'index list', len(self.randomStatesIndex)
            # print 'states:', len(self.randomStates)

            # lengthOldPath = len(self.board.path)

            # # newPath = self.compressRandomPath(self.randomStatesIndex, self.randomStates, self.board.path)
            # newPath = self.compressPathWithAStar(self.board.path)
            # # print 'compressed:', newPath
            # print 'old vs new length:', lengthOldPath, 'vs', len(newPath)

            # self.printSolution(newPath, True)

    def visualizeSolution(self, path):
        # print "called function"
        self.board = loadGame(self.configuration)
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
            time.sleep(0.5)
            pygame.display.update()
            self.screen.drawScreen(self.board)

        # while True:
        #     for event in pygame.event.get():
        #             # Event that should close the game.
        #             if event.type == QUIT \
        #                  or (event.type == KEYUP and event.key == K_ESCAPE):
        #                 self.quitGame()
        #     self.screen.drawScreen(self.board)
        #     pygame.display.update()

    def printSolution(self, path, orientation):

        self.board = loadGame(self.configuration)
        self.board.setCarsMovable()

        if not orientation:
            pathList = list()

            while len(path) != 0:
                pathList.append(path.pop())
        else:
            pathList = path

        print "Start:"
        self.board.printGrid()

        for move in pathList:
            carID = move[0]
            distance = move[1]
            self.board.moveCarByID(carID, distance)
            print "Move:", move
            self.board.printGrid()

    def compressRandomPath(self, loops, states, path):

        pathList = list()

        while len(path) != 0:
            pathList.append(path.pop())

        biggestLoopSize = 0
        biggestLoop = ()
        for loop in loops:
            loopSize = loop[1] - loop[0]

            if loopSize > biggestLoopSize:
                biggestLoop = loop
                biggestLoopSize = loopSize

        print "biggest:", biggestLoop

        # print "path:", pathList

        if biggestLoop:
            del pathList[biggestLoop[0]:biggestLoop[1]]
            del states[biggestLoop[0]:biggestLoop[1]]

        return pathList

    def compressRandomMove(self, path):
        print "compressing!", path

        self.board = loadGame(self.configuration)
        self.board.setCarsMovable()

        pathList = list()

        boardList = list()

        while len(path) != 0:
            pathList.append(path.pop())

        for move in pathList:
            carID = move[0]
            distance = move[1]
            self.board.moveCarByID(carID, distance)

            boardList.append(self.board.toString())

        frontList = list()
        backList = list()



        for i in range(0, len(boardList)/2):
            if not boardList[i] in backList:
                frontList.append(boardList[i])
            else:
                backIndex = backList.index(boardList[i])
                if backIndex:
                    # shortboardList = boardList[:i+1] + boardList[-backIndex:]
                    shortPathList = pathList[:i] + pathList[-backIndex:]
                break

            if i and  not boardList[-i] in frontList:
                backList.append(boardList[-i])
            elif not i:
                continue
            else:
                frontIndex = frontList.index(boardList[-i])

                if frontIndex:
                    # shortboardList = boardList[:frontIndex+1] + boardList[-i-1:]
                    shortPathList = pathList[:frontIndex] + pathList[-i:]
                else:
                    # shortboardList = boardList[-i:]
                    shortPathList = pathList[-i:]

                break

        print "result:",shortPathList
        self.board = loadGame(self.configuration)

        return shortPathList

    def compressPathWithAStar(self, path):
        pathList = list()

        while len(path) != 0:
            pathList.append(path.pop())

        # pathList = pathList[::-1]

        self.board = loadGame(self.configuration)

        statesGraph = dict() #{"stateString": ["newStateString1","newStateString2",...]}

        currentState = self.board.toString()

        for move in pathList:
            self.board.moveCarByID(move[0],move[1])
            newState = self.board.toString()
            if currentState in statesGraph:
                statesGraph[currentState].add(newState)
            else:
                statesGraph[currentState] = set([newState])

            if newState in statesGraph:
                statesGraph[newState].add(currentState)
            else:
                statesGraph[newState] = set([currentState])

            currentState = newState

        return self.aStarWithStatesGraph(statesGraph)

    def printStatistics(self):
        print "Played game nr:", self.configuration
        print "Solved using:", self.solveMethod
        print "Path lenght to goal:", len(self.board.path)
        print "Number of visited states:", self.moveCounter
        print "Time taken: %f seconds" % ( time.time() - self.startTime)

    def randomMove(self):
        movableCars = []
        for car in self.board.getCars():
            if car.getCanMove():
                movableCars.append( car )
        moved = False
        while not moved:
            car = random.choice(movableCars)
            direction = 1 if random.randint(0,1) else -1
            if car.getCanMove() and ((direction == -1 and self.board.carCanMoveBackward(car)) or (direction == 1 and self.board.carCanMoveForward(car))):
                carID = car.getCarID()
                self.board.moveCarByID(carID, direction)

                self.board.setCarsMovable()
                moved = True
                self.moveCounter += 1
                # print self.moveCounter
                # boardString = self.board.toString()
                # if boardString in self.randomStates:
                #     for index, state in enumerate(self.randomStates):
                #         if boardString == state:
                #             self.randomStatesIndex.append((index, len(self.randomStates)))
                #             continue

                # self.randomStates.append(boardString)


    def breadthfirstMove(self):
        if self.statesToVisit.empty():
            print "Could not find a solution, no more possibleMoves"
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
            else:
                continue

            if self.drawStateSpace:
                board1String = self.board.toString()
                board2String = newBoard.toString()
                self.stateSpace.add_node(board1String)
                self.stateSpace.add_node(board2String)
                self.stateSpace.add_edge(board1String, board2String)

    def aStarMove(self):

        if self.priorityQueue.empty():
            print "Could not find a solution, no more possibleMoves"
            return -1


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

            if self.drawStateSpace:
                board1String = self.board.toString()
                board2String = newBoard.toString()
                self.stateSpace.add_node(board1String)
                self.stateSpace.add_node(board2String)
                self.stateSpace.add_edge(board1String, board2String)

            if newBoard.checkForWin():
                self.board = newBoard
                return

    # vindt wel paden, maar niet de kortste
    def depthFirstMove(self, board, depth):
        print "Depth:", depth
        self.visitedStates.add(board.toString())

        if depth < self.LIMIT:
            if board.checkForWin():
                print board.path
                print len(board.path)

            possibleMoves = board.checkPossibleMoves()
            neighbors = list()

            for move in possibleMoves:
                newBoard = board.copy()
                newBoard.moveCarByID(move[0], move[1])
                newBoard.setCarsMovable()
                neighbors.append((newBoard, move))

            for state in neighbors:
                if state[0].toString() not in self.visitedStates:
                    # print possibleMoves
                    # print "Move:", state[1]
                    # state[0].printGrid()
                    self.depthFirstMove(state[0], depth+1)

    def aStarWithStatesGraph(self,statesGraph):
        self.board = loadGame(self.configuration)
        self.priorityQueue.put((self.board.getFCost(),self.board))
        # currentState = self.board.toString()

        while True:
            currentState = self.priorityQueue.get()
            self.board = currentState[1]

            possibleStates = list(statesGraph[self.board.toString()])

            # print "compressing with A*"
            for state in possibleStates:
                move = self.board.getMoveToNewState(state)

            # for move in possibleMoves:
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
                    print self.board.path
                    return self.board.path

        # print 'qlen', self.priorityQueue.qsize()

    def pathMove(self):
        print self.playPath
        if len(self.playPath):
            move = self.playPath[0]
            print move
            self.board.moveCarByID(move[0], move[1])
            del self.playPath[0]
            self.moveCounter += 1
            print self.moveCounter


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
