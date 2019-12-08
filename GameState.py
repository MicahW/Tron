SIZE_X = 200
SIZE_Y = 200


# Holds board values and player head values
class GameState:

    # Maps dirrection states to x and y position changes
    direction_map = {
        0: [-1, 0],  # Left
        1: [0, -1],  # Up
        2: [1, 0],   # Right
        3: [0, 1]    # Down
    }

    # Maximun number of players supported
    MAX_PLAYERS = 4

    # Player starting positions
    starting_positions = [
        [0, SIZE_Y / 2],           # Left side
        [SIZE_X - 1, SIZE_Y / 2],  # Right side
        [SIZE_X / 2, 0],           # Top
        [SIZE_X / 2, SIZE_Y - 1]   # Bottom
    ]

    # Player starting directions
    starting_directions = [
        2,  # Right
        0,  # Left
        3,  # Down
        1   # Up
    ]

    # Contructor to initialize an empty state
    def __init__(self):
        self.init_empty_state()

    def init_empty_state(self):
        self.board = [[0] * SIZE_Y] * SIZE_X

        # players[player_number] = [head_x, head_y, direction, alive])
        self.players = {}

    # Set up the game state for the start of a game
    def setup_game_start(self, player_numbers):
        self.init_empty_state()
        if len(player_numbers) > MAX_PLAYERS:
            raise "Cannont set the game state for more players the supported"

        # Add each player to the game
        for i in range(0,len(player_numbers)):
            player_number = player_numbers[i]
            start_x = starting_positions[i][0]
            start_y = starting_positions[i][1]

            self.players[player_number] = [
                start_x,
                start_y,
                self.starting_directions[i],
                True
            ]

            self.board[start_x][start_y] = player_number

    # Called by server to set player direction on request
    def set_direction(self, player_number, direction):
        if player_number in player.keys():
            players[player_number][2] = direction

    # Called by server to update the game state
    # Returns a list of dead players
    def tick(self):
        # Move each head then add it to the board
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

    # Updates the game state from the information contained in a game state message
    # client_states are lists of touples in the form (client_number, [(x0, y0), (x1, y1)])
    def update(self, dead_list, client_states):
        # Kill off dead players
        for dead in dead_list:
            if dead in self.players.keys():
                self.players[dead][3] = False
        
        # Update each client states
        for client_num, positions in client_states:
            if (client_num in self.players.keys() and
                len(positions) > 0):
                # Set head position for (x0, y0)
                self.players[client_num][0] = positions[0][0]
                self.players[client_num][1] = positions[0][1]

                # Set the board walls for the last player positions
                for x, y in positions:
                    self.board[x][y] = client_num

    # Called by server to add a new player, returns player number
    def create_new_player(self):
        pass

    # Randomizes players on the edge of the board
    def randomize_positions(self):
        pass
