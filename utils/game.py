from typing import List
from utils.player import Player
from utils.card import Deck, Card

class Board:
    """
    Class for the board where the game is played
    """
    
    def __init__(self, players: List[Player]) -> None:
        """
        Initalize the board with the player 
        
        param players: A list of player who will participate in the game
        """
        self.players: List[Player] = players
        self.turn_count: int = 0
        self.active_cards: list[Card] = [] # Last card that was played by each of the player
        self.history_cards: List[Card] = [] # all card that was played except the last one ( active_cards)
    def start_game(self) -> None:
        """
         Start the game
    
         1. Create and fill the deck
         2. Shuffle it
         3. Distribute cards to each player
        4. Run a loop ( the game ) untill all players dooes not have card anymore
            """
    
        print("Starting the game!")
        print(f"Players: {', '.join([player.name for player in self.players])}")
        print()
    
        # Create and the deck
        deck = Deck()
        deck.fill_deck()
        deck.shuffle()
    
        # Distribute cards to players
        deck.distribute(self.players)
    
        print(f"Cards distribued!")
        for player in self.players:
            print(f"{player.name}: {player.number_of_cards} cards")
            print()
         # Loop of the game ( goes on untill all players does not have card anymore)
            while any(player.number_of_cards > 0 for player in self.players):
                self.turn_count += 1
                print(f"This is the turn {self.turn_count}, let's look what cards did the player played ?")
                print()

                # Move current active cards to the history (Not the first turn)
                if self.active_cards:
                    self.history_cards.extend(self.active_cards) 
            
                # Clear the active cards each turn
                self.active_cards = []
            
                # Each players play a card
                for player in self.players:
                    if player.number_of_cards > 0:
                        played_card = player.play()
                        self.active_cards.append(played_card)
                # Print the turn
                print(f"=== Turn {self.turn_count} summary : ===")
                print(f"Active cards: {[str(card) for card in self.active_cards]}")
                print(f"Total cards in the history: {len(self.history_cards)}")
                print()
                print()
        
            # put the final active cards to the history at the end
            if self.active_cards:
                self.history_cards.extend(self.active_cards)
                self.active_cards = []
        
            print("GAME IS DONE")
            print("Each of the player are out of cards")
            print(f"Total turns played: {self.turn_count}")
            print(f"Total cards played: {len(self.history_cards)}")
        
            # Show the final player stats
            print("\nFinal player statistics:")
            for player in self.players:
                print(f"{player.name}: Played {len(player.history)} cards in {player.turn_count} turns")
        
def __str__(self) -> str:
        """
        String representation of the Board.
        
        :return: A string showing the current game state.
        """
        return f"Board with {len(self.players)} players, turn {self.turn_count}"     
    
    
       
