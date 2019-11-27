# The Tron server
class Server:

    # Set up data structures and open UDP server
    def __init__(self):
        pass

    # Start listening for conecting messages, create new clients send connected message
    # Ensures addtional connecting message from the same client does not 
    #   produce multiple clients in the game state
    def listen_for_connections(self);
        pass

    # Send the game starting message to all players and ensure a ack was received
    def send_game_starting(self):
        pass

    # Get any player directin inputs through non blocking calls for player direction messages
    def get_direction_inputs(self):
        pass

    # Update the game state
    def update_game_state(self):
        pass

    # Send out game state message
    def send_game_state(self):
        pass

    # Start updating the game state and waiting for player direction messages
    def start_game(self):
        pass