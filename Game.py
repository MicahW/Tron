import GameState
import Window


# Client class to connect to server, handle user inputs, and render the game
class Game:

    def __init__(self):
        self.window = Window.Window()

    # Send a connecting message and receive a connected message
    # Store the client ID
    def connect(addr, port):
        pass

    # Wait for game starting and send game starting ack
    def wait_for_game_starting():
        pass

    # Send multiple direction messages
    def send_direction(direction):
        pass

    # Get the game state if present in the buffer and return it in a friendly
    # format
    def get_game_state():
        pass

game = Game()

# TODO remove this wait for real block on user input
input("Press any key to exit")
