from typing import List
from random import shuffle


class Symbol:
    """
    Class representing a card symbol with color and icon.
    """
    
    def __init__(self, color: str, icon: str) -> None:
        """
        Initialize a Symbol with color and icon.
        
        :param color: A string representing the color of the symbol.
        :param icon: A single character from [♥, ♦, ♣, ♠].
        """
        self.color: str = color
        self.icon: str = icon
    
    def __str__(self) -> str:
        """
        String representation of the Symbol.
        
        :return: A string showing the symbol's color and icon.
        """
        return f"{self.color} {self.icon}"

class Card(Symbol):
    """
    Class representing a playing card that inherits from Symbol.
    """
    
    def __init__(self, color: str, icon: str, value: str) -> None:
        """
        Initialize a Card with color, icon, and value.
        
        :param color: A string representing the color of the symbol.
        :param icon: A single character from [♥, ♦, ♣, ♠].
        :param value: A string representing the card value from ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'].
        """
        super().__init__(color, icon)
        self.value: str = value
    
    def __str__(self) -> str:
        """
        String representation of the Card.
        
        :return: A string showing the card's value and symbol icon.
        """
        return f"{self.value} {self.icon}"
   
class Deck:
    """
    Class representing a deck of playing cards.
    """
    
    def __init__(self) -> None:
        """
        Initialize an empty Deck.
        """
        self.cards: List[Card] = []
    
    def fill_deck(self) -> None:
        """
        Fill the deck with a complete set of 52 playing cards.
        Creates one card for each combination of value and symbol.
        """
        # Define the symbols with their colors and icons
        symbols = [
            ("red", "♥"),
            ("red", "♦"),
            ("black", "♣"),
            ("black", "♠")
        ]
        
        # Define all possible card values
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        
        
        #Create all 52 cards
        for color, icon in symbols:
            for value in values:
                card = Card(color, icon, value)
                self.cards.append(card)
    def shuffle(self) -> None:
        shuffle(self.cards)

    def distribute(self, players: List['Player']) -> None:
        """
        Distribute all card between players.
    
        :param players: A list of Player objects to distribute cards to.
        """
    
        # Calculate how many cards each player should get
        cards_per_player  = len(self.cards) // len(players)
    
        # Distribute cards to each player
        card_index = 0
        for player in players:
            #Give each player their shafe of cards
            player.cards = []
            for _ in range(cards_per_player):
                if card_index < len(self.cards):
                    player.cards.append(self.cards[card_index])
                    card_index += 1
            player.number_of_cards = len(player.cards)
        
        #Distribute any remaining cards
        
        player_index = 0
        while card_index < len(self.cards):
            players[player_index].cards.append(self.cards[card_index])
            players[player_index].number_of_cards += 1
            card_index += 1
            player_index = (player_index + 1) % len(players)
    
    
    def __str__(self) -> str:
        """
        String representation of the Deck.
        
        :return: A string showing the number of cards in the deck.
        """
        return f"Deck with {len(self.cards)} cards"
    


