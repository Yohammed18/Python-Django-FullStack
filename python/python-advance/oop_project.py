from random import shuffle

SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

# mycards = [(s,r) for s in SUITE for r in RANKS]

# mycards = []
# for r in RANKS:
#     for s in SUITE:
#         mycards.append((s,r))

class Deck():

    def __init__(self):
        print("Creating a new Order Deck")
        # create an object that stores all the cards in the deck
        self.allcards = [(s,r) for s in SUITE for r in RANKS]

    def shuffle(self):
        print('Shuffling Deck')
        shuffle(self.allcards)

    def split_in_half(self):
        return (self.allcards[:26], self.allcards[26:])

class Hand():

    def __init__(self, cards):
        self.cards = cards
    
    def __str__(self) -> str:
        return "Contains {} cards.".format(len(self.cards))
    
    def add(self, added_cards):
        self.cards.extend(added_cards)

    def remove(self):
        return self.cards.pop()


class Player():

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed: {}".format(self.name, drawn_card))
        print("\n")
        return drawn_card
    
    def remove_war_card(self):
        war_cards = []
        for x in range(3):
            war_cards.append(self.hand.cards.pop())
        return war_cards
    
    def still_has_cards(self):
        """
        Return True if player still has cards left
        """
        return len(self.hand.cards) != 0
    