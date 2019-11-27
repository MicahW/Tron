SIZE_X = 200
SIZE_Y = 200

# Holds board values and player head values
class GameState:

    # Create empty board and player states
    def __init__(self):
        self.board = [[0] * SIZE_Y] * SIZE_X

        # players[player_number] = [head_x, head_y, direction, alive])
        self.players = {}

    # Called by server to set player direction on request
    def set_direction(self, player_number, direction):
        if player_number in player.keys():
            players[player_number][2] = direction

    # Called by server to update the game state
    def tick(self):
        pass

    # Called by server to add a new player, returns player number
    def create_new_player(self):
        pass

    # Randomizes players on the edge of the board
    def randomize_positions(self):
        pass

