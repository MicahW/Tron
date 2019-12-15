import GameState

# Creates a sample game state and window

game_state = GameState.GameState()
game_state.setup_game_start([1,2])
board = game_state.get_board()
for x in range(0,len(board)):
    for y in range(0,len(board[x])):
        v = board[x][y]
        if v != 0:
            print("{}: ({}, {})".format(v, x, y))
