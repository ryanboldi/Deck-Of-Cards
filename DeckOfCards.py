""" 
Author: Ryan Boldi
Date: 19/8/18
"""

class Card(object):
    """Class of a Card object
    """
    
    colors = ["Red", "Black"]
    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
    symbols = ["♠","♥","♣","♦"]
    values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    
    def __init__(self, value, suit, name = None):
        
        if (suit == "Hearts" or suit == "Diamonds"):    
            self.color = "Red"
        elif  (suit == "Spades" or suit == "Clubs"):
            self.color = "Black"
        else:
            raise ValueError("Color and suit do not match")
       
        if (suit in self.suits):
            self.suit = suit
        else:
            raise ValueError("Suit not valid")
            
        if (value in self.values):
            self.value = value
        else:
            raise ValueError("Value not valid")
            
            
        self.symbol = None
        if self.suit == "Spades":
            self.symbol = self.symbols[0]
        elif self.suit == "Hearts":
            self.symbol = self.symbols[1]
        elif self.suit == "Clubs":
            self.symbol = self.symbols[2]
        else:
            self.symbol = self.symbols[3]
            
        self.name = self.value + self.symbol
        

    def getColor(self):
        return self.color
    def getSuit(self):
        return self.suit
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    
    def __str__(self):
        return str(self.name)
        
        


class DeckOfCards(object):
    def __init__(self):
        self.Deck = []
    
    def getDeck(self):
        return self.Deck
    
    def addCard(self, card):
        self.Deck.append(card)
    
    def __str__(self):
        return str([str(i) for i in self.Deck])
    




