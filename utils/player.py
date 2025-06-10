from typing import List
from utils.card import Card
from random import choice

class Player:
    """
    Class representing the player in the card game
    """
    def __init__(self, name: str) -> None:
        """
        Initialize a Player with a naame and enmpty card slot.
    
        :param name: A string with the player name.
        """
        self.name: str = name
        self.cards: List[Card] = [] # This is the cards in the player hand
        self.turn_count: int = 0 # Number of turns played
        self.number_of_cards: int = 0 # Current number of card in the player hand
        self.history: List[Card] = [] # All cards played by the player
    
    def play(self) -> Card:
        """
        Play a random card
        
        Randomly picks a card from player hands, add to the history, print the action and 
        return the card that was played
        
        :return: The card that was played
        """
        
        # Randomly pick a card from the player's hand
        played_card = choice(self.cards)
    
        # Remove the card from his hand
        self.cards.remove(played_card)
        
        # Add the card to the player's history
        self.history.append(played_card)
        
        # increment the turn
        self.turn_count += 1
        
        # Update number of cards
        self.number_of_cards = len(self.cards)
        
        # Print 
        print(f"{self.name} turn {self.turn_count} played: {played_card.value} {played_card.icon} {played_card.color}")
        
        return played_card
    
    def __str__(self) -> str:
        """
        String representation of the Player.
        
        :return: A string showing the player's name and number of cards.
        """
        return f"Player {self.name} with {self.number_of_cards} cards"

