import logging
import argparse

logger = logging.getLogger('Tron.Server')


# The Tron server
class Server:

    # Set up data structures and open UDP server
    def __init__(self):
        pass

    # Start listening for conecting messages, create new clients send connected
    # message. Ensures addtional connecting message from the same client does
    # not produce multiple clients in the game state
    def listen_for_connections(self):
        pass

    # Send the game starting message to all players and ensure a ack was
    # received
    def send_game_starting(self):
        pass

    # Get any player directin inputs through non blocking calls for player
    # direction messages
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


if __name__ == '__main__':

    # Setup logging
    logging.basicConfig(
        format='[%(asctime)s.%(msecs)03d] %(levelname)s:%(name)s - %(message)s',
        datefmt='%I:%M:%S')

    tron_logger = logging.getLogger('Tron')
    tron_logger.setLevel(logging.INFO)

    # Setup command line arguments
    parser = argparse.ArgumentParser()

    parser.add_argument("-v", "--verbosity",
                        type=int, default=1, choices=[0, 1, 2],
                        help="verbosity of output; default is 1")

    # Process command line arguments
    args = parser.parse_args()

    if args.verbosity == 0:
        tron_logger.setLevel(logging.ERROR)
    elif args.verbosity == 2:
        tron_logger.setLevel(logging.DEBUG)

    # Start processing
    logger.info("Starting")
