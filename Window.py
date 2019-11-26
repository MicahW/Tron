from graphics import *

import GameState

# Container for Graphics Window and all graphis related functionality
class Window():

    BOARD_SCALE = 1

    def __init__(self):
        self.window = GraphWin("Tron",
                               GameState.SIZE_X * BOARD_SCALE,
                               GameState.SIZE_Y * BOARD_SCALE)

