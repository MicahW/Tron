SIZE_X = 200
SIZE_Y = 200


# Holds board values and player head values
class GameState:

    direction_map = {
        0: [-1, 0],
        1: [0, -1],
        2: [1, 0],
        3: [0, 1]
    }

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
    # Returns a list of dead players
    def tick(self):
        # Move each head then add it to the baord
        for player_number, (head_x, head_y, direction, alive) in self.players.items():
            if alive:
                delta_x, delta_y = direction_map[direction]
                head_x = head_x + delta_x
                head_y = head_x + delta_y
                self.players[player_number] = [head_x, head_y, direction, alive]
                self.board[head_x][head_y] = player_number

        # Check if any heads colided into a wall
        dead_list = []
        for player_number, (head_x, head_y, direction, alive) in self.players.items():
            if alive:
                if (board[head_x][head_y] != 0):
                    dead_list.append(player_number)
                    self.players[player_number] = [head_x, head_y, direction, False]

        return dead_list

    # Called by server to add a new player, returns player number
    def create_new_player(self):
        pass

    # Randomizes players on the edge of the board
    def randomize_positions(self):
        pass
