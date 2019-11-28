from graphics import *

import GameState

BOARD_SCALE = 4


# Container for Graphics Window and all graphis related functionality
class Window():

    def __init__(self):
        self.size_x = GameState.SIZE_X * BOARD_SCALE
        self.size_y = GameState.SIZE_Y * BOARD_SCALE
        self.window = GraphWin("Tron",
                               self.size_x,
                               self.size_y,
                               autoflush = False)
        self.window.setBackground("black")

    def render_start_screen(self):
        titleText = Text(Point(self.size_x / 2, 20), 'Tron')
        titleText.setTextColor("white")
        titleText.draw(self.window)

        addrText = Text(Point(self.size_x / 2, 100), "IP Address")
        addrText.setTextColor("white")
        addrText.draw(self.window)

        self.addrEntry = Entry(Point(self.size_x / 2, 150), 20)
        self.addrEntry.draw(self.window)

        portText = Text(Point(self.size_x / 2, 200), "Port")
        portText.setTextColor("white")
        portText.draw(self.window)

        self.portEntry = Entry(Point(self.size_x / 2, 250), 20)
        self.portEntry.draw(self.window)