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

    # Clear the window
    def clear(self):
        for item in self.window.items[:]:
            item.undraw()
            win.update()

    def inside(self, point, rectangle):
        """ Is point inside rectangle? """

        ll = rectangle.getP1()  # assume p1 is ll (lower left)
        ur = rectangle.getP2()  # assume p2 is ur (upper right)

        return ll.getX() < point.getX() < ur.getX() and ll.getY() < point.getY() < ur.getY()

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

        self.connectButton = Rectangle(
                                       Point((self.size_x / 2) - 40, 300),
                                       Point((self.size_x / 2) + 40, 340))
        self.connectButton.setFill("grey")
        self.connectButton.draw(self.window)

        connect_text = Text(Point(self.size_x / 2, 320), 'Connect')
        connect_text.setTextColor("white")
        connect_text.draw(self.window)

    def get_connect_info(self):
        while True:
            if self.inside(self.window.getMouse(), self.connectButton):
                return self.addrEntry.getText(), self.portEntry.getText()
        
