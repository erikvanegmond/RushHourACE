from board import *

def loadGame(num):
    if num == 1:
        return loadGame1()
    elif num == 2:
        return loadGame2()
    elif num == 3:
        return loadGame3()
    elif num == 4:
        return loadGame4()
    elif num == 5:
        return loadGame5()
    elif num == 6:
        return loadGame6()
    elif num == 7:
        return loadGame7()
    elif num == -1:
        return loadTestGame1()
    elif num == -2:
        return loadTestGame2()
    elif num == -3:
        return loadTestGame3()
    elif num == -4:
        return loadTestGame4()
    elif num == -5:
        return loadTestGame5()
    elif num == -6:
        return loadTestGame6()
    elif num == -7:
        return loadTestGame7()
    else:
        print 'no configuration'


def loadGame1():
    width = 6
    height = 6
    board = Board(width,height)
    board.setExitCoord((5,2))
    windowWidth = width * 50
    windowHeight = height * 50
    board.addCar((3,2),2,1, 0, True)
    board.addCar((2,0),3,0, 9)
    board.addCar((3,0),2,1, 7)
    board.addCar((5,0),3,0, 2)
    board.addCar((3,3),3,0, 1)
    board.addCar((4,3),2,1, 3)
    board.addCar((0,4),2,0, 1)
    board.addCar((1,4),2,1, 7)
    board.addCar((4,5),2,1, 5)
    return board


def loadGame2():
    width = 6
    height = 6
    board = Board(width,height)
    board.setExitCoord((5,2))
    windowWidth = width * 50
    windowHeight = height * 50
    board.addCar((2,2),2,1, 0, True)
    board.addCar((2,0),2,1, 8)
    board.addCar((4,0),2,1, 1)
    board.addCar((1,1),2,1, 1)
    board.addCar((3,1),2,1, 5)
    board.addCar((5,1),3,0, 2)
    board.addCar((4,2),2,0, 6)
    board.addCar((0,3),2,1, 5)
    board.addCar((2,3),2,1, 8)
    board.addCar((0,4),2,0, 1)
    board.addCar((3,4),2,0, 6)
    board.addCar((4,4),2,1, 5)
    board.addCar((4,5),2,1, 2)
    return board

def loadGame3():
    width = 6
    height = 6
    board = Board(width,height)
    board.setExitCoord((5,2))
    windowWidth = width * 50
    windowHeight = height * 50
    board.addCar((0,2),2,1, 0, True)
    board.addCar((1,0),2,1, 8)
    board.addCar((3,0),3,1, 2)
    board.addCar((1,1),2,1, 1)
    board.addCar((3,1),2,0, 8)
    board.addCar((4,1),2,1, 5)
    board.addCar((2,2),2,0, 6)
    board.addCar((5,2),2,0, 6)
    board.addCar((0,3),2,1, 5)
    board.addCar((3,3),2,1, 8)
    board.addCar((0,4),2,0, 1)
    board.addCar((2,4),2,0, 5)
    board.addCar((4,4),2,1, 5)
    return board

def loadGame4():
    width = 9
    height = 9
    board = Board(width,height)
    board.setExitCoord((8,4))
    windowWidth = width * 50
    windowHeight = height * 50
    board.addCar((1,4),2,1, 0, True)
    board.addCar((0,0),2,0, 5)
    board.addCar((1,0),3,1, 2)
    board.addCar((5,0),3,0, 11)
    board.addCar((3,1),3,0, 9)
    board.addCar((6,1),3,1, 9)
    board.addCar((8,2),3,0, 2)
    board.addCar((0,3),2,1, 7)
    board.addCar((5,3),3,1, 2)
    board.addCar((0,4),2,0, 3)
    board.addCar((3,4),2,0, 4)
    board.addCar((2,5),3,0, 2)
    board.addCar((5,5),3,1, 10)
    board.addCar((8,5),3,0, 2)
    board.addCar((0,6),2,1, 1)
    board.addCar((3,6),2,0, 8)
    board.addCar((4,6),2,1, 4)
    board.addCar((0,7),2,0, 8)
    board.addCar((4,7),2,0, 1)
    board.addCar((1,8),3,1, 11)
    board.addCar((5,8),2,1, 6)
    board.addCar((7,8),2,1, 4)
    return board

