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

    def loadGame3(self):
        width = 6
        height = 6
        self.board = Board(width,height)
        self.board.setExitCoord((5,2))
        self.windowWidth = width * 50
        self.windowHeight = height * 50
        self.board.addCar((0,2),2,1, 0, True)
        self.board.addCar((1,0),2,1, 8)
        self.board.addCar((3,0),3,1, 2)
        self.board.addCar((1,1),2,1, 1)
        self.board.addCar((3,1),2,0, 8)
        self.board.addCar((4,1),2,1, 5)
        self.board.addCar((2,2),2,0, 6)
        self.board.addCar((5,2),2,0, 6)
        self.board.addCar((0,3),2,1, 5)
        self.board.addCar((3,3),2,1, 8)
        self.board.addCar((0,4),2,0, 1)
        self.board.addCar((2,4),2,0, 5)
        self.board.addCar((4,4),2,1, 5)

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

    def loadGame5(self):
        width = 9
        height = 9
        self.board = Board(width,height)
        self.board.setExitCoord((8,4))
        self.windowWidth = width * 50
        self.windowHeight = height * 50
        self.board.addCar((6,4),2,1, 0, True)
        self.board.addCar((0,0),3,1, 2)
        self.board.addCar((3,0),3,0, 9)
        self.board.addCar((5,0),2,0, 5)
        self.board.addCar((6,0),2,0, 8)
        self.board.addCar((7,1),2,1, 5)
        self.board.addCar((4,2),2,1, 1)
        self.board.addCar((6,2),2,0, 6)
        self.board.addCar((4,3),2,1, 8)
        self.board.addCar((7,3),2,1, 1)
        self.board.addCar((2,4),3,1, 3)
        self.board.addCar((5,4),3,0, 9)
        self.board.addCar((8,4),3,0, 2)
        self.board.addCar((0,5),2,0, 8)
        self.board.addCar((2,5),2,0, 1)
        self.board.addCar((3,6),2,1, 5)
        self.board.addCar((6,6),2,1, 5)
        self.board.addCar((0,7),2,0, 7)
        self.board.addCar((1,7),2,0, 5)
        self.board.addCar((2,7),2,1, 8)
        self.board.addCar((4,7),2,0, 1)
        self.board.addCar((5,7),3,1, 10)
        self.board.addCar((8,7),2,0, 7)
        self.board.addCar((2,8),2,1, 7)

    def loadGame6(self):
        width = 9
        height = 9
        self.board = Board(width,height)
        self.board.setExitCoord((8,4))
        self.windowWidth = width * 50
        self.windowHeight = height * 50
        self.board.addCar((0,4),2,1, 0, True)
        self.board.addCar((0,0),2,1, 8)
        self.board.addCar((2,0),2,1, 6)
        self.board.addCar((4,0),2,0, 5)
        self.board.addCar((7,0),2,0, 8)
        self.board.addCar((0,1),2,0, 6)
        self.board.addCar((1,1),3,1, 3)
        self.board.addCar((5,1),2,1, 1)
        self.board.addCar((2,2),2,1, 5)
        self.board.addCar((4,2),2,0, 1)
        self.board.addCar((5,2),2,0, 6)
        self.board.addCar((7,2),2,1, 5)
        self.board.addCar((2,3),2,0, 8)
        self.board.addCar((3,3),3,0, 2)
        self.board.addCar((6,3),3,1, 10)
        self.board.addCar((1,5),2,0, 1)
        self.board.addCar((4,5),2,1, 6)
        self.board.addCar((6,5),2,1, 1)
        self.board.addCar((8,5),3,0, 9)
        self.board.addCar((0,6),3,0, 9)
        self.board.addCar((2,6),2,1, 5)
        self.board.addCar((4,6),3,0, 10)
        self.board.addCar((5,6),3,1, 2)
        self.board.addCar((2,7),2,1, 8)
        self.board.addCar((5,7),2,1, 5)
        self.board.addCar((1,8),3,1, 3)

    def loadGame7(self):
        width = 12
        height = 12
        self.board = Board(width,height)
        self.board.setExitCoord((11,5))
        self.windowWidth = width * 50
        self.windowHeight = height * 50
        self.board.addCar((2,5),2,1, 0, True)
        self.board.addCar((0,0),2,0, 5)
        self.board.addCar((6,0),2,0, 8)
        self.board.addCar((7,0),3,1, 9)
        self.board.addCar((10,0),2,1, 6)
        self.board.addCar((5,1),2,0, 6)
        self.board.addCar((10,1),2,0, 1)
        self.board.addCar((11,1),2,0, 8)
        self.board.addCar((0,2),3,1, 2)
        self.board.addCar((3,2),2,1, 1)
        self.board.addCar((6,2),3,0, 3)
        self.board.addCar((7,2),2,1, 5)
        self.board.addCar((0,3),3,0, 9)
        self.board.addCar((1,3),3,0, 3)
        self.board.addCar((5,3),2,0, 5)
        self.board.addCar((7,3),2,1, 1)
        self.board.addCar((9,3),2,1, 6)
        self.board.addCar((2,4),3,1, 10)
        self.board.addCar((7,4),3,1, 9)
        self.board.addCar((4,5),2,0, 1)
        self.board.addCar((5,5),2,0, 6)
        self.board.addCar((0,6),3,1, 10)
        self.board.addCar((3,6),2,0, 6)
        self.board.addCar((6,6),3,0, 2)
        self.board.addCar((7,6),2,0, 8)
        self.board.addCar((9,6),2,0, 6)
        self.board.addCar((10,6),2,1, 5)
        self.board.addCar((0,7),3,1, 2)
        self.board.addCar((4,7),2,1, 5)
        self.board.addCar((10,7),2,1, 8)
        self.board.addCar((0,8),2,1, 1)
        self.board.addCar((2,8),2,0, 5)
        self.board.addCar((3,8),3,1, 9)
        self.board.addCar((7,8),3,1, 3)
        self.board.addCar((11,8),2,0, 5)
        self.board.addCar((3,9),3,1, 2)
        self.board.addCar((6,9),3,0, 10)
        self.board.addCar((8,9),2,1, 5)
        self.board.addCar((10,9),3,0, 9)
        self.board.addCar((9,10),2,0, 6)
        self.board.addCar((11,10),2,0, 6)
        self.board.addCar((1,11),2,1, 5)
        self.board.addCar((3,11),3,1, 3)
        self.board.addCar((7,11),2,1, 8)

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

    def loadTestGame3(self):
        width = 6
        height = 6
        self.board = Board(width,height)
        self.board.setExitCoord((5,2))
        self.windowWidth = width * 50
        self.windowHeight = height * 50
        self.board.addCar((0,2),2,1, 0, True)
        self.board.addCar((5,0),3,0, 2)
        self.board.addCar((4,5),2,1, 2)


