from DeckOfCards import DeckOfCards
import time


def main():
    TrickDeck = DeckOfCards()
    TrickDeck.addRandomCards(21)
    
    
    print("Welcome to my magic trick. I have 21 cards: ")
    TrickDeck.printDeck()
    time.sleep(1)
    
    print("Please think of any of these cards")
    time.sleep(3)
    print("Got one?")
    time.sleep(2)
    
    print("I will now deal these cards into 3 piles")
    time.sleep(1)
    print("....")
    time.sleep(0.5)
    print("alright I got it")
    
    arr1, arr2, arr3 = magicDeal(TrickDeck)
    print(*arr1, sep=" ")
    print(*arr2, sep=" ")
    print(*arr3, sep=" ")

#returns 3 arrays of the original deck dealt magically
def magicDeal(Deck):
    MainArray = Deck.deckToArray()
    temp1 = [] #3n-3
    temp2 = [] #3n-2
    temp3 = [] #3n-1
    
    print (len(MainArray))
    for i in range(len(MainArray)):
        print (str(temp1), str(temp2), str(temp3))
        if inSeq(i,3,-3):
            temp1.append(MainArray[i])
        elif inSeq(i,3,-2):
            temp2.append(MainArray[i])
        elif inSeq(i,3,-1):
            temp3.append(MainArray[i])
            
    return temp1, temp2 , temp3

#determines if a number is part of a sequence when given the nth term
def inSeq(num, bef, aft):
    #print("nth term =" ,bef, "n", aft)
    print("is ", num, " in ", bef, "n", aft)
    firstNum = bef+aft
    dif = num-firstNum
    if dif % bef ==0:
        return True
    
    
    
if __name__ == "__main__":
    main()