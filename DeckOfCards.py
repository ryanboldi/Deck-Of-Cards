""" 
Author: Ryan Boldi
Date: 19/8/18
"""
from random import randint, seed

class Card(object):
    """Class of a Card object
    """
    #ids go A -> K of Spades, A -> K of Diamonds,
    #A -> K of Clubs, A -> K of Hearts
    #Ace of spades is 0, king of hearts is 51`
    colors = ["Red", "Black"]
    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
    symbols = ["♠","♥","♣","♦"]
    values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    
    def __init__(self, value, suit, name = None):
        self.id = 0
        
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
            self.id += 0
        elif self.suit == "Hearts":
            self.symbol = self.symbols[1]
            self.id += 39
        elif self.suit == "Clubs":
            self.symbol = self.symbols[2]
            self.id += 26
        else:
            self.symbol = self.symbols[3]
            self.id += 13
        self.name = self.value + self.symbol
        
        for i in range (len(self.values)):
            if value == str(self.values[i]):
                self.id += i
        
        
    def getId(self):
        return self.id
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
    
    def __repr__(self):
        return str(self.name)
    
    def __eq__(self, other):
        return self.id == other.id
           
class DeckOfCards(object):
    values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    def __init__(self):
        self.Deck = []
    
    def getDeck(self):
        return self.Deck
    
    def addCard(self, card):
        self.Deck.append(card)
    
    def __str__(self):
        return str([str(i) for i in self.Deck])
    
    def getCardFromId(self, Id):
        if Id <= 12:
            suit = "Spades"
            value = self.values[Id-1]
        elif Id <= 25:
            suit = "Diamonds"
            value = self.values[Id-12-1]
        elif Id <= 38:
            suit = "Clubs"
            value = self.values[Id-25-1]
        elif Id <= 51:
            suit = "Hearts"
            value = self.values[Id-38-1]
        else:
            raise ValueError("Id not valid")
        
        return (Card(value,suit))
        
    def addCardFromId(self, Id):
        self.addCard(self.getCardFromId(Id))
    
    
    def addRandomCard(self):   
        rand = randint(0,51)
        if not (self.getCardFromId(rand) in self.Deck):
            self.addCardFromId(rand)
            
        
    def addRandomCards(self, amount):
        for i in range (amount):
            self.addRandomCard()
        
    def deckToArray(self):
        return self.Deck

    def printDeck(self):
        temp = self.deckToArray()
        print(*temp, sep=" ")
