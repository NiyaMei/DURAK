import utils
from cards import Deck, Card
from players import Player, Comp



def test1():
    card1 = Card("spades", 10)
    card2 = Card("diamonds", 11)
    deck1 = Deck()
    deck1.add_card(card1)
    deck1.add_card(card2)
    for card in deck1:
        card.show_card()

def main():
    test1()

if __name__ == '__main__':
    main()



