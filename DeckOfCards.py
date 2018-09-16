""" 
Author: Ryan Boldi
Date: 19/8/18
"""
import math
from random import randint
from Card import Card
          
class DeckOfCards(object):
    values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    def __init__(self):
        self.Deck = []
    
    def __add__(self,other):
        return(self.Deck + other.Deck)
    
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
        else:
            self.addRandomCard()
            
        
    def addRandomCards(self, amount):
        for i in range (amount):
            self.addRandomCard()
        
    def deckToArray(self):
        return self.Deck
    
    def addCards(self, cards):
        for i in range(len(cards)):
            self.Deck.append(cards[i])

    def printDeck(self):
        temp = self.deckToArray()
        print(*temp, sep=" ")
        
    def riffleShuffle(self):
            
        raise NotImplementedError
         

        
    #leaves the original first card first, and the original last card last
    def outFaro(self):
        FullLen = len(self.Deck)
        if FullLen % 2 != 0:
            #noramlises for odd lengths
            FullLen+=1
        deck1 = self.Deck[:int(FullLen/2)]
        deck2 = self.Deck[int(FullLen/2):]
        
        
        newDeck = DeckOfCards()
        #print(deck1, deck2)
        
        for i in range(math.ceil(FullLen/2)):
            newDeck.addCard(deck1[i])
            newDeck.addCard(deck2[i])
        
        return newDeck
    
        #leaves the first card second, and the bottom second to bottom
    def inFaro(self):
    
        FullLen = len(self.Deck)
        if FullLen % 2 != 0:
            #noramlises for odd lengths
            FullLen+=1
        deck1 = self.Deck[:int(FullLen/2)]
        deck2 = self.Deck[int(FullLen/2):]
        
        
        newDeck = DeckOfCards()
        #print(deck1, deck2)
        
        for i in range(math.ceil(FullLen/2)):
            newDeck.addCard(deck2[i])
            newDeck.addCard(deck1[i])
        
        return newDeck
        
        
