from DeckOfCards import DeckOfCards
from Card import Card
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
    
    doTrick(TrickDeck)
    

def doTrick(Deck):
    print("I will now deal these cards into 3 piles")
    time.sleep(1)
    print("....")
    time.sleep(0.5)
    print("Alright, I got it")
    
    for i in range(3):
    
        arr1, arr2, arr3 = magicDeal(Deck)
        print(*arr1, sep=" ")
        print(*arr2, sep=" ")
        print(*arr3, sep=" ")
        
        time.sleep(1)
        
        arr = [arr1,arr2,arr3]
        Good = False
        while Good == False:
            allowedInputs = [1,2,3]
            try:
                num = input("Which pile is your card in? (1,2,3) : ")
                int(num)
            except ValueError:
                print("not a number, please try again")
                break
            
            if int(num) in allowedInputs:
                newDeck = DeckOfCards()
                num = int(num)-1
                try:
                    newDeck.addCards(arr[num+1])
                except IndexError:
                    newDeck.addCards(arr[0])
                newDeck.addCards(arr[num])
                try:
                    newDeck.addCards(arr[num-1])
                except IndexError:
                    newDeck.addCards(arr[2])
                
                Deck = newDeck
                Good = True
                    
            else:
                print("not a valid pile, please try again")
                    
            
    
    



#returns 3 arrays of the original deck dealt magically
def magicDeal(Deck):
    MainArray = Deck.deckToArray()
    temp1 = [] #3n-3
    temp2 = [] #3n-2
    temp3 = [] #3n-1
    
    #print (len(MainArray))
    for i in range(len(MainArray)):
        #print (i)
        if inSeq(i,3,-3):
            #print (i, "temp 1")
            temp1.append(MainArray[i])
        elif inSeq(i,3,-2):
            #print (i, "temp 2")
            temp2.append(MainArray[i])
        else:
            #print (i, "temp 3")
            temp3.append(MainArray[i])
            
    return temp1, temp2 , temp3

#determines if a number is part of a sequence when given the nth term
def inSeq(num, bef, aft):
    #print("nth term =" ,bef, "n", aft)
    #print("is ", num, " in ", bef, "n", aft)
    temp = num - aft
    if temp % bef == 0:
        return True
    else:
        return False
    
    
    
if __name__ == "__main__":
    main()