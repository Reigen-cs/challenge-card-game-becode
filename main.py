from utils.player import Player
from utils.game import Board


def main() -> None:
    """
    Main function to start the card game.
    
    Creates players, initializes the game board, and starts the game.
    """
    print("Welcome to Reigen Card game!")
    print("*" * 40)
    
    # Create players for the game
    players = [
        Player("Reigen"),
        Player("Nixfe"),
        Player("Younes"),
        Player("Amina")
    ]
    
    # Create the game board with the players
    board = Board(players)
    
    # Start the game
    board.start_game()


if __name__ == "__main__":
    main()