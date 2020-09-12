from cards import Deck
import random

def min_trump_suit(trump_suit, a_deck):  # арг-ы функции: метод choose_trump_suit  и a_deck，карты игрока
    all_trump_suit_cards = []
    for i in a_deck.deck:               # a_deck is not a list, is not iterable, a_deck._deck IS a list, it's iterable
        if i.suit == trump_suit:         # если масть карты i равна козырной, то добавляем ее номер в список
            all_trump_suit_cards.append(i.value) # все козырные карты игрока
    if len(all_trump_suit_cards) == 0:
        return 100
    return min(all_trump_suit_cards)

def make_step(player1, player2, trump_suit):  # one attacks, the other defends
    attack_cards = player1.attacks(trump_suit)
    defended_or_not = "Wrong action"
    while defended_or_not == "Wrong action":
        defended_or_not = player2.defends(attack_cards, trump_suit)
    return defended_or_not

def is_beatable(defend_card, attack_card, trump_suit):
    if defend_card.suit != attack_card.suit and defend_card.suit != trump_suit:
        print("Wrong suit! Try again!")
        return False
    elif defend_card.value < attack_card.value:
        print("Your card is too small to beat it. Try again!")
        return False
    else:
        print("Beaten!")
        return True

def are_equal_cards(card_a, card_b, trump_suit):
    return card_a.value == card_b.value and card_a.suit != trump_suit




    #attack_card = list(comp.deck.random_draw().split())
    # or list(min(comp.deck)) print i for comp.deck.split()[1] if comp.deck.split()[1] = attack_cards[1]
   # print(attack_card)












ALL_CARDS = ['6 hearts', '7 hearts', '8 hearts', '9 hearts', '10 hearts', 'J hearts', 'Q hearts', 'K hearts',
                'A hearts', '6 diamonds', '7 diamonds', '8 diamonds', '9 diamonds', '10 diamonds', 'J diamonds',
                'Q diamonds', 'K diamonds', 'A diamonds', '6 spades', '7 spades', '8 spades', '9 spades', '10 spades',
                'J spades', 'Q spades', 'K spades', 'A spades', '6 clubs', '7 clubs', '8 clubs', '9 clubs', '10 clubs',
                'J clubs', 'Q clubs', 'K clubs', 'A clubs']




