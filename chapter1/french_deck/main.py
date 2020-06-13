from random import choice
from chapter1.french_deck.card_deck import FrenchDeck

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    print(card)
    ranked_value = FrenchDeck.rank.index(card.rank)
    return ranked_value * len(suit_values) + suit_values[card.suit]

def show_deck_length(deck):
    print(len(deck))

def show_card_from_index(deck, index):
    card = deck[index]
    print(card)


def show_random_card(deck, times):
    print(choice(deck))
    print(choice(deck))
    print(choice(deck))


if __name__ == '__main__':
    deck = FrenchDeck()

    show_deck_length(deck)
    show_card_from_index(deck, 1)
    show_card_from_index(deck, choice([0, len(deck)-1]))
    show_random_card(deck, times=3)

    for card in sorted(deck, key=spades_high):
        print(card)
