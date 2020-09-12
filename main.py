from utils import *
from cards import Deck, Card
from players import Player, Comp
from constants import *


def start_game():
    print("Game started!")
    name = input('Write your name: ')
    player = Player(name)
    comp = Comp()
    start_deck = Deck()
    start_deck.build()
    start_deck.shuffle()
    player_cards = Deck()
    comps_cards = Deck()
    cards_for_player = start_deck.draw_several_cards(6)
    player_cards.add_cards(cards_for_player)
    cards_for_comp = start_deck.draw_several_cards(6)
    comps_cards.add_cards(cards_for_comp)
    player.deck = player_cards
    print("Here're your cards: ")
    player.deck.show()
    comp.deck = comps_cards
    print("Here're comp's cards: ")
    comp.deck.show()
    return player, comp, start_deck


def define_whose_turn(player, comp, trump_suit):
    player_min_trump_suit = min_trump_suit(trump_suit, player.deck)
    comp_min_trump_suit = min_trump_suit(trump_suit, comp.deck)
    print("Minimal trump suit card of the player: ", VALUES_DICT[player_min_trump_suit])
    print("Minimal trump suit card of the comp: ", VALUES_DICT[comp_min_trump_suit])
    if player_min_trump_suit < comp_min_trump_suit:
        print("Player starts")
        whose_turn = "player"
    else:
        print("Computer starts")
        whose_turn = "comp"
    return whose_turn


def game_cycle(player, comp, trump_suit, deck, whose_turn):
    while (len(player.deck) != 0 or len(comp.deck) != 0) and len(deck) != 0:
        if whose_turn == "player":
            defended_or_not = make_step(player, comp, trump_suit)
            if defended_or_not == True:
                whose_turn = "comp"
        elif whose_turn == "comp":
            defended_or_not = make_step(comp, player, trump_suit)
            if defended_or_not == True:
                whose_turn = "player"
    if len(player.deck) == 0 and len(comp.deck) == 0:
        return "Game over! It's a draw!"
    elif len(player.deck) != 0:
        return "Game over! Computer won!"
    else:
        return "Game over! Player won!"


def main():
    player, comp, start_deck = start_game()
    trump_suit = Card.choose_trump_suit()
    print("The trump suit in this game is:  ", trump_suit)
    whose_turn = define_whose_turn(player, comp, trump_suit)
    game = game_cycle(player, comp, trump_suit, start_deck, whose_turn)
    print(game)


if __name__ == '__main__':
    main()

