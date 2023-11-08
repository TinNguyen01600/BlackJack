'''
This file contains stage functions in a BlackJack round
'''

import classes
import os

def set_up_deck():
    new_deck = classes.Deck()
    new_deck.shuffle()
    return new_deck

def set_up_players(players_list):
    num_of_players = classes.Player.get_integer('Number of Players: ')
    for i in range(num_of_players):
        print(f'Player {i+1}. ')
        player = classes.Player()
        players_list.append(player)
        print()
    return players_list

def set_up_bet(players_list):
    for i in players_list:
        i.place_bet()
        print()  

def dealing(players_list, deck, dealer):
    num_of_players = len(players_list)
    for _ in range(2):
        for i in range(num_of_players):
            players_list[i].add_card(deck.deal_one())
        dealer.add_card(deck.deal_one())

if __name__ == '__main__':
    deck = set_up_deck()
    players_list = set_up_players([])
    dealer = classes.Dealer()
    
    set_up_bet(players_list)
    dealing(players_list, deck, dealer)
    
    for i in players_list:
        print(i)
        i.show_all_cards()
    