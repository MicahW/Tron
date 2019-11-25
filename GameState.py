# Holds board values and player head values
class GameState:
    
    SIZE_X = 200
    SIZE_Y = 200

    # Create empty board and player states
    def __init__(self):
        self.board = [[0] * SIZE_Y]] * SIZE_X

        # players[player_
        self.players = {}

    # Called by server to set player direction on request
    def set_direction(player_number, direction):
        pass

    # Called by server to update the game state
    def tick()
        pass

    # Called by server to add a new player, returns player number
    def create_new_player():
        pass

    # Randomizes players on the edge of the board
    def randomize_positions():
        pass

