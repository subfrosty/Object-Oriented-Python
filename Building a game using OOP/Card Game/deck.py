# Defines Deck class
class Deck:
    # Initiates deck object as an empty list
    def __init__(self):
        self.deck = []

    # Creates method to check length of deck (list)
    def __len__(self):
        return len(self.deck)

    # Creates method to add a card to the deck
    def add_card(self, card):
        self.deck.append(card)

    # Creates method to remove last card from deck
    def pop_card(self):
        self.deck.pop()