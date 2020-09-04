import random
from constants import NUMS_DICT, VALUES_DICT

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show_card(self):
        print("{} of {}".format(VALUES_DICT[self.value], self.suit), ', ')

    all_suits = ('hearts', 'diamonds', 'spades', 'clubs')
    all_nums = ('6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')

    @staticmethod
    def choose_trump_suit():
        trump_suit = random.choice(Card.all_suits)
        return trump_suit


class Deck:
    def __init__(self):
        self.deck = []
        self.index = -1                     #?

    def build(self):
        for s in ['spades', 'clubs', 'diamonds', 'hearts']:
            for v in range(6, 15):
                card1 = Card(s, v)
                self.deck.append(card1)

    def __len__(self):
        return len(self.deck)

    def __getitem__(self, key):
        return self.deck[key]

    def show(self):
        for c in self.deck:
            c.show_card()

    def shuffle(self):
        return random.shuffle(self.deck)

    def draw(self):
        return self.deck.pop()

    def draw_several_cards(self, number):
        cards_drawn = Deck()
        for _ in range(number):
            card = self.draw()
            cards_drawn.add_card(card)
        return cards_drawn

    def random_draw(self):
        return random.choice(self.deck)

    def delete_card(self, ind):
        return self.deck.pop(ind)

    def add_card(self, card):
        self.deck.insert(0, card)

    def add_cards(self, deck):
        for card in deck:
            self.add_card(card)

    def get_card_by_index(self, i):
        self.show()
        print(i)
        return self.deck[i]

    def find_min(self):
        min_value = 15
        min_card = Card("clubs", min_value)
        for elem in self.deck:
            if elem.value < min_value:
                min_value = elem.value
                min_card = elem
        return min_card

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            try:
                self.index += 1
                return self.deck[self.index]
            except IndexError:
                raise StopIteration