def loadGame5():
    width = 9
    height = 9
    board = Board(width,height)
    board.setExitCoord((8,4))
    windowWidth = width * 50
    windowHeight = height * 50
    board.addCar((6,4),2,1, 0, True)
    board.addCar((0,0),3,1, 2)
    board.addCar((3,0),3,0, 9)
    board.addCar((5,0),2,0, 5)
    board.addCar((6,0),2,0, 8)
    board.addCar((7,1),2,1, 5)
    board.addCar((4,2),2,1, 1)
    board.addCar((6,2),2,0, 6)
    board.addCar((4,3),2,1, 8)
    board.addCar((7,3),2,1, 1)
    board.addCar((2,4),3,1, 3)
    board.addCar((5,4),3,0, 9)
    board.addCar((8,4),3,0, 2)
    board.addCar((0,5),2,0, 8)
    board.addCar((2,5),2,0, 1)
    board.addCar((3,6),2,1, 5)
    board.addCar((6,6),2,1, 5)
    board.addCar((0,7),2,0, 7)
    board.addCar((1,7),2,0, 5)
    board.addCar((2,7),2,1, 8)
    board.addCar((4,7),2,0, 1)
    board.addCar((5,7),3,1, 10)
    board.addCar((8,7),2,0, 7)
    board.addCar((2,8),2,1, 7)
    return board

def loadGame6():
    width = 9
    height = 9
    board = Board(width,height)
    board.setExitCoord((8,4))
    windowWidth = width * 50
    windowHeight = height * 50
    board.addCar((0,4),2,1, 0, True)
    board.addCar((0,0),2,1, 8)
    board.addCar((2,0),2,1, 6)
    board.addCar((4,0),2,0, 5)
    board.addCar((7,0),2,0, 8)
    board.addCar((0,1),2,0, 6)
    board.addCar((1,1),3,1, 3)
    board.addCar((5,1),2,1, 1)
    board.addCar((2,2),2,1, 5)
    board.addCar((4,2),2,0, 1)
    board.addCar((5,2),2,0, 6)
    board.addCar((7,2),2,1, 5)
    board.addCar((2,3),2,0, 8)
    board.addCar((3,3),3,0, 2)
    board.addCar((6,3),3,1, 10)
    board.addCar((1,5),2,0, 1)
    board.addCar((4,5),2,1, 6)
    board.addCar((6,5),2,1, 1)
    board.addCar((8,5),3,0, 9)
    board.addCar((0,6),3,0, 9)
    board.addCar((2,6),2,1, 5)
    board.addCar((4,6),3,0, 10)
    board.addCar((5,6),3,1, 2)
    board.addCar((2,7),2,1, 8)
    board.addCar((5,7),2,1, 5)
    board.addCar((1,8),3,1, 3)
    return board

def loadGame7():
    width = 12
    height = 12
    board = Board(width,height)
    board.setExitCoord((11,5))
    windowWidth = width * 50
    windowHeight = height * 50
    board.addCar((2,5),2,1, 0, True)
    board.addCar((0,0),2,0, 5)
    board.addCar((6,0),2,0, 8)
    board.addCar((7,0),3,1, 9)
    board.addCar((10,0),2,1, 6)
    board.addCar((5,1),2,0, 6)
    board.addCar((10,1),2,0, 1)
    board.addCar((11,1),2,0, 8)
    board.addCar((0,2),3,1, 2)
    board.addCar((3,2),2,1, 1)
    board.addCar((6,2),3,0, 3)
    board.addCar((7,2),2,1, 5)
    board.addCar((0,3),3,0, 9)
    board.addCar((1,3),3,0, 3)
    board.addCar((5,3),2,0, 5)
    board.addCar((7,3),2,1, 1)
    board.addCar((9,3),2,1, 6)
    board.addCar((2,4),3,1, 10)
    board.addCar((7,4),3,1, 9)
    board.addCar((4,5),2,0, 1)
    board.addCar((5,5),2,0, 6)
    board.addCar((0,6),3,1, 10)
    board.addCar((3,6),2,0, 6)
    board.addCar((6,6),3,0, 2)
    board.addCar((7,6),2,0, 8)
    board.addCar((9,6),2,0, 6)
    board.addCar((10,6),2,1, 5)
    board.addCar((0,7),3,1, 2)
    board.addCar((4,7),2,1, 5)
    board.addCar((10,7),2,1, 8)
    board.addCar((0,8),2,1, 1)
    board.addCar((2,8),2,0, 5)
    board.addCar((3,8),3,1, 9)
    board.addCar((7,8),3,1, 3)
    board.addCar((11,8),2,0, 5)
    board.addCar((3,9),3,1, 2)
    board.addCar((6,9),3,0, 10)
    board.addCar((8,9),2,1, 5)
    board.addCar((10,9),3,0, 9)
    board.addCar((9,10),2,0, 6)
    board.addCar((11,10),2,0, 6)
    board.addCar((1,11),2,1, 5)
    board.addCar((3,11),3,1, 3)
    board.addCar((7,11),2,1, 8)
    return board

