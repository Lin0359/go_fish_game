from random import shuffle

class Card:
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value
        if 2 <= value <= 10:
            self.name = str(value)
        else:
            special_names = {11: "Jack", 12: "Queen", 13: "King", 14: "Ace"}
            self.name = special_names[value]

    def __str__(self):
        return f"{self.name} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = []
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        for suit in suits:
            for value in range(2, 15):  
                self.cards.append(Card(value, suit))

        shuffle(self.cards)

    def draw(self):
        if self.cards:
            return self.cards.pop()
        else:
            raise RuntimeError("The deck is empty. Cannot draw any more cards.")
