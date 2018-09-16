# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 22:54:23 2018

@author: ryan-pc

Created By: Ryan Boldi
"""
import DeckOfCards

Deck = DeckOfCards.DeckOfCards()

Deck.addRandomCards(52)

print(Deck)
print(("                   \n"))
print(Deck.inFaro())
    