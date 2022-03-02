# deck.py
"""Deck class represents a deck of Cards."""
import random
from modules.card import Card  ## modules.card is needed if python is run from different directory

class DeckOfCards:
    NUMBER_OF_CARDS = 52  # constant number of Cards

    def __init__(self):
        """Initialize the deck."""
        self._current_card = 0 # card index set to 0
        self._deck = []

        for count in range(DeckOfCards.NUMBER_OF_CARDS):
            self._deck.append(Card(Card.FACES[count % 13], Card.SUITS[count // 13]))

    def shuffle(self):
        """Shuffle deck"""
        self._current_card = 0
        random.shuffle(self._deck)
    
    def deal_card(self):
        """Deal Cards"""
        try:
            card = self._deck[self._current_card]
            self._current_card += 1
            return card
        except:
            return None\
                
    def __str__(self):
        """Return a string representation of the current _deck."""
        s = ''

        for index, card in enumerate(self._deck):
            s += f'{self._deck[index]:<19}'
            if (index + 1) % 4 == 0:
                s += '\n'
        
        return s

    
