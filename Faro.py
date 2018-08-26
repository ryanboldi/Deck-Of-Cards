from DeckOfCards import Card
from DeckOfCards import DeckOfCards

ryanDeck = DeckOfCards()

card = Card("K","Spades")
newCard = Card("K","Hearts")
ryanDeck.addCardFromId(51)
ryanDeck.addRandomCard()

ryanDeck.addCard(card)
ryanDeck.addCard(newCard)

print(ryanDeck)
print(newCard.getId())