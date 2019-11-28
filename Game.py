import GameState
import Window


# Client class to connect to server, handle user inputs, and render the game
class Game:

    def __init__(self):
        self.window = Window.Window()
        self.title_screen()
    
    def title_screen(self):
        self.window.render_start_screen()
        addr, port = self.window.get_connect_info()
        print("{} {}".format(addr, port))

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
