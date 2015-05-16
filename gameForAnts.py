from board import *
import random
from configurations import *
import argparse
import time
import statisticsLogger as sl
import networkx as nx
import matplotlib.pyplot as plt
import threading

class Game(object):

    stateSpace = nx.Graph()

    moveCounter = 0

    winState = False

    startNode = []

    winNodes = set()

    """docstring for Game"""
    def __init__(self):
        parser = argparse.ArgumentParser(description='Solve Rush Hour')

        parser.add_argument('--game', type=int, choices =[1, 2, 3, 4, 5, 6, 7, -1, -2, -3, -4, -5], default = '3',
                    help='load a game from 1 to 7, test game form -1, -2 or -3')

        args = parser.parse_args()

        argdict = vars(args) # converts namespace with all arguments to a dictionary

        self.configuration = argdict.get('game')

        self.startGame()


    def startGame(self):
        print "starting game", self.configuration


        threads = []
        for i in range(10):
            t = threading.Thread(target=self.ant, args=(i,))
            threads.append(t)
            t.start()

        print "Waiting..."
        for t in threads:
            t.join()
        print "Waiting done"

        # nx.draw(self.stateSpace)
        myBoard = loadGame(self.configuration).toString()
        pos=nx.graphviz_layout(self.stateSpace,prog='neato')
        nx.draw(self.stateSpace,pos=pos,node_size=20)
        nx.draw_networkx_nodes(self.stateSpace,pos,
                       nodelist=[myBoard],
                       node_color='g',
                       node_size=100)
        nx.draw_networkx_nodes(self.stateSpace,pos,
                       nodelist=list(self.winNodes),
                       node_color='b',
                       node_size=100)

        # A = nx.to_agraph(self.stateSpace)
        # A.layout(prog='neato', color='red')
        # A.draw('color.png')

        plt.show()

    def ant(self, antNumber):
        myBoard = loadGame(self.configuration)

        myBoard.setCarsMovable()


        while True:
            self.randomMove(myBoard)

            if myBoard.checkForWin():
                self.winState = True
                self.winNodes.add(myBoard.toString())
                print "ant", antNumber, "found the food!"
                return


    def randomMove(self, myBoard):
        movableCars = []
        for car in myBoard.getCars():
            if car.getCanMove():
                movableCars.append( car )
        moved = False
        while not moved:
            car = random.choice(movableCars)
            direction = 1 if random.randint(0,1) else -1
            if car.getCanMove() and ((direction == -1 and myBoard.carCanMoveBackward(car)) or (direction == 1 and myBoard.carCanMoveForward(car))):
                carID = car.getCarID()
                board1String = myBoard.toString()
                myBoard.moveCarByID(carID, direction)
                myBoard.setCarsMovable()
                board2String = myBoard.toString()
                self.stateSpace.add_node(board1String)
                self.stateSpace.add_node(board2String)
                self.stateSpace.add_edge(board1String, board2String)
                moved = True
                self.moveCounter += 1

if __name__ == '__main__':
    Game()

