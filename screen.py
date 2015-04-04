import pygame, sys

from pygame.locals import *

class Screen(object):
    """docstring for Screen"""

    screen = None
    width = 0
    height = 0

    gridWidth = 50
    gridHeight = 50


    pygame.display.set_caption('RushHour')

    # Set up the colors.
    BLACK       = (  0,   0,   0)
    GREY        = (127, 127, 127)
    WHITE       = (255, 255, 255)
    RED         = (255,   0,   0)
    ORANGE      = (255, 165,   0)
    YELLOW      = (255, 255,   0)
    YELLOWGREEN = (127, 155,   0)
    GREEN       = (  0, 255,   0)
    GREENCYAN   = (  0, 255, 127)
    CYAN        = (  0, 255, 255)
    AZURE       = (  0, 127, 255)
    BLUE        = (  0,   0, 255)
    VIOLET      = (127,   0, 255)
    MAGENTA     = (255,   0, 255)
    ROSE        = (255,   0, 127)
    BUTTONCOLOR = (  0, 127, 255, 100)
    BUTTONCOLORACTIVE = (  0, 255,   0, 100)
    BUTTONCOLORDEACTIVE = (255,   0,   0, 100)
    OVERLAYCOLOR = (255,255,255,200)

    # The ColorDict is used to determine the color of the disk.
    ColorDict = {0:RED,
                 1:ORANGE,
                 2:YELLOW,
                 3:YELLOWGREEN,
                 4:GREEN,
                 5:GREENCYAN,
                 6:CYAN,
                 7:AZURE,
                 8:BLUE,
                 9:VIOLET,
                 10:MAGENTA,
                 11:ROSE
                }

    def __init__(self, width, height):
        self.screen = pygame.display.set_mode((width, height), \
                                       HWSURFACE|DOUBLEBUF|RESIZABLE)
        self.width = width
        self.height = height

        self.updateScreenSize([width, height])

    def updateScreenSize(self, size):
        self.width = size[0]
        self.height = size[1]

        self.screen = pygame.display.set_mode((self.width,self.height), \
                                               HWSURFACE|DOUBLEBUF|RESIZABLE)

    def drawScreen(self, board):
        self.screen.fill(self.WHITE)
        self.drawBoard(board)
        cars = board.getCars()
        for car in cars:
            self.drawCar(car)

    def drawCar(self, car):
        coords = car.getCoords()
        direction = car.getDirection()
        lenght = car.getLength()
        color = self.ColorDict[car.getColor()]




        xStart = self.gridWidth * coords[0]
        yStart = self.gridHeight * coords[1]

        if direction:
            width = lenght * self.gridWidth
            height = self.gridHeight
        else:
            width = self.gridWidth
            height = lenght * self.gridHeight

        rect = pygame.Rect(xStart, yStart, width, height)


        pygame.draw.rect(self.screen, color, rect)

        if not car.getCanMove():
            pygame.draw.rect(self.screen, self.BLACK, rect, 5)
            color = self.darkenColor(color)


    def drawBoard(self, board):
        x = board.getWidth()
        y = board.getHeight()

        for i in range(0,x):
            pygame.draw.line(self.screen, self.BLACK, (i * self.gridWidth,0), (i * self.gridWidth, y*self.gridHeight))

        for i in range(0,y):
            pygame.draw.line(self.screen, self.BLACK, (0, i * self.gridHeight), (x * self.gridWidth, i*self.gridHeight))

    # Darkens the inputted color and returns the result.
    def darkenColor(self, color):
        darkenFactor = 0.3
        newColor = (int(color[0]*darkenFactor),
                    int(color[1]*darkenFactor),
                    int(color[2]*darkenFactor)
                   )
        return newColor