def loadTestGame1():
    width = 6
    height = 6
    board = Board(width,height)
    board.setExitCoord((5,2))
    windowWidth = width * 50
    windowHeight = height * 50
    board.addCar((0,2),2,1, 0, True)
    board.addCar((4,2),2,0, 4)
    return board

def loadTestGame2():
    width = 6
    height = 6
    board = Board(width,height)
    board.setExitCoord((5,2))
    windowWidth = width * 50
    windowHeight = height * 50
    board.addCar((0,2),2,1, 0, True)
    board.addCar((4,2),3,0, 2)
    board.addCar((3,5),2,1, 4)
    return board

def loadTestGame3():
    width = 6
    height = 6
    board = Board(width,height)
    board.setExitCoord((5,2))
    windowWidth = width * 50
    windowHeight = height * 50
    board.addCar((0,2),2,1, 0, True)
    board.addCar((5,0),3,0, 2)
    board.addCar((4,5),2,1, 2)
    return board

def loadTestGame4():
    width = 6
    height = 6
    board = Board(width,height)
    board.setExitCoord((5,2))
    windowWidth = width * 50
    windowHeight = height * 50
    board.addCar((0,2),2,1, 0, True)
    board.addCar((2,0),3,0, 1)
    board.addCar((4,0),2,1, 2)
    board.addCar((0,3),3,1, 3)
    board.addCar((5,3),3,0, 4)
    return board
    # playPath = [(5, -1), (4, 1), (4, -1), (5, -1), (5, 1), (4, 1), (3, -1), (3, 1), (5, 1), (5, -1), (3, -1), (5, 1), (4, -1), (3, 1), (5, -1), (4, 1), (3, -1), (5, -1), (4, -1), (5, -1), (5, 1), (3, 1), (4, 1), (5, 1), (4, 1), (3, -1), (5, 1), (5, -1), (5, -1), (3, 1), (5, 1), (5, -1), (3, -1), (5, -1), (5, 1), (4, -1), (3, 1), (3, -1), (3, 1), (3, -1), (3, 1), (5, 1), (4, 1), (3, -1), (3, 1), (3, -1), (5, -1), (5, 1), (3, 1), (4, -1), (4, -1), (5, -1), (4, 1), (4, 1), (3, -1), (5, 1), (5, -1), (5, -1), (5, 1), (5, 1), (3, 1), (3, -1), (4, -1), (5, -1), (5, -1), (5, 1), (4, 1), (5, -1), (4, 1), (4, -1), (5, 1), (4, -1), (4, 1), (5, 1), (4, -1), (5, 1), (5, -1), (4, -1), (3, 1), (4, 1), (5, -1), (4, -1), (3, -1), (3, 1), (4, 1), (5, 1), (4, -1), (4, 1), (5, 1), (4, -1), (5, -1), (3, -1), (3, 1), (5, -1), (3, -1), (4, 1), (4, 1), (5, -1), (5, 1), (5, -1), (5, 1), (3, 1), (3, -1), (4, -1), (4, -1), (5, -1), (5, 1), (4, 1), (4, -1), (4, 1), (3, 1), (4, -1), (3, -1), (5, 1), (5, 1), (5, -1), (5, 1), (3, 1), (4, 1), (4, -1), (3, -1), (5, -1), (4, 1), (5, -1), (3, 1), (4, -1), (5, 1), (5, 1), (4, 1), (4, -1), (4, 1), (4, 1), (5, -1), (3, -1), (3, 1), (5, -1), (5, 1), (4, -1), (5, -1), (4, 1), (5, 1), (4, -1), (5, 1), (4, -1), (4, 1), (4, -1), (4, 1), (4, -1), (3, -1), (4, 1), (3, 1), (4, -1), (5, -1), (5, 1), (4, 1), (5, -1), (5, 1), (5, -1), (4, 1), (5, -1), (3, -1), (5, -1), (4, -1), (4, -1), (5, 1), (3, 1), (3, -1), (3, 1), (4, 1), (4, 1), (3, -1), (5, -1), (5, 1), (4, -1), (4, -1), (3, 1), (3, -1), (3, 1), (3, -1), (3, 1), (3, -1), (4, 1), (5, 1), (4, -1), (4, 1), (5, -1), (4, -1), (5, 1), (4, 1), (4, 1), (5, -1), (3, 1), (5, 1), (3, -1), (3, 1), (4, -1), (5, 1), (4, -1), (3, -1), (4, 1), (5, -1), (5, -1), (5, 1), (5, -1), (3, 1), (5, 1), (5, -1), (4, -1), (3, -1), (3, 1), (3, -1), (4, 1), (5, 1), (4, 1), (3, 1), (5, 1), (5, -1), (5, -1), (4, -1), (4, 1), (3, -1), (4, -1), (3, 1), (3, -1), (4, 1), (3, 1), (3, -1), (5, -1), (4, 1), (2, 1), (3, -1), (3, -1), (2, 1), (3, 1), (2, 1), (2, -1), (2, 1), (1, 1), (3, 1), (3, -1), (1, 1), (3, -1), (3, -1), (3, 1), (1, 1), (2, -1), (3, -1), (3, 1), (3, 1), (3, -1), (3, 1), (3, 1), (2, -1), (2, -1), (4, -1), (5, 1), (4, -1), (4, -1), (5, 1), (5, 1), (5, -1), (5, 1), (5, -1), (5, 1), (1, 1)]

