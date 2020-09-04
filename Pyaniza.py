from cards import *


def playPyaniza():
    a_list = []
    a_deck = Deck()
    a_deck.build()
    a_deck.shuffle()
    player_cards = Deck()
    for _ in range(26):
        card = a_deck.draw()
        player_cards.add_card(card)

    comps_cards = Deck()
    for i in range(26):
        card = a_deck.draw()
        comps_cards.add_card(card)

    while len(player_cards) and len(comps_cards):
        a_card = player_cards.draw()
        a_card.show_card()
        b_card = comps_cards.draw()
        b_card.show_card()
        a_list.append(a_card)
        a_list.append(b_card)
        if a_card.value > b_card.value:
            for i in a_list:
                player_cards.add_card(i)
                a_list.clear()
        elif a_card.value == b_card.value:
            continue
        else:
            comps_cards.add_card(a_card)
            comps_cards.add_card(b_card)

    if len(player_cards) == 0:
        print('Comp won')
    elif len(comps_cards) == 0:
        print('Player won')

