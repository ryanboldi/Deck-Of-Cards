import DeckOfCards as DC

card = DC.Card("K","Spades")
newCard = DC.Card("2","Hearts")

ryanDeck = DC.DeckOfCards()
ryanDeck.addCard(card)
ryanDeck.addCard(newCard)

print(ryanDeck)