def loadTestGame5():
    width = 4
    height = 4
    board = Board(width,height)
    board.path = deque()
    board.setExitCoord((3,1))
    windowWidth = width * 50
    windowHeight = height * 50
    board.addCar((0,1),2,1, 0, True)
    board.addCar((3,0),2,0, 4)
    return board
    # playPath = [(1, 1), (2, 1), (2, 1), (2, -1), (2, -1), (1, 1), (2, 1), (1, -1), (2, 1), (1, 1)]
    # playPath = [(1, 1), (1, 1), (1, -1), (2, 1), (1, 1), (2, -1), (1, -1), (1, 1), (2, 1), (2, 1), (1, -1), (1, 1), (1, -1), (1, 1)]
    # playPath = playPath[::-1]

def loadTestGame6():
    width = 6
    height = 6
    board = Board(width,height)
    board.setExitCoord((5,2))
    windowWidth = width * 50
    windowHeight = height * 50
    board.addCar((2,2),2,1, 0, True)
    board.addCar((4,0),3,0, 1)
    board.addCar((3,3),2,0, 2)
    board.addCar((4,4),2,1, 3)
    return board

def loadTestGame7():
    width = 6
    height = 6
    board = Board(width,height)
    board.setExitCoord((5,2))
    windowWidth = width * 50
    windowHeight = height * 50
    board.addCar((0,2),2,1, 0, True)
    board.addCar((0,0),2,0, 1)
    board.addCar((5,0),3,0, 2)
    board.addCar((4,3),2,1, 3)
    board.addCar((2,3),2,0, 4)
    board.addCar((3,5),3,1, 5)
    return board

