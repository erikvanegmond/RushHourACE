from board import *

def loadGame(game, num):
    if num == 1:
        loadGame1(game)
    elif num == 2:
        loadGame2(game)
    elif num == 3:
        loadGame3(game)
    elif num == 4:
        loadGame4(game)
    elif num == 5:
        loadGame5(game)
    elif num == 6:
        loadGame6(game)
    elif num == 7:
        loadGame7(game)
    elif num == -1:
        loadTestGame1(game)
    elif num == -2:
        loadTestGame2(game)
    elif num == -3:
        loadTestGame3(game)
    else:
        print 'no configuration'


def loadGame1(game):
    width = 6
    height = 6
    game.board = Board(width,height)
    game.board.setExitCoord((5,2))
    game.windowWidth = width * 50
    game.windowHeight = height * 50
    game.board.addCar((3,2),2,1, 0, True)
    game.board.addCar((2,0),3,0, 9)
    game.board.addCar((3,0),2,1, 7)
    game.board.addCar((5,0),3,0, 2)
    game.board.addCar((3,3),3,0, 1)
    game.board.addCar((4,3),2,1, 3)
    game.board.addCar((0,4),2,0, 1)
    game.board.addCar((1,4),2,1, 7)
    game.board.addCar((4,5),2,1, 5)


def loadGame2(game):
    width = 6
    height = 6
    game.board = Board(width,height)
    game.board.setExitCoord((5,2))
    game.windowWidth = width * 50
    game.windowHeight = height * 50
    game.board.addCar((2,2),2,1, 0, True)
    game.board.addCar((2,0),2,1, 8)
    game.board.addCar((4,0),2,1, 1)
    game.board.addCar((1,1),2,1, 1)
    game.board.addCar((3,1),2,1, 5)
    game.board.addCar((5,1),3,0, 2)
    game.board.addCar((4,2),2,0, 6)
    game.board.addCar((0,3),2,1, 5)
    game.board.addCar((2,3),2,1, 8)
    game.board.addCar((0,4),2,0, 1)
    game.board.addCar((3,4),2,0, 6)
    game.board.addCar((4,4),2,1, 5)
    game.board.addCar((4,5),2,1, 2)

def loadGame3(game):
    width = 6
    height = 6
    game.board = Board(width,height)
    game.board.setExitCoord((5,2))
    game.windowWidth = width * 50
    game.windowHeight = height * 50
    game.board.addCar((0,2),2,1, 0, True)
    game.board.addCar((1,0),2,1, 8)
    game.board.addCar((3,0),3,1, 2)
    game.board.addCar((1,1),2,1, 1)
    game.board.addCar((3,1),2,0, 8)
    game.board.addCar((4,1),2,1, 5)
    game.board.addCar((2,2),2,0, 6)
    game.board.addCar((5,2),2,0, 6)
    game.board.addCar((0,3),2,1, 5)
    game.board.addCar((3,3),2,1, 8)
    game.board.addCar((0,4),2,0, 1)
    game.board.addCar((2,4),2,0, 5)
    game.board.addCar((4,4),2,1, 5)

def loadGame4(game):
    width = 9
    height = 9
    game.board = Board(width,height)
    game.board.setExitCoord((8,4))
    game.windowWidth = width * 50
    game.windowHeight = height * 50
    game.board.addCar((1,4),2,1, 0, True)
    game.board.addCar((0,0),2,0, 5)
    game.board.addCar((1,0),3,1, 2)
    game.board.addCar((5,0),3,0, 11)
    game.board.addCar((3,1),3,0, 9)
    game.board.addCar((6,1),3,1, 9)
    game.board.addCar((8,2),3,0, 2)
    game.board.addCar((0,3),2,1, 7)
    game.board.addCar((5,3),3,1, 2)
    game.board.addCar((0,4),2,0, 3)
    game.board.addCar((3,4),2,0, 4)
    game.board.addCar((2,5),3,0, 2)
    game.board.addCar((5,5),3,1, 10)
    game.board.addCar((8,5),3,0, 2)
    game.board.addCar((0,6),2,1, 1)
    game.board.addCar((3,6),2,0, 8)
    game.board.addCar((4,6),2,1, 4)
    game.board.addCar((0,7),2,0, 8)
    game.board.addCar((4,7),2,0, 1)
    game.board.addCar((1,8),3,1, 11)
    game.board.addCar((5,8),2,1, 6)
    game.board.addCar((7,8),2,1, 4)

def loadGame5(game):
    width = 9
    height = 9
    game.board = Board(width,height)
    game.board.setExitCoord((8,4))
    game.windowWidth = width * 50
    game.windowHeight = height * 50
    game.board.addCar((6,4),2,1, 0, True)
    game.board.addCar((0,0),3,1, 2)
    game.board.addCar((3,0),3,0, 9)
    game.board.addCar((5,0),2,0, 5)
    game.board.addCar((6,0),2,0, 8)
    game.board.addCar((7,1),2,1, 5)
    game.board.addCar((4,2),2,1, 1)
    game.board.addCar((6,2),2,0, 6)
    game.board.addCar((4,3),2,1, 8)
    game.board.addCar((7,3),2,1, 1)
    game.board.addCar((2,4),3,1, 3)
    game.board.addCar((5,4),3,0, 9)
    game.board.addCar((8,4),3,0, 2)
    game.board.addCar((0,5),2,0, 8)
    game.board.addCar((2,5),2,0, 1)
    game.board.addCar((3,6),2,1, 5)
    game.board.addCar((6,6),2,1, 5)
    game.board.addCar((0,7),2,0, 7)
    game.board.addCar((1,7),2,0, 5)
    game.board.addCar((2,7),2,1, 8)
    game.board.addCar((4,7),2,0, 1)
    game.board.addCar((5,7),3,1, 10)
    game.board.addCar((8,7),2,0, 7)
    game.board.addCar((2,8),2,1, 7)

