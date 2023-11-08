'''
This file contains stage functions in a BlackJack round
'''

import classes
import os

def set_up_deck():
    new_deck = classes.Deck()
    new_deck.shuffle()
    print(new_deck)
    return new_deck

if __name__ == '__main__':
    deck = set_up_deck()
    