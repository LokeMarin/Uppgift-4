import os

#"♠", "♥", "♣", "♦"

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    #vanlig metod i en klass
    def show(self):
        return f"{self.suit} {self.value}"
    
    def __str__(self):
        return f"{self.suit} {self.value}"
    
    def __repr__(self):
        return f"{self.suit} {self.value}"

def create_deck():
    cards = []

    suits = ["♠", "♥", "♣", "♦"]
    values = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    
    
    for suit in suits:
        for value in values:
            cards.append(Card(suit, value))
            

    return cards

#skapa ett kort

os.system("cls")

cards = []

#cards.append = (Card("♥",2))
#cards.append = (Card("♥",4))

cards = create_deck()
for cards in cards:
    print(cards)

                