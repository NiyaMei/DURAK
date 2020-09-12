from cards import Deck, Card
from constants import NUMS_DICT, VALUES_DICT
from utils import *


class APlayer:
    def __init__(self, a_name):
        self.deck = None
        self._name = a_name

    def take_cards_from_deck(self, deck):           # shall I delete deck parameter?
        need_cards = 6 - len(self.deck)
        if need_cards <= 0 or len(deck) == 0:
            return "Players have enough cards. Let's continue"
        if need_cards > len(deck):
            cards_for_a_player = deck.draw_several_cards(len(deck))
            self.deck.add_cards(cards_for_a_player)
            return "The main deck is empty. Continue the game"
        cards_for_a_player = deck.draw_several_cards(need_cards)
        self.deck.add_cards(cards_for_a_player)
        return "Players have enough cards. Let's continue"


class Player(APlayer):
    def defends(self, attack_cards, trump_suit):
        print("Here're your cards: ")
        self.deck.show()
        print("Comp attacks you with these cards: ")
        for i in range(len(attack_cards)):
            print(VALUES_DICT[attack_cards.get_card_by_index(i).value], attack_cards.get_card_by_index(i).suit)
        defend_cards = Deck()
        cards_indices = list(map(int, input("What cards do you put for attack? Write their indices (if you can't beat a card, type '-1'):  ").split()))
        for card_index in cards_indices:
            for attack_card in attack_cards:
                if card_index == -1:
                    self.deck.add_cards(attack_cards)
                    return "You couldn't defend and picked up cards"
                defend_card = self.deck.get_card_by_index(card_index)
                if is_beatable(defend_card, attack_card, trump_suit) == False:
                    return "Wrong action"
                defend_cards.add_card(defend_card)
        print("You're throwing these cards: ")
        defend_cards.show()
        updated_deck = Deck()
        for j in range(len(self.deck)):
            if j in cards_indices:
                continue
            updated_deck.add_card(self.deck[j])
        self.deck = updated_deck
        print("Here're your cards now: ")
        self.deck.show()
        return "Defended succesfully"

    def attacks(self, trump_suit):
        self.deck.show()  # delete later
        cards_indices = list(map(int, input("What cards do you put for attack? Write their indices:  ").split()))
        attack_cards = Deck()
        for card_index in cards_indices:
            attack_card = self.deck.get_card_by_index(card_index)
            attack_cards.add_card(attack_card)
        attack_cards.show()
        updated_deck = Deck()
        for j in range(len(self.deck)):
            if j in cards_indices:
                continue
            updated_deck.add_card(self.deck[j])
        self.deck = updated_deck
        print("Here're your cards now: ")
        self.deck.show()
        return "You're attacking with these cards: ", attack_cards


class Comp(APlayer):
    def __init__(self, a_name="comp"):
        super().__init__(a_name)

    # TO DO: add possibility to pick up cards if couldn't beat, and it must return Boolean: defended or not
    def defends(self, attack_cards, trump_suit):
        defended_or_not = False
        defend_cards_indices = []
        for attack_card in attack_cards:
            for j, defend_card in enumerate(self.deck):
                defended_or_not = is_beatable(defend_card, attack_card, trump_suit)
                if defended_or_not == True:
                    defend_cards_indices.append(j)
            if defended_or_not == False:
                self.deck.add_card(attack_card)
                return "Comp couldn't beat the cards and it picked them."
        for j in range(len(self.deck)):                 # I added delete defend cards from comp's hand
            if j in defend_cards_indices:
                self.deck.delete_card(j)
        return defended_or_not

    def attacks(self, trump_suit):
        plain_suit = Deck()         # plain_suit contains all comp's non-trump suit cards
        for i in self.deck.deck:        # I forgot why?
            if i.suit != trump_suit:
                plain_suit.add_card(i)
        attack_cards = Deck()
        min_card = plain_suit.find_min()
        for i, card in enumerate(plain_suit):
            #print("a plain suit card:")
            #card.show_card()
            if are_equal_cards(card, min_card, trump_suit):
                attack_cards.add_card(card)
                self.deck.delete_card(i)
        return  "Comp attack with these cards: ", attack_cards