def loadGame6(game):
    width = 9
    height = 9
    game.board = Board(width,height)
    game.board.setExitCoord((8,4))
    game.windowWidth = width * 50
    game.windowHeight = height * 50
    game.board.addCar((0,4),2,1, 0, True)
    game.board.addCar((0,0),2,1, 8)
    game.board.addCar((2,0),2,1, 6)
    game.board.addCar((4,0),2,0, 5)
    game.board.addCar((7,0),2,0, 8)
    game.board.addCar((0,1),2,0, 6)
    game.board.addCar((1,1),3,1, 3)
    game.board.addCar((5,1),2,1, 1)
    game.board.addCar((2,2),2,1, 5)
    game.board.addCar((4,2),2,0, 1)
    game.board.addCar((5,2),2,0, 6)
    game.board.addCar((7,2),2,1, 5)
    game.board.addCar((2,3),2,0, 8)
    game.board.addCar((3,3),3,0, 2)
    game.board.addCar((6,3),3,1, 10)
    game.board.addCar((1,5),2,0, 1)
    game.board.addCar((4,5),2,1, 6)
    game.board.addCar((6,5),2,1, 1)
    game.board.addCar((8,5),3,0, 9)
    game.board.addCar((0,6),3,0, 9)
    game.board.addCar((2,6),2,1, 5)
    game.board.addCar((4,6),3,0, 10)
    game.board.addCar((5,6),3,1, 2)
    game.board.addCar((2,7),2,1, 8)
    game.board.addCar((5,7),2,1, 5)
    game.board.addCar((1,8),3,1, 3)

def loadGame7(game):
    width = 12
    height = 12
    game.board = Board(width,height)
    game.board.setExitCoord((11,5))
    game.windowWidth = width * 50
    game.windowHeight = height * 50
    game.board.addCar((2,5),2,1, 0, True)
    game.board.addCar((0,0),2,0, 5)
    game.board.addCar((6,0),2,0, 8)
    game.board.addCar((7,0),3,1, 9)
    game.board.addCar((10,0),2,1, 6)
    game.board.addCar((5,1),2,0, 6)
    game.board.addCar((10,1),2,0, 1)
    game.board.addCar((11,1),2,0, 8)
    game.board.addCar((0,2),3,1, 2)
    game.board.addCar((3,2),2,1, 1)
    game.board.addCar((6,2),3,0, 3)
    game.board.addCar((7,2),2,1, 5)
    game.board.addCar((0,3),3,0, 9)
    game.board.addCar((1,3),3,0, 3)
    game.board.addCar((5,3),2,0, 5)
    game.board.addCar((7,3),2,1, 1)
    game.board.addCar((9,3),2,1, 6)
    game.board.addCar((2,4),3,1, 10)
    game.board.addCar((7,4),3,1, 9)
    game.board.addCar((4,5),2,0, 1)
    game.board.addCar((5,5),2,0, 6)
    game.board.addCar((0,6),3,1, 10)
    game.board.addCar((3,6),2,0, 6)
    game.board.addCar((6,6),3,0, 2)
    game.board.addCar((7,6),2,0, 8)
    game.board.addCar((9,6),2,0, 6)
    game.board.addCar((10,6),2,1, 5)
    game.board.addCar((0,7),3,1, 2)
    game.board.addCar((4,7),2,1, 5)
    game.board.addCar((10,7),2,1, 8)
    game.board.addCar((0,8),2,1, 1)
    game.board.addCar((2,8),2,0, 5)
    game.board.addCar((3,8),3,1, 9)
    game.board.addCar((7,8),3,1, 3)
    game.board.addCar((11,8),2,0, 5)
    game.board.addCar((3,9),3,1, 2)
    game.board.addCar((6,9),3,0, 10)
    game.board.addCar((8,9),2,1, 5)
    game.board.addCar((10,9),3,0, 9)
    game.board.addCar((9,10),2,0, 6)
    game.board.addCar((11,10),2,0, 6)
    game.board.addCar((1,11),2,1, 5)
    game.board.addCar((3,11),3,1, 3)
    game.board.addCar((7,11),2,1, 8)

def loadTestGame1(game):
    width = 6
    height = 6
    game.board = Board(width,height)
    game.board.setExitCoord((5,2))
    game.windowWidth = width * 50
    game.windowHeight = height * 50
    game.board.addCar((0,2),2,1, 0, True)
    game.board.addCar((4,2),2,0, 4)

def loadTestGame2(game):
    width = 6
    height = 6
    game.board = Board(width,height)
    game.board.setExitCoord((5,2))
    game.windowWidth = width * 50
    game.windowHeight = height * 50
    game.board.addCar((0,2),2,1, 0, True)
    game.board.addCar((4,2),3,0, 2)
    game.board.addCar((3,5),2,1, 4)

def loadTestGame3(game):
    width = 6
    height = 6
    game.board = Board(width,height)
    game.board.setExitCoord((5,2))
    game.windowWidth = width * 50
    game.windowHeight = height * 50
    game.board.addCar((0,2),2,1, 0, True)
    game.board.addCar((5,0),3,0, 2)
    game.board.addCar((4,5),2,1, 2)


